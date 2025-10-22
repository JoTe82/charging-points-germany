"""
public charging points in Germany
clean raw data for further analysis

Created by Jochen Teschke
Linkedin: https://www.linkedin.com/in/jochen-teschke/
Tableau public: https://public.tableau.com/app/profile/jochen.teschke

Data Source: The dataset "Liste der Ladesäulen (xlsx, Ladesaeulenregister_BNetzA_2025-09-24.xlsx, 15 MB)" 
was obtained from the "bundesnetzagentur.de"(www.bundesnetzagentur.de). The dataset 
is licensed under the Creative Commons Attribution 4.0 International (CC BY 4.0) license.  

Licence: https://creativecommons.org/licenses/by/4.0/

Modifications: The original dataset was modified during data preparation. Redundant 
columns were removed, missing values cleaned where necessary, spelling errors corrected, 
duplicates deleted, and invalid characters removed.
"""

# import of pandas, sqlalchemy and the self-created module "output"
import pandas as pd
import sqlalchemy as db
import output

# all columns of a DataFrame should be displayed with full width
pd.set_option("display.max_columns", None)
pd.set_option("display.max_colwidth", None)

def del_cell_duplicates(dataset,column):
    """
    a function to delete duplicate values in cells
    """
    # create a copy of the DataFrame and assign it to a local variable
    df = dataset.copy()

    # cell entries of "column" are converted to list items
    df = df.assign(new_split=df[column].astype(str).str.split(";"))

    # each list item becomes a separate row entry for the same row index
    df = df.explode("new_split")

    # whitespaces are deleted
    df["new_split"] = df["new_split"].astype(str).str.strip()

    # completely duplicate rows are deleted
    df = df.drop_duplicates()

    # everything will be put together and assigned to the original DataFrame
    # .join is a build-in function of python-strings and is applied to a delimiter
    dataset[column+"_clean"] = df.groupby(df.index)["new_split"].agg(lambda x: "; ".join(sorted(x)))

    return dataset

def count_values(dataset):
    """
    a function to convert column titles to a list 
    and count values in each column
    """
    # creating a list with all column titles
    column_titles = dataset.columns.tolist()

    # counting values of each column
    for i in column_titles:
        output.spacing(dataset.value_counts(i, ascending=False))

# load dataset
file_path = "https://data.bundesnetzagentur.de/Bundesnetzagentur/DE/Fachthemen/ElektrizitaetundGas/E-Mobilitaet/Ladesaeulenregister_BNetzA_2025-09-24.xlsx"
dataset = pd.read_excel(file_path,skiprows=10)

# the first five rows of the raw dataset should be displayed
output.spacing(dataset.head())

# infos about the raw dataset
print("The structure of the raw dataset:")
dataset.info()
print()

# deleting columns which are not required for further analysis
dataset = dataset.drop(columns=["Anzeigename (Karte)", "Adresszusatz",
                      "Standortbezeichnung","EVSE-ID1","EVSE-ID2","EVSE-ID3","EVSE-ID4",
                      "EVSE-ID5","EVSE-ID6", "Public Key1", "Public Key2", "Public Key3",
                      "Public Key4", "Public Key5", "Public Key6",
                      "Nennleistung Stecker1", "Nennleistung Stecker2", "Nennleistung Stecker3",
                      "Nennleistung Stecker4","Nennleistung Stecker5","Nennleistung Stecker6"])

output.spacing("Not required columns were deleted.")

# infos about the compressed dataset
print("The structure of the compressed dataset:")
dataset.info()
print()

# check for NaN-Values
output.spacing("Checking for NaN-Values:")
output.spacing(dataset.isnull().sum())

# all NaN values will be replaced by "Keine Angabe"
dataset = dataset.fillna("Keine Angabe")

# check for NaN-Values after replacing them
output.spacing("All NaN-values were replaced by \"Keine Angabe\":")
output.spacing(dataset.isnull().sum())

# call a function to count the values of each column
count_values(dataset)

# after counting values a second test to look for duplicate rows and IDs
output.spacing("There are "+ str(dataset.duplicated(subset=["Ladeeinrichtungs-ID"]).sum()) +" duplicate IDs.")
output.spacing("There are "+ str(dataset.duplicated().sum())+" duplicate rows.")

