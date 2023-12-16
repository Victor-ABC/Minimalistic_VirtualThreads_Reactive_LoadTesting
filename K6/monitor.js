const http = require('http');
const fs = require('fs');
const csv = require('csv-parser');

const config = require('./config.json');
const port = config.port;
const apiUrl = `http://localhost:${port}/custom-metrics/system-info`;

// Read vus value from config.json
const vus = config.vus;

// Construct the CSV file path with vus as a suffix
const csvFilePath = `./output/ressources/metric_output_${vus}.csv`;

function sendMonitorRequest() {
  http.get(apiUrl, (response) => {
    let data = '';

    // A chunk of data has been received.
    response.on('data', (chunk) => {
      data += chunk;
    });

    // The whole response has been received.
    response.on('end', () => {
      try {
        const jsonData = JSON.parse(data);
        saveToCsv(jsonData);
      } catch (error) {
        console.error('Error parsing JSON:', error.message);
      }
    });
  }).on('error', (error) => {
    console.error('Error making request:', error.message);
  });
}

function saveToCsv(data) {
  const timestamp = new Date().toISOString();
  const csvRow = `${timestamp},${data.maxMemory},${data.freeHeapMemory},${data.usedHeapMemory},${data.cpuUsagePercentage},${data.freeHeapPercentage},${data.usedHeapPercentage}\n`;

  fs.appendFile(csvFilePath, csvRow, (err) => {
    if (err) {
      console.error('Error writing to CSV:', err.message);
    } else {
      console.log('Data saved to CSV successfully.');
    }
  });
}

// Start monitoring after waiting for 25 seconds.
setTimeout(function() {
  // Start monitoring every second.
  var monitorInterval = setInterval(sendMonitorRequest, 1000);

  // Stop the interval after 20 seconds.
  setTimeout(function() {
    clearInterval(monitorInterval);
  }, 20000);

}, 25000);
