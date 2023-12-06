@echo off


REM Set the path to k6 executable (adjust this path based on your k6 installation)

for /L %%V in (100, 100, 200) do (

    REM Update the config.json
    echo { "info": "Port: Normal=8080 ; Reactive=8081 ; Virtual=8082", "port": "8080", "vus": %%V } > config.json

    REM Start fetching RAM and CPU
    start node monitor.js

    REM Run k6
    k6 run test.js 

    REM Stop fetching RAM and CPU
    taskkill /F /IM node.exe

    REM Sleep
    timeout /t 3
)

REM Analysis
cd .\output\analysis\
python analysis.py

REM Sleep
timeout /t 1000

exit /b 0