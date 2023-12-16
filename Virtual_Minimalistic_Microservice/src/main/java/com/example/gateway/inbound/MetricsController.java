package com.example.gateway.inbound;

import com.sun.management.OperatingSystemMXBean;
import java.lang.management.ManagementFactory;
import java.lang.management.MemoryMXBean;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/custom-metrics")
public class MetricsController {

    @GetMapping("/system-info")
    public SystemInfo systemInfo() {
        Runtime runtime = Runtime.getRuntime();
        OperatingSystemMXBean operatingSystemMXBean = (OperatingSystemMXBean) ManagementFactory.getOperatingSystemMXBean();
        MemoryMXBean memoryMXBean = ManagementFactory.getMemoryMXBean();

        long freeMemory = runtime.freeMemory();
        long totalMemory = runtime.totalMemory();
        long maxMemory = runtime.maxMemory();
        double freeRamPercentage = ((double) freeMemory / totalMemory) * 100;

        double cpuUsagePercentage = operatingSystemMXBean.getCpuLoad() * 100;

        long freeHeapMemory = memoryMXBean.getHeapMemoryUsage().getMax() - memoryMXBean.getHeapMemoryUsage().getUsed();
        double freeHeapPercentage = ((double) freeHeapMemory / memoryMXBean.getHeapMemoryUsage().getMax()) * 100;

        return new SystemInfo(freeRamPercentage, freeMemory, totalMemory, maxMemory, cpuUsagePercentage,
                freeHeapPercentage);
    }


    public static class SystemInfo {

        private final double freeRamPercentage;
        private final long freeMemory;
        private final long totalMemory;
        private final long maxMemory;
        private final double cpuUsagePercentage;
        private final double freeHeapPercentage;

        public SystemInfo(double freeRamPercentage, long freeMemory, long totalMemory, long maxMemory,
                double cpuUsagePercentage, double freeHeapPercentage) {
            this.freeRamPercentage = freeRamPercentage;
            this.freeMemory = freeMemory;
            this.totalMemory = totalMemory;
            this.maxMemory = maxMemory;
            this.cpuUsagePercentage = cpuUsagePercentage;
            this.freeHeapPercentage = freeHeapPercentage;
        }

        public double getFreeRamPercentage() {
            return freeRamPercentage;
        }

        public long getFreeMemory() {
            return freeMemory;
        }

        public long getTotalMemory() {
            return totalMemory;
        }

        public long getMaxMemory() {
            return maxMemory;
        }

        public double getCpuUsagePercentage() {
            return cpuUsagePercentage;
        }

        public double getFreeHeapPercentage() {
            return freeHeapPercentage;
        }
    }
}
