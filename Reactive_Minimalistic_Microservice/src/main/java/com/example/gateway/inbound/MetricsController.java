package com.example.gateway.inbound;

import com.sun.management.OperatingSystemMXBean;
import java.lang.management.ManagementFactory;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import reactor.core.publisher.Mono;

@RestController
@RequestMapping("/custom-metrics")
public class MetricsController {

    @GetMapping("/system-info")
    public Mono<SystemInfoDTO> getSystemInfo() {
        return Mono.fromCallable(() -> {
            OperatingSystemMXBean osBean = (OperatingSystemMXBean) ManagementFactory.getOperatingSystemMXBean();
            double cpuUsage = osBean.getProcessCpuLoad() * 100;

            // Convert total memory and free memory to megabytes
            long totalMemoryInBytes = osBean.getTotalMemorySize();
            long freeMemoryInBytes = osBean.getFreeMemorySize();
            long totalMemoryInMB = totalMemoryInBytes / (1024 * 1024);  // Convert bytes to megabytes
            long freeMemoryInMB = freeMemoryInBytes / (1024 * 1024);    // Convert bytes to megabytes

            double percentOfCpuUsed = (cpuUsage / osBean.getAvailableProcessors());
            double percentOfRamUsed = (1 - ((double) freeMemoryInBytes / totalMemoryInBytes)) * 100;

            LocalDateTime currentTime = LocalDateTime.now();
            String formattedTime = currentTime.format(DateTimeFormatter.ofPattern("HH:mm:ss:SSS"));

            return new SystemInfoDTO(cpuUsage, totalMemoryInMB, freeMemoryInMB, percentOfCpuUsed, percentOfRamUsed, formattedTime);
        });
    }
}
