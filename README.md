# Evaluating Carbon Emissions of Steel Plants in the United States

![image](https://github.com/steeltracker/carbon-analysis/blob/main/steel-plants.jpg)

## Project Motivation
#### Goal
Calculate and analyze the weekly and annual emissions intensity of electrified steel production in the United States at the individual plant level. 
#### Background
Approximately 70% of steel produced in the US is from electrified steel plants which use EAF (Electric Arc Furnace) as opposed to the traditional blast furnaces that rely heavily on coal. Blast furnaces comparatively create more direct emissions from burning the coal on site to create steel and EAF steel plants produce emissions off site when using the power needed to melt scrap and direct-reduce iron (DRI) inputs. While there is data on the direct emissions (Scope 1) from steel plants, there is a lack of transparency regarding the indirect emissions (Scope 2) and this project aimed to bridge that knowledge gap. 

## How to Install and Run the Project
#### 1. Fork and clone this repo
#### 2. Download and unzip the data folder and save the data in the following folder path: carbon-analysis/data/. Two of the five datasets, EPA flight data and eGrid data can be downloaded directly from the links below. The eGrid shape file is too large so it must be downloaded from the link provided below. The AISI data requires one to reach out and the GEM data requires one to complete a quick form to track the users. You can also find the links to the datasets below:

##### AISI (American Iron and Steel Institute): Contact Caitlin Swalec at *caitlin.swalec@globalenergymonitor.org* to obtain data
###### - Date of Data Collection: January 2023
###### - Number of variables: 33
###### - Number of rows: 109
###### - File name read in to analysis: AISI_data.xlsx, AISI_regions.xlsx
###### - List of variables used from the dataset: Great Lakes region capacity utilization, Midwest region capacity utilization, Southern region capacity utilization, Western region capacity utilization, North East region capacity utilization

##### [GEM (Global Energy Monitor)](https://globalenergymonitor.org/projects/global-steel-plant-tracker/download-data/): Scroll down and enter your email, name, and organization to obtain the data. This measure is put in place to track the individuals accessing the data.
###### - Date of Data Collection: January 2023
###### - Number of variables: 51
###### - Number of rows: 1433
###### - File name read in to analysis: GEM_2022_data.xlsx
###### - List of variables used from the dataset: Country, Status, Plant ID, Plant Name, Owner, Coordinates, State, Start Date, Plant Age, Address, Municipality, EAF Capacity 

##### [EPA eGrid](https://www.epa.gov/egrid/download-data): Click "Download eGRID2021 (xlsx)" and use sheet "SRL21"
###### - Date of Data Collection: January 2023
###### - Number of variables: 164
###### - Number of rows: 27
###### - File name read in to analysis: eGRID2021_data.xlsx
###### - List of variables used from the dataset: eGrid Subregion Name, eGrid Subregion Acronym, eGRID subregion annual CO2 combustion output emission rate (lb/MWh)

##### [EPA GHG Reporting Program](https://ghgdata.epa.gov/ghgp/main.do#/facility/?q=Find%20a%20Facility%20or%20Location&st=&bs=&et=&fid=&sf=11001100&lowE=-20000&highE=23000000&g1=1&g2=0&g3=0&g4=0&g5=0&g6=0&g7=0&g8=0&g9=0&g10=0&g11=0&g12=0&s1=0&s2=0&s3=1&s4=0&s5=0&s6=0&s7=0&s8=0&s9=0&s10=0&s201=0&s202=0&s203=0&s204=0&s301=0&s302=0&s303=1&s304=0&s305=0&s306=0&s307=0&s401=0&s402=0&s403=0&s404=0&s405=0&s601=0&s602=0&s701=0&s702=0&s703=0&s704=0&s705=0&s706=0&s707=0&s708=0&s709=0&s710=0&s711=0&s801=0&s802=0&s803=0&s804=0&s805=0&s806=0&s807=0&s808=0&s809=0&s810=0&s901=0&s902=0&s903=0&s904=0&s905=0&s906=0&s907=0&s908=0&s909=0&s910=0&s911=0&si=&ss=&so=0&ds=E&yr=2021&tr=current&cyr=2021&ol=0&sl=0&rs=ALL): Filter the Sector so only "Iron & Steel Production" is selected and then Export Data 
###### - Date of Data Collection: January 2023
###### - Number of variables: 13
###### - Number of rows: 135
###### - File name read in to analysis: GHG_flight_scope1.xls
###### - List of variables used from the dataset: GHGRP ID, Zip Code, GHG Quantity Metric Tons CO2e, Latitude, Longitude

##### [eGrid Subregions Shapefile](https://www.epa.gov/egrid/egrid-mapping-files): Under year 2020, click "eGRID2020 Subregions Shapefile (zip)"
###### - Date of Data Collection: January 2023
###### - File name read in to analysis: eGRID2020_subregions.shp

#### 3. The repository offers the same information through both R and Python analyses, providing users with the flexibility to choose the language they are most comfortable using. You can run all the code to acquire the tables and visualizations created in the respective programming languages. 
The data is not stored within the repo, but can be accessed through the links and contacts listed above. The analysis folder has the R markdown and Python Notebook for calculating the Scope 2 emissiosn and emissions intensity. The summary folder contains a document summarizing some of the findings from these calculations. The output data is not stored in this repo, but it can also be requested from caitlin.swalec@globalenergymonitor.org. The deliverables folder contains the technical documentation of the project. The references folder includes the citations saved as pdfs. The references folder contains the Global Efficiency Intelligience report that contains the energy intensity value for EAF scrap steel production on page 39, Table 10. Below is the structure of this repository: 

	A.	steel_co2e_2021_analysis.R
	B. 	steel_co2e_2021_analysis.ipynb
	C.	summary
			i. summary_analysis.qmd
			ii. summary_analysis.pdf
	D.	deliverables
			i. technical_documentaion.docx
	E.	references
			i. hasenbeigi_GEI_report.pdf
	F. 	README.md

We recommend storing the input data in a directory one level above your project directory as shown:

Data
	i. aisi_2021_util_rate.xlsx
	ii. gem_2022_plant_info.xlsx
	iii. egrid_2021_emissions_intensity.xlsx
	iv. flight_2021_scope1_emissions.xls
	v. egrid_2020_subregions
		a.egrid_2020_subregions.shp
	
#### 4. The interactive map is hosted on the Tableau server and can be found here.

https://public.tableau.com/app/profile/steel.tracker

## Collaborators 
If you have any questions, comments, or concerns, please reach out to a team member using the information below:

##### Erica Bishop,      Github: @erica-bishop,     Email: ericabishop@bren.ucsb.edu

##### Ruth Enriquez,     Github: @ruthe808,         Email: rbe786@bren.ucsb.edu

##### Amrit Sandhu,      Github: @aksandhu23,       Email: aksandhu@bren.ucsb.edu

##### Michael Zargari,   Github: @mzargari,         Email: mzargari@bren.ucsb.edu

*Affiliation: This project was carried out as a part of the Masters in Environmental Data Science program at UC Santa Barbara. The client for this project was [Global Energy Monitor(GEM)](https://globalenergymonitor.org/projects/global-steel-plant-tracker/), an organization dedicated to heavy industry decarbonization. The primary contact from GEM was Caitlin Swalec and the faculty advisor from the Bren School of Environment was Roland Geyer.*

## References 

Emissions & Generation Resource Integrated Database (eGRID) https://www.epa.gov/egrid.

Global Energy Monitor. Global Steel Plant Tracker. https://globalenergymonitor.org/projects/global-steel-plant-tracker/. 

Hasanbeigi, A. 2022. Steel Climate Impact. https://www.globalefficiencyintel.com/steel-climate-impact-international-benchmarking-energy-co2-intensities.

Hasanbeigi, A. 2022. What is Green Steel? https://www.globalefficiencyintel.com/what-is-green-steel. 

World Steel Association. World Steel in Figures 2022. https://worldsteel.org/steel-topics/statistics/world-steel-in-figures-2022/#major-steel-producing-countries-2021-and-2020.  

