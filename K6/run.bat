@echo off
setlocal enabledelayedexpansion

REM Set the path to k6 executable (adjust this path based on your k6 installation)

REM Initialize iterations variable
set iterations=0

for /L %%V in (100, 100, 1000) do (
    REM Increment the iterations counter
    set /a iterations+=1

    REM Update the config.json with the new "iterations" value
    echo { "info": "Port: Normal=8080 ; Reactive=8081 ; Virtual=8082", "port": "8082", "vus": %%V, "iterations": !iterations! } > config.json

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
timeout /t 3

python visualize.py

REM Sleep
timeout /t 100

endlocal
exit /b 0
