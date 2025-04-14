import pandas as pd
import os
from glob import glob

Cal_fire_inc = pd.read_csv(r"C:\Users\mattl\OneDrive\Desktop\DATA 501\Datasets\California Wildfires\California_Fire_Incidents (2013 - 2020).csv", encoding="ISO-8859-1")
NFD_area_burn_cause_class = pd.read_csv(r"C:\Users\mattl\OneDrive\Desktop\DATA 501\Datasets\Canadian National Forestry Database\NFD - Area burned by cause class - EN FR.csv", encoding="ISO-8859-1")
NFD_area_burn_fire_size = pd.read_csv(r"C:\Users\mattl\OneDrive\Desktop\DATA 501\Datasets\Canadian National Forestry Database\NFD - Area burned by fire size class - EN FR.csv", encoding="ISO-8859-1")
NFD_area_burn_bymonth = pd.read_csv(r"C:\Users\mattl\OneDrive\Desktop\DATA 501\Datasets\Canadian National Forestry Database\NFD - Area burned by month - EN FR.csv", encoding="ISO-8859-1")
NFD_num_fires_bycauseclass = pd.read_csv(r"C:\Users\mattl\OneDrive\Desktop\DATA 501\Datasets\Canadian National Forestry Database\NFD - Number of fires by cause class - EN FR.csv", encoding="ISO-8859-1")
NFD_num_fires_sizeclass = pd.read_csv(r"C:\Users\mattl\OneDrive\Desktop\DATA 501\Datasets\Canadian National Forestry Database\NFD - Number of fires by fire size class - EN FR.csv", encoding="ISO-8859-1")
NFD_num_fires_bymonth = pd.read_csv(r"C:\Users\mattl\OneDrive\Desktop\DATA 501\Datasets\Canadian National Forestry Database\NFD - Number of fires by month - EN FR.csv", encoding="ISO-8859-1")
NFD_property_loss_byfire = pd.read_csv(r"C:\Users\mattl\OneDrive\Desktop\DATA 501\Datasets\Canadian National Forestry Database\NFD - Property losses from fires - EN FR.csv", encoding="ISO-8859-1")
Canada_Weather_Daily = pd.read_csv(r"C:\Users\mattl\OneDrive\Desktop\DATA 501\Datasets\Canada Weather\Canadian_climate_daily_original.csv", encoding="ISO-8859-1")
Arrow_Zone_2020 = pd.read_csv(r"C:\Users\mattl\OneDrive\Desktop\DATA 501\VS Code - Python (DATA 501)\Datasets\Canada Weather\BC Wildfire Weather Stations\Arrow\2020 - Arrow Zone Weather Data (May - October).csv", encoding="ISO-8859-1")
Arrow_Zone_2021 = pd.read_csv(r"C:\Users\mattl\OneDrive\Desktop\DATA 501\VS Code - Python (DATA 501)\Datasets\Canada Weather\BC Wildfire Weather Stations\Arrow\2021 - Arrow Zone Weather Data (May - October).csv", encoding="ISO-8859-1")
Arrow_Zone_2022 = pd.read_csv(r"C:\Users\mattl\OneDrive\Desktop\DATA 501\VS Code - Python (DATA 501)\Datasets\Canada Weather\BC Wildfire Weather Stations\Arrow\2022 - Arrow Zone Weather Data (May - October).csv", encoding="ISO-8859-1")
Arrow_Zone_2023 = pd.read_csv(r"C:\Users\mattl\OneDrive\Desktop\DATA 501\VS Code - Python (DATA 501)\Datasets\Canada Weather\BC Wildfire Weather Stations\Arrow\2023 - Arrow Zone Weather Data (May - October).csv", encoding="ISO-8859-1")
Arrow_Zone_2024 = pd.read_csv(r"C:\Users\mattl\OneDrive\Desktop\DATA 501\VS Code - Python (DATA 501)\Datasets\Canada Weather\BC Wildfire Weather Stations\Arrow\2024 - Arrow Zone Weather Data (May - October).csv", encoding="ISO-8859-1")
Fort_Nelson_2020 = pd.read_csv(r"C:\Users\mattl\OneDrive\Desktop\DATA 501\VS Code - Python (DATA 501)\Datasets\Canada Weather\BC Wildfire Weather Stations\Fort Nelson\2020 - Fort Nelson Weather Data (May - October).csv", encoding="ISO-8859-1")
Fort_Nelson_2021 = pd.read_csv(r"C:\Users\mattl\OneDrive\Desktop\DATA 501\VS Code - Python (DATA 501)\Datasets\Canada Weather\BC Wildfire Weather Stations\Fort Nelson\2021 - Fort Nelson Weather Data (May - October).csv", encoding="ISO-8859-1")
Fort_Nelson_2022 = pd.read_csv(r"C:\Users\mattl\OneDrive\Desktop\DATA 501\VS Code - Python (DATA 501)\Datasets\Canada Weather\BC Wildfire Weather Stations\Fort Nelson\2022 - Fort Nelson Weather Data (May - October).csv", encoding="ISO-8859-1")
Fort_Nelson_2023 = pd.read_csv(r"C:\Users\mattl\OneDrive\Desktop\DATA 501\VS Code - Python (DATA 501)\Datasets\Canada Weather\BC Wildfire Weather Stations\Fort Nelson\2023 - Fort Nelson Weather Data (May - October).csv", encoding="ISO-8859-1")
Fort_Nelson_2024 = pd.read_csv(r"C:\Users\mattl\OneDrive\Desktop\DATA 501\VS Code - Python (DATA 501)\Datasets\Canada Weather\BC Wildfire Weather Stations\Fort Nelson\2024 - Fort Nelson Weather Data (May - October).csv", encoding="ISO-8859-1")
Kamloops_2020 = pd.read_csv(r"C:\Users\mattl\OneDrive\Desktop\DATA 501\VS Code - Python (DATA 501)\Datasets\Canada Weather\BC Wildfire Weather Stations\Kamloops\2020 - Kamloops Zone Weather Data (May - October).csv", encoding="ISO-8859-1")
Kamloops_2021 = pd.read_csv(r"C:\Users\mattl\OneDrive\Desktop\DATA 501\VS Code - Python (DATA 501)\Datasets\Canada Weather\BC Wildfire Weather Stations\Kamloops\2021 - Kamloops Zone Weather Data (May - October).csv", encoding="ISO-8859-1")
Kamloops_2022 = pd.read_csv(r"C:\Users\mattl\OneDrive\Desktop\DATA 501\VS Code - Python (DATA 501)\Datasets\Canada Weather\BC Wildfire Weather Stations\Kamloops\2022 - Kamloops Zone Weather Data (May - October).csv", encoding="ISO-8859-1")
Kamloops_2023 = pd.read_csv(r"C:\Users\mattl\OneDrive\Desktop\DATA 501\VS Code - Python (DATA 501)\Datasets\Canada Weather\BC Wildfire Weather Stations\Kamloops\2023 - Kamloops Zone Weather Data (May - October).csv", encoding="ISO-8859-1")
Kamloops_2024 = pd.read_csv(r"C:\Users\mattl\OneDrive\Desktop\DATA 501\VS Code - Python (DATA 501)\Datasets\Canada Weather\BC Wildfire Weather Stations\Kamloops\2024 - Kamloops Zone Weather Data (May - October).csv", encoding="ISO-8859-1")
Mid_Island_2020 = pd.read_csv(r"C:\Users\mattl\OneDrive\Desktop\DATA 501\VS Code - Python (DATA 501)\Datasets\Canada Weather\BC Wildfire Weather Stations\Mid-Island\2020 - Mid-Island Zone Weather Data (May - October).csv", encoding="ISO-8859-1")
Mid_Island_2021 = pd.read_csv(r"C:\Users\mattl\OneDrive\Desktop\DATA 501\VS Code - Python (DATA 501)\Datasets\Canada Weather\BC Wildfire Weather Stations\Mid-Island\2021 - Mid-Island Zone Weather Data (May - October).csv", encoding="ISO-8859-1")
Mid_Island_2022 = pd.read_csv(r"C:\Users\mattl\OneDrive\Desktop\DATA 501\VS Code - Python (DATA 501)\Datasets\Canada Weather\BC Wildfire Weather Stations\Mid-Island\2022 - Mid-Island Zone Weather Data (May - October).csv", encoding="ISO-8859-1")
Mid_Island_2023 = pd.read_csv(r"C:\Users\mattl\OneDrive\Desktop\DATA 501\VS Code - Python (DATA 501)\Datasets\Canada Weather\BC Wildfire Weather Stations\Mid-Island\2023 - Mid-Island Zone Weather Data (May - October).csv", encoding="ISO-8859-1")
Mid_Island_2024 = pd.read_csv(r"C:\Users\mattl\OneDrive\Desktop\DATA 501\VS Code - Python (DATA 501)\Datasets\Canada Weather\BC Wildfire Weather Stations\Mid-Island\2024 - Mid-Island Zone Weather Data (May - October).csv", encoding="ISO-8859-1")
Robson_2020 = pd.read_csv(r"C:\Users\mattl\OneDrive\Desktop\DATA 501\VS Code - Python (DATA 501)\Datasets\Canada Weather\BC Wildfire Weather Stations\Robson\2020 - Valemount Weather Data (May - October).csv", encoding="ISO-8859-1")
Robson_2021 = pd.read_csv(r"C:\Users\mattl\OneDrive\Desktop\DATA 501\VS Code - Python (DATA 501)\Datasets\Canada Weather\BC Wildfire Weather Stations\Robson\2021 - Valemount Weather Data (May - October).csv", encoding="ISO-8859-1")
Robson_2022 = pd.read_csv(r"C:\Users\mattl\OneDrive\Desktop\DATA 501\VS Code - Python (DATA 501)\Datasets\Canada Weather\BC Wildfire Weather Stations\Robson\2022 - Valemount Weather Data (May - October).csv", encoding="ISO-8859-1")
Robson_2023 = pd.read_csv(r"C:\Users\mattl\OneDrive\Desktop\DATA 501\VS Code - Python (DATA 501)\Datasets\Canada Weather\BC Wildfire Weather Stations\Robson\2023 - Valemount Weather Data (May - October).csv", encoding="ISO-8859-1")
Robson_2024 = pd.read_csv(r"C:\Users\mattl\OneDrive\Desktop\DATA 501\VS Code - Python (DATA 501)\Datasets\Canada Weather\BC Wildfire Weather Stations\Robson\2024 - Valemount Weather Data (May - October).csv", encoding="ISO-8859-1")

