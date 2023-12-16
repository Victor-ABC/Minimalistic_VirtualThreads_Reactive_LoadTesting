import pandas as pd
import matplotlib.pyplot as plt
import os

def read_and_visualize_csv(csv_file_path):
    # Read CSV file into a DataFrame
    df = pd.read_csv(csv_file_path, index_col=0)

    # Set up the figure and axes
    fig, ax1 = plt.subplots(figsize=(12, 8))  # Adjust the figure size as needed

    # Set the width of the bars (increase the width for wider bars)
    bar_width = 100  # Adjust the width of the bars for all columns

    # Plot bars for avg_duration and request_count on the left axis with a wider bar
    color_duration = 'tab:blue'
    color_count = 'tab:gray'
    ax1.bar(df.index - bar_width/2, df['avg_duration'], width=bar_width, color=color_duration, label='avg_duration')
    ax1.bar(df.index + bar_width/2, df['request_count'], width=bar_width, color=color_count, alpha=0.5, label='request_count')
    ax1.set_xlabel('Virtual Users')
    ax1.set_ylabel('Average Duration (ms) / Request Count', color=color_duration)
    ax1.tick_params(axis='y', labelcolor=color_duration)

    # Create a second y-axis for other metrics
    ax2 = ax1.twinx()

    # Plot error_rate on the right axis
    color_error_rate = 'tab:red'
    ax2.plot(df.index, df['error_rate'] * 100, color=color_error_rate, linestyle='dashed', marker='o', label='error_rate')
    ax2.tick_params(axis='y', labelcolor=color_error_rate)

    # Plot avg_percentOfCpuUsed on the right axis
    color_cpu_used = 'tab:orange'
    ax2.plot(df.index, df['avg_percentOfCpuUsed'], color=color_cpu_used, linestyle='dashed', marker='o', label='CPU_Used')
    ax2.tick_params(axis='y', labelcolor=color_cpu_used)

    # Plot avg_percentOfFreeHeap on the right axis
    color_free_heap = 'tab:purple'
    ax2.plot(df.index, df['avg_percentOfFreeHeap'], color=color_free_heap, linestyle='dashed', marker='o', label='Free_Heap (JVM)')
    ax2.tick_params(axis='y', labelcolor=color_free_heap)

    # Plot avg_percentOfRamUsed on the right axis
    color_ram_used = 'tab:green'
    ax2.set_ylabel('Percentage', color=color_ram_used)
    ax2.plot(df.index, df['avg_percentOfRamUsed'], color=color_ram_used, linestyle='dashed', marker='o', label='Free_RAM (JVM)')
    ax2.tick_params(axis='y', labelcolor=color_ram_used)

    # Set labels and title
    plt.title('Performance Metrics for Different Virtual Users')

    # Move the legend above the chart
    ax1.legend(loc='upper left', bbox_to_anchor=(0, 1.1))  # Adjust the y-coordinate as needed
    ax2.legend(loc='upper left', bbox_to_anchor=(0.8, 1.16))  # Adjust the y-coordinate as needed

    # Show the chart
    plt.show()

if __name__ == "__main__":
    # Provide the path to the stored CSV file
    stored_csv_file_path = os.path.abspath('./final_metrics.csv')

    # Call the function to read and visualize the CSV file
    read_and_visualize_csv(stored_csv_file_path)
