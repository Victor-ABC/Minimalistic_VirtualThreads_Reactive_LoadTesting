import http from 'k6/http';
import { sleep } from 'k6';

const configFile = 'config.json';
const configData = JSON.parse(open(configFile));
const port = parseInt(configData.port); // Use the "port" value from the JSON
const vus = parseInt(configData.vus); // Use the "vus" value from the JSON

const csvFile = 'results.csv';

export const options = {
    stages: [
        { duration: '2s', target: 0 },
        { duration: '2s', target: vus }, // Use the "vus" value here
        { duration: '2s', target: vus }, // Use the "vus" value here
        { duration: '2s', target: 0 },
    ],
};

export default function () {

    const startTime = new Date().getTime();
    const response = http.get(`http://localhost:${port}/minimalistic`);
    const endTime = new Date().getTime();
    const responseTime = endTime - startTime;

    // Log the response time
    console.log(`[localhost:${port}] Response time: ${responseTime} ms`);



    // Introduce a sleep to simulate user think time
    sleep(1);
}

export function handleSummary(data) {
    // Return the default data object
    const my_string = "C:\\Users\\User\\fep\\minimalistic_gateway\\K6\\output/k6/summary_" + vus + ".json";
    const result = {};
    result[my_string] = JSON.stringify(data);
    return result;
}