# calling a function to delete duplicates within cells of certain columns
dataset = del_cell_duplicates(dataset,"Bezahlsysteme")
dataset = del_cell_duplicates(dataset,"Steckertypen1")
dataset = del_cell_duplicates(dataset,"Steckertypen2")
dataset = del_cell_duplicates(dataset,"Steckertypen3")
dataset = del_cell_duplicates(dataset,"Steckertypen4")
dataset = del_cell_duplicates(dataset,"Steckertypen5")
dataset = del_cell_duplicates(dataset,"Steckertypen6")
output.spacing("Duplicates within cells were removed in all affected columns.")

# call a function to count the values of each column after deleting the duplicates within cells
count_values(dataset)

# deleting wrong leading characters from column "Hausnummer"
unique = pd.unique(dataset["Hausnummer"]).tolist()
unique.sort()
print(unique[:40],"...",unique[-40:])
print()
dataset["Hausnummer"] = dataset["Hausnummer"].str.strip(" \"!.´ ")
dataset["Hausnummer"] = dataset["Hausnummer"].replace({"1-":"1",
                                                       "1 ":"1",
                                                       "01":"1",
                                                       "05":"5", 
                                                       "00":"0",
                                                       "0\"":"0"
                                                       })
dataset["Hausnummer"] = dataset["Hausnummer"].replace({r"^\s+1":"1",
                                                       r"^\s+":"-"},
                                                       regex=True)
output.spacing("The wrong leading characters from column \"Hausnummer\" were deleted.")

# the new column "Bezahlsysteme_clean" has leading characters which should be removed
# and the value "Sonstige" should be replaced by "Keine Angabe"
dataset["Bezahlsysteme_clean"] = dataset["Bezahlsysteme_clean"].str.strip("; ")
dataset["Bezahlsysteme_clean"] = dataset["Bezahlsysteme_clean"].replace("Sonstige", "Keine Angabe")
output.spacing("In column \"Bezahlsysteme_clean\" the term \"Sonstige\" was replaced by \"Keine Angabe\"")

# in column "Informationen zum Parkraum" are identical values
# which are treated as two different values
# therefore the spelling of one of theses values will be adjusted
dataset["Informationen zum Parkraum"] = dataset["Informationen zum Parkraum"].replace("keine Beschränkung", "Keine Beschränkung")
output.spacing("The spelling of some values in column \"Informationen zum Parkraum\" were adjusted.")

# intermediate step to display the infos about the dataset
dataset.info()

# dropping the columns with duplicates within their cells
dataset = dataset.drop(columns=["Bezahlsysteme", "Steckertypen1", "Steckertypen2",
                                "Steckertypen3", "Steckertypen4", "Steckertypen5",
                                "Steckertypen6"])
output.spacing("The columns with duplicates within their cells were deleted.")

# rename the columns with the appendix _clean
dataset = dataset.rename(columns={"Bezahlsysteme_clean": "Bezahlsysteme",
                                  "Steckertypen1_clean": "Steckertypen1",
                                  "Steckertypen2_clean": "Steckertypen2",
                                  "Steckertypen3_clean": "Steckertypen3",
                                  "Steckertypen4_clean": "Steckertypen4",
                                  "Steckertypen5_clean": "Steckertypen5",
                                  "Steckertypen6_clean": "Steckertypen6",
                                  })
output.spacing("The columns with the appendix \"_clean\" were renamed.")

# call a function to count the values of each column to perform a final evaluation
count_values(dataset)

# final infos about the cleaned dataset
print("The structure of the cleaned dataset:")
dataset.info()

# create engines for MySQL and PostgreSQL
engine_mysql = db.create_engine("mysql+mysqlconnector://<username>:<password>@<hostname>:<port>/<database>")
engine_postgresql = db.create_engine("postgresql+psycopg2://<username>:<password>@<hostname>:<port>/<database>")
print("The engines for MySQL and PostgreSQL were created.")
print()

# full upload of the clean dataset into databases and saving as an excel file
# the old dataset will be replaced
dataset.to_sql("<table_name>", con=engine_mysql, if_exists="replace")
dataset.to_sql("<table_name>", con=engine_postgresql, if_exists="replace")
dataset.to_excel(r"....\<filename>.xlsx",sheet_name="<sheet_name>", index=False)
print("The dataset was uploaded to MySQL and PostgreSQL.")
print("The cleaned dataset was saved as an Excel sheet.")

