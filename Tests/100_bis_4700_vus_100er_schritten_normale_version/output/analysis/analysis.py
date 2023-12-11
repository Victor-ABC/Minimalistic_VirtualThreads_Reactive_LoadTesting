import os
import json
import pandas as pd

def read_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        
    # Extract relevant values from the JSON
    avg_duration = data['metrics']['http_req_duration']['values']['avg']
    avg_waiting = data['metrics']['http_req_waiting']['values']['avg']
    error_rate = data['metrics']['http_req_failed']['values']['rate']

    # Create a DataFrame
    df = pd.DataFrame({
        'avg_duration': [avg_duration],
        'avg_waiting': [avg_waiting],
        'error_rate': [error_rate]
    })

    return df

def read_csv(file_path):
    # Read CSV into a DataFrame
    df_csv = pd.read_csv(file_path, header=None, names=['timestamp', 'cpuUsage', 'totalMemory', 'freeMemory', 'percentOfCpuUsed', 'percentOfRamUsed', 'currentTime'])

    # Calculate the average for relevant columns
    avg_cpuUsage = df_csv['cpuUsage'].mean()
    avg_totalMemory = df_csv['totalMemory'].mean()
    avg_freeMemory = df_csv['freeMemory'].mean()
    avg_percentOfCpuUsed = df_csv['percentOfCpuUsed'].mean()
    avg_percentOfRamUsed = df_csv['percentOfRamUsed'].mean() / 100

    # Create a DataFrame with average values
    df_avg = pd.DataFrame({
        'avg_cpuUsage': [avg_cpuUsage],
        'avg_totalMemory': [avg_totalMemory],
        'avg_freeMemory': [avg_freeMemory],
        'avg_percentOfCpuUsed': [avg_percentOfCpuUsed],
        'avg_percentOfRamUsed': [avg_percentOfRamUsed]
    })

    return df_avg

def main():
    # Provide the path to the config.json file
    config_file_path = os.path.abspath('../../config.json')

    # Read values from config.json
    with open(config_file_path, 'r') as config_file:
        config_data = json.load(config_file)

    # Extract values from config.json
    end_vus = config_data['vus']
    start_vus = end_vus - ((config_data['iterations'] - 1) * 100)

    # Create an empty DataFrame to store the results
    final_df = pd.DataFrame()

    for vus in range(start_vus, end_vus + 1, 100):
        # Construct the paths based on the loop variable
        json_file_path = os.path.abspath(f'./../k6/summary_{vus}.json')
        csv_file_path = os.path.abspath(f'./../ressources/metric_output_{vus}.csv')

        # Read JSON and create DataFrame
        df_json = read_json(json_file_path)

        # Read CSV, calculate average, and create DataFrame
        df_avg = read_csv(csv_file_path)

        # Merge DataFrames on a common column (e.g., timestamp)
        merged_df = pd.merge(df_json, df_avg, left_index=True, right_index=True)

        # Set the index
        merged_df.index = [str(vus)]

        # Add the row to the final DataFrame
        final_df = pd.concat([final_df, merged_df])

    # Save the final DataFrame to a CSV file in the current folder
    output_csv_path = os.path.abspath('./final_metrics.csv')
    final_df.to_csv(output_csv_path, index=True, header=True)

    # Display the final DataFrame
    print(final_df)

    # Display the final DataFrame
    print(final_df)

if __name__ == "__main__":
    main()
