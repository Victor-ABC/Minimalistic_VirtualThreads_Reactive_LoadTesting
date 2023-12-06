@echo off


rem Loop through VU values from 100 to 10000 with a step of 100
for /L %%v in (100, 100, 1000) do (
    echo Running k6 test with %%v VUs...
    
    rem Set the output file name based on the current VU value
    set OUTPUT_FILE=output_%%v.json

    rem Run the k6 test with the current VU value
    set VUS=%%v
    k6 run --vus %VUS% --duration 10s --out json=%OUTPUT_FILE% test.js
    
    rem Add a timeout for a short duration to give some time between test runs (optional)
    timeout /t 5 /nobreak >nul
)