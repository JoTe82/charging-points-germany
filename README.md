# Analysis of the German charging points infrastructure
A published and freely accessible dataset from bundesnetzagentur.de was extracted and prepared for further analysis as part of a data wrangling process.
The dataset was then analyzed and visualized using Tableau to create a dashboard that will be updated monthly.

## Motivation / Goal
  ### Why does the project exist?
  - This project was carried out to practice all steps of a data analysis with a real world dataset
  - As a part of my continuing education becoming a data analyst

  ### Which steps of a data analysis process was practised?
  - Dataset extraction from an internet resource
  - Discovery / Exploration of the dataset
  - Data cleaning and transformation
  - Loading to databases
  - Visualization of the data
  - Creating an interactive dashboard

  ### Which tools where used?
  - python (pandas, sqlalchemy)
  - Jupyter Notebook
  - MySQL
  - PostgreSQL
  - Tableau

  ### What results does the analysis and its visualization provide?
  - Total number of charging points in Germany and the figures for annual expansion (trend)
  - How many charging points are normal charging devices or fast charging devices
  - the current status of the charging points
  - the total rated power in kW
  - Germany-wide coverage with public charging points
  - and the interactive filter option by historical extent, “federal state”, “district/independent city”, “location” and “operator”

## Dashboard
<div class='tableauPlaceholder' id='viz1761127883716' style='position: relative'><noscript><a href='#'><img alt='Öffentlich zugängliche Ladepunkte in Deutschland, Stand:24.09.2025 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;ff&#47;ffentlichzugnglicheLadepunkteinDeutschland&#47;ffentlichzugnglicheLadepunkteinDeutschland&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='ffentlichzugnglicheLadepunkteinDeutschland&#47;ffentlichzugnglicheLadepunkteinDeutschland' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;ff&#47;ffentlichzugnglicheLadepunkteinDeutschland&#47;ffentlichzugnglicheLadepunkteinDeutschland&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='de-DE' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1761127883716');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='1650px';vizElement.style.height='891px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='1650px';vizElement.style.height='891px';} else { vizElement.style.width='100%';vizElement.style.height='2027px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>

## Link / Lizenz 
The dataset "Liste der Ladesäulen (xlsx, Ladesaeulenregister_BNetzA_2025-09-24.xlsx, 15 MB)"  was obtained from the "bundesnetzagentur.de"(www.bundesnetzagentur.de). 
The dataset is licensed under the Creative Commons Attribution 4.0 International (CC BY 4.0) license. 

Licence: https://creativecommons.org/licenses/by/4.0/

## Contact

- Jochen Teschke
- E-mail: jochen.teschke@web.de
- Linkedin: https://www.linkedin.com/in/jochen-teschke/   
- Tableau public: https://public.tableau.com/app/profile/jochen.teschke