#Converts acres to hectares
Cal_fire_inc["HectaresBurned"] = Cal_fire_inc["AcresBurned"] * 0.404686

#Drops unnecessary columns
Cal_fire_inc.drop(columns=["AcresBurned", "Active", "AdminUnit", "CountyIds", "Featured",
                           "Name", "PercentContained", "Public", "Status"], inplace=True)

#Assigns numerical values to months
month_map = {
    "January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6,
    "July": 7, "August": 8, "September": 9, "October": 10, "November": 11, "December": 12
}

#Replaces all months of the year with numerical values
for df in [NFD_num_fires_bymonth, NFD_area_burn_bymonth]:
    df.loc[:, "Month"] = df["Month"].map(month_map)

#Creates new column with Year-Month formatting
for df in [NFD_num_fires_bymonth, NFD_area_burn_bymonth]:
    df["Month"] = df["Month"].fillna(1).astype(int)
    df["Year-Month"] = df["Year"].astype(str) + "-" + df["Month"].apply(lambda x: f"{x:02d}")

#Drops all unnecessary columns in the NFD datasets
drop_columns = {
    "NFD_area_burn_cause_class": ["Année", "Juridiction", "Origine", "Data Qualifier", "Superficie (en hectare)", "Qualificatifs de données"],
    "NFD_area_burn_fire_size": ["Année", "Juridiction", "Classe de superficie à l'extinction", "Data Qualifier", "Superficie (en hectare)", "Qualificatifs de données"],
    "NFD_area_burn_bymonth": ["Year", "Month", "Année", "Juridiction", "Mois", "Data Qualifier", "Superficie (en hectare)", "Qualificatifs de données"],
    "NFD_num_fires_bycauseclass": ["Année", "Juridiction", "Origine", "Data Qualifier", "Nombre", "Qualificatifs de données"],
    "NFD_num_fires_sizeclass": ["Année", "Juridiction", "Classe de superficie à l'extinction", "Data Qualifier", "Nombre", "Qualificatifs de données"],
    "NFD_num_fires_bymonth": ["Year", "Month", "Année", "Juridiction", "Mois", "Data Qualifier", "Nombre", "Qualificatifs de données"],
    "NFD_property_loss_byfire": ["Année", "Juridiction", "Zone de protection", "Data qualifier", "Dollars (Fr)", "Qualificatifs de données"]
}

