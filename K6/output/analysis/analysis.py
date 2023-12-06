import os
import json
import pandas as pd

def read_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        
    # Extract relevant values from the JSON
    avg_duration = data['metrics']['http_req_duration{expected_response:true}']['values']['avg']
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
    
    return df_csv

def main():
    # Provide the absolute path to the JSON file
    json_file_path = os.path.abspath('./../k6/summary_100.json')

    # Provide the absolute path to the CSV file
    csv_file_path = os.path.abspath('./../ressources/metric_output.csv')
    
    # Extract index from the filename
    index = json_file_path.split('_')[-1].split('.')[0]

    # Read JSON and create DataFrame
    df_json = read_json(json_file_path)

    # Read CSV and create DataFrame
    df_csv = read_csv(csv_file_path)

    # Merge DataFrames on a common column (e.g., timestamp)
    merged_df = pd.merge(df_json, df_csv, left_index=True, right_index=True)

    # Set the index
    merged_df.index = [index]

    # Display the merged DataFrame
    print(merged_df)

if __name__ == "__main__":
    main()
