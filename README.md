# Evaluating Carbon Emissions of Steel Plants in the United States

![image](https://github.com/steeltracker/carbon-analysis/blob/main/steel-plant-night.jpg)

## Project Motivation
#### Goal
Calculate and analyze the weekly and annual emissions intensity of electrified steel production in the United States at the individual plant level. 
#### Background
Approximately 70% of steel produced in the US is from electrified steel plants which use EAF (Electric Arc Furnace) as opposed to the traditional blast furnaces that rely heavily on coal. Blast furnaces comparatively create more direct emissions from burning the coal on site to create steel and EAF steel plants produce emissions off site when using the power needed to melt scrap and direct-reduce iron (DRI) inputs. While there is data on the direct emissions (Scope 1) from steel plants, there is a lack of transparency regarding the indirect emissions (Scope 2) and this project aimed to bridge that knowledge gap. 

## How to Install and Run the Project
#### 1. Fork and clone this repo
#### 2. Download and unzip the data folder and save the data in the following folder path: carbon-analysis/data/. The data is in a zip folder, because some files were too large. 
You can also find the links to the datasets below:

###### AISI (American Iron and Steel Institute):
###### GEM (Global Energy Monitor): Contact 
###### EPA eGrid:
###### EPA GHG Reporting Program:
###### eGrid Subregions Shapefile(zip): https://www.epa.gov/egrid/egrid-mapping-files  

#### 3. The repository offers the same information through both R and Python analyses, providing users with the flexibility to choose the language they are most comfortable using. You can run all the code to acquire the tables and visualizations created in the respective programming languages. 
The data folder contains all 5 datsets used to conduct the analysis. The analysis folder has the R markdown and Python Notebook. The output data folder has the final dataframes after joining the required data. The deliverables folder contains the technical documentation of the project and a summary of the analysis. The references folder includes the citations saved as pdfs. Below is the structure of this repository: 

	A.	steel_carbon_emissions_analysis
		a.	data
			i.	gem_2022_plant_info.xlsx
			ii.	egrid_2020_subregions.shp
			iii.	egrid_2021_emissions_intensity.xlsx
			iv.	aisi_2021_util_rate.xlsx
			v.	flight_2021_scope1_emissions.xls
		b.	analysis
			i.	steel_carbon_analysis.R
			ii.	steel_carbon_analsysis.ipynb
		c.	output_data
			i.	scope2_emissions_annual_weekly.csv
			ii.	scope1_and_scope2_emissions_annual.csv
	B.	deliverables
		a.      technical_documentaion.docx
		b.	summary_of_analysis.docx
	C.	references
		a.	hasenbeigi_GEI_report.pdf
		b.	swalec_GEM_report.pdf
	
#### 4. The interactive map is hosted on the Tableau server and can be found here.

## Collaborators 
If you have any questions, comments, or concerns, please reach out to a team member using the information below:

Erica Bishop,      Github: @erica-bishop,     Email: ericabishop@bren.ucsb.edu

Ruth Enriquez,     Github: @ruthe808,         Email: rbe786@bren.ucsb.edu

Amrit Sandhu,      Github: @aksandhu23,       Email: aksandhu@bren.ucsb.edu

Michael Zargari,   Github: @mzargari,         Email: mzargari@bren.ucsb.edu

## References 
Hasanbeigi, A. 2022. Steel Climate Impact. https://www.globalefficiencyintel.com/steel-climate-impact-international-benchmarking-energy-co2-intensities.

World Steel Association. World Steel in Figures 2022. https://worldsteel.org/steel-topics/statistics/world-steel-in-figures-2022/#major-steel-producing-countries-2021-and-2020.  

Hasanbeigi, A. 2022. What is Green Steel? https://www.globalefficiencyintel.com/what-is-green-steel. 

Global Energy Monitor. Global Steel Plant Tracker. https://globalenergymonitor.org/projects/global-steel-plant-tracker/. 

Emissions & Generation Resource Integrated Database (eGRID) https://www.epa.gov/egrid.