for df_name, cols in drop_columns.items():
    df = globals()[df_name] 
    df.drop(columns=cols, inplace=True)

#Renames the column Jurisdiction to Province. 
for df in [NFD_area_burn_cause_class, NFD_area_burn_fire_size, NFD_area_burn_bymonth, 
           NFD_num_fires_sizeclass, NFD_num_fires_bymonth, NFD_property_loss_byfire]:
    df.rename(columns={"Jurisdiction": "Province"}, inplace=True)

#Filters data between 1990 and 2019
Canada_Weather_Daily = Canada_Weather_Daily.query('"1990-01-01" <= LOCAL_DATE <= "2019-12-31"')

#Converts dates to proper format and sets index
Canada_Weather_Daily.loc[:, "LOCAL_DATE"] = pd.to_datetime(Canada_Weather_Daily["LOCAL_DATE"])
Canada_Weather_Daily.set_index("LOCAL_DATE", inplace=True)

#Creates list for all columns containing temperature and precipitation
temp_columns = [col for col in Canada_Weather_Daily.columns if "TEMPERATURE" in col.upper()]
precip_columns = [col for col in Canada_Weather_Daily.columns if "PRECIPITATION" in col.upper()]

#Computes daily average precip and temp
Canada_Weather_Daily.loc[:, "CANADA_TEMPERATURE"] = Canada_Weather_Daily[temp_columns].mean(axis=1)
Canada_Weather_Daily.loc[:, "CANADA_PRECIPITATION"] = Canada_Weather_Daily[precip_columns].mean(axis=1)
Canada_Weather_Daily.reset_index(inplace=True)

