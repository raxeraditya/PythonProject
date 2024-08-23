import pandas as pd
import os

# Function to append data to Excel file
def append_data_to_excel(df, file_path, sheet_name='Sheet1'):
    if not os.path.isfile(file_path):
        # If the file does not exist, create it and write the dataframe
        df.to_excel(file_path, index=False, sheet_name=sheet_name)
    else:
        with pd.ExcelWriter(file_path, mode='a', if_sheet_exists='overlay') as writer:
            # Get the last row in the existing Excel sheet
            existing_df = pd.read_excel(file_path, sheet_name=sheet_name)
            startrow = len(existing_df)
            df.to_excel(writer, index=False, header=False, startrow=startrow, sheet_name=sheet_name)

# Function to create the first dataframe and write it
def get_weather_data():
    dataframe1 = {
        "Temperature": ["304.67 K"],
        "Feels Like": ["311.2 K"],
        "Humidity": ["67 %"],
        "Weather": ["light rain"],
        "Wind Speed": ["1.78 m/s"],
        "Pressure": ["1003 hPa"],
        "Visibility": ["10000 m"],
        "Cloudiness": ["100 %"],
        "Rain": ["0.87 mm"],
        "Country": ["IN"]
    }

    df1 = pd.DataFrame(dataframe1)
    append_data_to_excel(df1, 'weather.xlsx')

# Function to create the second dataframe and write it
def new_data():
    dataframe2 = {
        "Temperature": ["306.15 K"],
        "Feels Like": ["312.3 K"],
        "Humidity": ["70 %"],
        "Weather": ["clear sky"],
        "Wind Speed": ["2.00 m/s"],
        "Pressure": ["1005 hPa"],
        "Visibility": ["11000 m"],
        "Cloudiness": ["0 %"],
        "Rain": ["0 mm"],
        "Country": ["IN"]
    }

    df2 = pd.DataFrame(dataframe2)
    append_data_to_excel(df2, 'weather.xlsx')

def main():
    get_weather_data()
    new_data()

if __name__ == "__main__":
    main()
