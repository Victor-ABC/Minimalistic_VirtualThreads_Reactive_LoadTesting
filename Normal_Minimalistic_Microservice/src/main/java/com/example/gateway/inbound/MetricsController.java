package com.example.gateway.inbound;

import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import java.lang.management.ManagementFactory;
import com.sun.management.OperatingSystemMXBean;

@RestController
@RequestMapping("/custom-metrics")
public class MetricsController {

    @GetMapping("/system-info")
    public SystemInfoDTO getSystemInfo() {
        OperatingSystemMXBean osBean = (OperatingSystemMXBean) ManagementFactory.getOperatingSystemMXBean();
        double cpuUsage = osBean.getProcessCpuLoad() * 100;
        long totalMemory = osBean.getTotalMemorySize();
        long freeMemory = osBean.getFreeMemorySize();

        double percentOfCpuUsed = (cpuUsage / osBean.getAvailableProcessors());
        double percentOfRamUsed = (1 - ((double) freeMemory / totalMemory)) * 100;

        LocalDateTime currentTime = LocalDateTime.now();
        String formattedTime = currentTime.format(DateTimeFormatter.ofPattern("HH:mm:ss:SSS"));

        return new SystemInfoDTO(cpuUsage, totalMemory, freeMemory, percentOfCpuUsed, percentOfRamUsed, formattedTime);
    }
}