#Calculates monthly averages and formats date
Canada_Weather_Monthly = Canada_Weather_Daily.resample("M", on="LOCAL_DATE").mean().reset_index()
Canada_Weather_Monthly["LOCAL_DATE"] = Canada_Weather_Monthly["LOCAL_DATE"].dt.to_period("M").astype(str)

#Calculates yearly averages and formats date
Canada_Weather_Yearly = Canada_Weather_Daily.resample("Y", on="LOCAL_DATE").mean().reset_index()
Canada_Weather_Yearly["LOCAL_DATE"] = Canada_Weather_Yearly["LOCAL_DATE"].dt.to_period("Y").astype(str)

#Defines file naming schema based off location
location_file_patterns = {
    "Arrow": "{} - Arrow Zone Weather Data (May - October).csv",
    "Fort Nelson": "{} - Fort Nelson Weather Data (May - October).csv",
    "Kamloops": "{} - Kamloops Zone Weather Data (May - October).csv",
    "Mid-Island": "{} - Mid-Island Zone Weather Data (May - October).csv",
    "Robson": "{} - Valemount Weather Data (May - October).csv"
}

#Creates a function to consolidate daily weather data
def consolidate_weather_data(location, years, base_path):
    data_frames = []

    #For each year, pull files from each location
    for year in years:
        filename_pattern = location_file_patterns.get(location)
        file_name = filename_pattern.format(year)
        file_path = os.path.join(base_path, location, file_name)
        #Read csv file and add year column
        df = pd.read_csv(file_path, encoding="ISO-8859-1")
        df["Year"] = year
        data_frames.append(df)

    #Consolidates all data into a single df 
    if data_frames:
        consolidated_df = pd.concat(data_frames, ignore_index=True)
        output_file = os.path.join(base_path, f"{location}_Weather_Data_2020_2024.csv")
        consolidated_df.to_csv(output_file, index=False, encoding="ISO-8859-1")
    else:
        print(f"No data to consolidate for {location}")


