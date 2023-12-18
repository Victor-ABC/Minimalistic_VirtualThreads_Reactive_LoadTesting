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
    request_count = data['metrics']['http_reqs']['values']['count']

    # Create a DataFrame
    df = pd.DataFrame({
        'avg_duration': [avg_duration],
        'avg_waiting': [avg_waiting],
        'error_rate': [error_rate],
        'request_count': [request_count]
    })

    return df

def read_csv(file_path):
    # Read CSV into a DataFrame
    df_csv = pd.read_csv(file_path, header=None, names=['timestamp', 'maxMemory', 'freeHeapMemory', 'usedHeapMemory', 'cpuUsagePercentage', 'freeHeapPercentage', 'usedHeapPercentage'])

    # Calculate the average for relevant columns
    print(df_csv['maxMemory'].mean())
    avg_maxHeap = df_csv['maxMemory'].mean()
    avg_freeHeapMomory = df_csv['freeHeapMemory'].mean() 
    avg_usedHeapMemory = df_csv['usedHeapMemory'].mean() 

    # Create a DataFrame with average values
    df_avg = pd.DataFrame({
        'avg_maxHeap': [avg_maxHeap],
        'avg_freeHeapMomory': [avg_freeHeapMomory],
        'avg_usedHeapMemory' : [avg_usedHeapMemory]
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
    start_vus = end_vus - ((config_data['iterations'] - 1) * 100) #todo: 10 bzw. 100 sind die Schrittweite der VUS!!!

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
