@echo off

REM Start the Node.js script before entering the loop
start node monitor.js

REM Set the path to k6 executable (adjust this path based on your k6 installation)

for /L %%V in (100, 100, 100) do (
    REM Update the config.json file with the current vus value
    echo { "info": "Port: Normal=8080 ; Reactive=8081 ; Virtual=8082", "port": "8080", "vus": %%V } > config.json

    REM Run the k6 test with the updated config.json file
    k6 run test.js 

    REM Sleep for a short duration between tests (adjust as needed)
    timeout /t 3
)

REM Stop the Node.js script after leaving the loop
taskkill /F /IM node.exe

exit /b 0