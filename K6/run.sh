#!/bin/bash

# Set the path to k6 executable (adjust this path based on your k6 installation)

# Initialize iterations variable
iterations=0

for ((V=1000; V<=10000; V+=1000)); do
    # Increment the iterations counter
    ((iterations++))

    # Update the config.json with the new "iterations" value
    echo "{ \"info\": \"Port: Normal=8080 ; Reactive=8081 ; Virtual=8082\", \"port\": \"8080\", \"vus\": $V, \"iterations\": $iterations }" > config.json

    # Start fetching RAM and CPU
    node monitor.js &

    # Run k6
    k6 run test.js

    # Stop fetching RAM and CPU
    pkill -f node.exe

    # Sleep
    sleep 3
done

# Analysis
cd ./output/analysis/
python3 analysis.py

# Sleep
sleep 3

python3 visualize.py

# Sleep
sleep 100

exit 0
