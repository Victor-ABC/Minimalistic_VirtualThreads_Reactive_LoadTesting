import http from 'k6/http';
import { sleep } from 'k6';

export const options = {
    stages: [
        { duration: '5s', target: 0 },   // Warm-up phase with 0 VUs
        { duration: '10s', target: 5000 }, // Linear increase to 100 VUs
        { duration: '10s', target: 5000 }, // Hold at 100 VUs for 10 seconds
        { duration: '10s', target: 0 },   // Ramp down to 0 VUs
    ],
};


export default function () {
    const url = 'http://localhost:8081/D';

    // Record the start time of the request
    const startTime = new Date().getTime();

    // Send an HTTP GET request to the specified URL
    const response = http.get(url);

    // Record the end time of the request
    const endTime = new Date().getTime();

    // Calculate the response time
    const responseTime = endTime - startTime;

    // Log the response time
    console.log(`Response time: ${responseTime} ms`);

    // Introduce a sleep to simulate user think time
    sleep(1);
}