base_path = r"C:\Users\mattl\OneDrive\Desktop\DATA 501\VS Code - Python (DATA 501)\Datasets\Canada Weather\BC Wildfire Weather Stations"
locations = ["Arrow", "Fort Nelson", "Kamloops", "Mid-Island", "Robson"]
years = [2020, 2021, 2022, 2023, 2024]

#Runs consolidate_weather_data for location and years
for location in locations:
    consolidate_weather_data(location, years, base_path)

#Uses glob to find the newly create files paths
consolidated_path = r"C:\Users\mattl\OneDrive\Desktop\DATA 501\VS Code - Python (DATA 501)\Datasets\Canada Weather\BC Wildfire Weather Stations"
consolidated_files = glob(os.path.join(consolidated_path, "*_Weather_Data_2020_2024.csv"))

#Creates blank list
all_data = []

#Combines all datasets into one large dataset
for file in consolidated_files:
    df = pd.read_csv(file, encoding="ISO-8859-1")
    df.columns = [col.strip() for col in df.columns]
    date_col_candidates = [col for col in df.columns if 'date' in col.lower()]
    df['Date'] = pd.to_datetime(df[date_col_candidates[0]], errors='coerce')
    df = df.dropna(subset=['Date'])
    all_data.append(df)

#Calculates daily averages for all files consolidated above
if all_data:
    combined_df = pd.concat(all_data, ignore_index=True)
    numeric_cols = combined_df.select_dtypes(include='number').columns
    averaged_df = combined_df.groupby("Date")[numeric_cols].mean().reset_index()
    output_file = os.path.join(consolidated_path, "All_Weather_Zones_Daily_Average_2020_2024.csv")
    averaged_df.to_csv(output_file, index=False, encoding="ISO-8859-1")
else:
    print("No data was found to combine and average")

#Produces csv files for all cleaned dataframes
output_files = {
    "Califonia Fire Incidents (Cleaned).csv": Cal_fire_inc,
    "NFD - Area Burned by Cause Class (Cleaned).csv": NFD_area_burn_cause_class,
    "NFD - Area Burned by Fire Size (Cleaned).csv": NFD_area_burn_fire_size,
    "NFD - Area Burned by Month (Cleaned).csv": NFD_area_burn_bymonth,
    "NFD - Number of Fires by Cause Class (Cleaned).csv": NFD_num_fires_bycauseclass,
    "NFD - Number of Fires by Size Class (Cleaned).csv": NFD_num_fires_sizeclass,
    "NFD - Number of Fires by Month (Cleaned).csv": NFD_num_fires_bymonth,
    "NFD - Property Loss by Fire (Cleaned).csv": NFD_property_loss_byfire,
    "Canadian_Climate_Data_Daily_1990-2019(Cleaned).csv": Canada_Weather_Daily,
    "Canadian_Climate_Data_Monthly_1990-2019(Cleaned).csv": Canada_Weather_Monthly, 
    "Canadian_Climate_Data_Yearly_1990-2019(Cleaned).csv": Canada_Weather_Yearly
}

for filename, df in output_files.items():
    df.to_csv(filename, index=False)