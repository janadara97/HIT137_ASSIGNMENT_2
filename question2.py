import os
import pandas as pd

# folder where temperature CSV files are stored
temperatures_folder = "temperature_data"

# Function to calculate seasonal averages
def calculate_seasonal_averages(data):
    # Define the seasons and their corresponding months
    seasons = {
        "Summer": ["December", "January", "February"],
        "Autumn": ["March", "April", "May"],
        "Winter": ["June", "July", "August"],
        "Spring": ["September", "October", "November"],
    }

    # Create a dictionary to store seasonal averages for each station
    seasonal_averages = {}

    for season, months in seasons.items():
        seasonal_averages[season] = data[months].mean(axis=1)

    return pd.DataFrame(seasonal_averages, index=data.index)

# Main function to process temperature data
def process_temperature_data():
    all_data = []  # List to store data from all files

    # Read each CSV file in the folder
    for file_name in os.listdir(temperatures_folder):
        if file_name.endswith(".csv"):
            file_path = os.path.join(temperatures_folder, file_name)
            print(f"Processing file: {file_name}")  # Debug message
            data = pd.read_csv(file_path)
            all_data.append(data)

    # Combine all data into a single DataFrame
    combined_data = pd.concat(all_data, ignore_index=True)
    combined_data.set_index("STATION_NAME", inplace=True)

    # Task 1: Calculate average temperatures for each season
    seasonal_averages = calculate_seasonal_averages(combined_data)
    overall_seasonal_avg = seasonal_averages.mean(axis=0)

    # Save the seasonal averages to a text file
    with open("average_temp.txt", "w") as file:
        file.write("Seasonal Average Temperatures Across All Years:\n")
        file.write(overall_seasonal_avg.to_string())
        file.write("\n\nDetailed Averages by Station:\n")
        file.write(seasonal_averages.to_string())

    # Task 2: Find the station with the largest temperature range
    monthly_temps = combined_data.loc[:, "January":"December"]
    temp_ranges = monthly_temps.max(axis=1) - monthly_temps.min(axis=1)
    max_temp_range = temp_ranges.max()
    stations_with_max_range = temp_ranges[temp_ranges == max_temp_range].index.tolist()

    # Save the largest temperature range station(s) to a text file
    with open("largest_temp_range_station.txt", "w") as file:
        file.write("Station(s) with the Largest Temperature Range:\n")
        for station in stations_with_max_range:
            file.write(f"{station}: {max_temp_range:.2f}\n")

    # Task 3: Find the warmest and coolest stations
    avg_monthly_temps = monthly_temps.mean(axis=1)
    warmest_temp = avg_monthly_temps.max()
    coolest_temp = avg_monthly_temps.min()

    warmest_stations = avg_monthly_temps[avg_monthly_temps == warmest_temp].index.tolist()
    coolest_stations = avg_monthly_temps[avg_monthly_temps == coolest_temp].index.tolist()

    # Save the warmest and coolest stations to a text file
    with open("warmest_and_coolest_station.txt", "w") as file:
        file.write("Warmest Station(s):\n")
        for station in warmest_stations:
            file.write(f"{station}: {warmest_temp:.2f}\n")

        file.write("\nCoolest Station(s):\n")
        for station in coolest_stations:
            file.write(f"{station}: {coolest_temp:.2f}\n")

# Entry point for the script
if __name__ == "__main__":
    print("Starting temperature data analysis...")
    process_temperature_data()
    print("Analysis complete. Results saved to text files.")
