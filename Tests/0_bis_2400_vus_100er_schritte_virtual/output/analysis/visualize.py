import pandas as pd
import matplotlib.pyplot as plt
import os as os

def read_and_visualize_csv(csv_file_path):
    # Read CSV file into a DataFrame
    df = pd.read_csv(csv_file_path, index_col=0)

    # Extract relevant columns for visualization
    columns_to_visualize = ['avg_duration', 'error_rate', 'avg_cpuUsage', 'avg_percentOfRamUsed']

    # Set up the figure and axes
    fig, ax1 = plt.subplots(figsize=(12, 8))  # Adjust the figure size as needed

    # Set the width of the bars
    bar_width = 6  # Adjust the width of the bars for all columns

    # Plot bars for avg_duration on the left axis with a wider bar
    color = 'tab:blue'
    ax1.bar(df.index, df['avg_duration'], width=bar_width, color=color, label='avg_duration')
    ax1.set_xlabel('Virtual Users')
    ax1.set_ylabel('Average Duration (ms)', color=color)
    ax1.tick_params(axis='y', labelcolor=color)

    # Create a second y-axis for error_rate, avg_percentOfCpuUsed, and avg_percentOfRamUsed
    ax2 = ax1.twinx()

    # Plot error_rate on the right axis
    color = 'tab:red'
    ax2.plot(df.index, df['error_rate'] * 100, color=color, linestyle='dashed', marker='o', label='error_rate')
    ax2.tick_params(axis='y', labelcolor=color)

    # Plot avg_percentOfCpuUsed on the right axis
    color = 'tab:orange'
    ax2.plot(df.index, df['avg_percentOfCpuUsed'] * 100, color=color, linestyle='dashed', marker='o', label='avg_percentOfCpuUsed')
    ax2.tick_params(axis='y', labelcolor=color)

    # Plot avg_percentOfRamUsed on the right axis
    color = 'tab:green'
    ax2.set_ylabel('Prozent', color=color)
    ax2.plot(df.index, df['avg_percentOfRamUsed'] * 100, color=color, linestyle='dashed', marker='o', label='avg_percentOfRamUsed')
    ax2.tick_params(axis='y', labelcolor=color)

    # Set labels and title
    plt.title('Performance Metrics for Different Virtual Users')

    # Move the legend outside the chart
    ax1.legend(loc='upper left', bbox_to_anchor=(1, 1))
    ax2.legend(loc='upper left', bbox_to_anchor=(1, 0.9))

    # Show the chart
    plt.show()

if __name__ == "__main__":
    # Provide the path to the stored CSV file
    stored_csv_file_path = os.path.abspath('./final_metrics.csv')

    # Call the function to read and visualize the CSV file
    read_and_visualize_csv(stored_csv_file_path)
