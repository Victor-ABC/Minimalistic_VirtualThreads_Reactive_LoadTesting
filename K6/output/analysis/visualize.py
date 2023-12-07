import pandas as pd
import matplotlib.pyplot as plt
import os as os

def read_and_visualize_csv(csv_file_path):
    # Read CSV file into a DataFrame
    df = pd.read_csv(csv_file_path, index_col=0)

    # Extract relevant columns for visualization
    columns_to_visualize = ['avg_duration', 'error_rate', 'avg_cpuUsage', 'avg_percentOfRamUsed']

    # Plot bar chart
    fig, ax1 = plt.subplots()

    # Plot avg_duration on the left axis
    color = 'tab:blue'
    ax1.set_xlabel('Virtual Users')
    ax1.set_ylabel('Average Duration (ms)', color=color)
    ax1.bar(df.index, df['avg_duration'], color=color)
    ax1.tick_params(axis='y', labelcolor=color)

    # Create a second y-axis for error_rate and avg_percentOfRamUsed
    ax2 = ax1.twinx()
    
    # Plot error_rate on the right axis
    color = 'tab:red'
    ax2.set_ylabel('Error Rate (%)', color=color)
    ax2.plot(df.index, df['error_rate'] * 100, color=color, linestyle='dashed', marker='o')
    ax2.tick_params(axis='y', labelcolor=color)

    # Plot avg_percentOfRamUsed on the right axis
    color = 'tab:green'
    ax2.set_ylabel('Average RAM Usage (%)', color=color)
    ax2.plot(df.index, df['avg_percentOfRamUsed'], color=color, linestyle='dashed', marker='o')
    ax2.tick_params(axis='y', labelcolor=color)

    # Set labels and title
    plt.title('Performance Metrics for Different Virtual Users')

    # Show the chart
    plt.show()

if __name__ == "__main__":
    # Provide the path to the stored CSV file
    stored_csv_file_path = os.path.abspath('./final_metrics.csv')

    # Call the function to read and visualize the CSV file
    read_and_visualize_csv(stored_csv_file_path)
