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

        long maxMemory = runtime.maxMemory();
        double freeRamPercentage = ((double) runtime.freeMemory() / maxMemory) * 100;

        double cpuUsagePercentage = operatingSystemMXBean.getCpuLoad() * 100;

        long freeHeapMemory =
                memoryMXBean.getHeapMemoryUsage().getMax() - memoryMXBean.getHeapMemoryUsage().getUsed();
        double freeHeapPercentage =
                ((double) freeHeapMemory / memoryMXBean.getHeapMemoryUsage().getMax()) * 100;

        // Convert memory values to megabytes
        maxMemory /= (1024 * 1024);
        freeHeapMemory /= (1024 * 1024);

        long usedHeapMemory = memoryMXBean.getHeapMemoryUsage().getUsed();
        double usedHeapPercentage =
                ((double) usedHeapMemory / memoryMXBean.getHeapMemoryUsage().getMax()) * 100;

        return new SystemInfo(freeRamPercentage, maxMemory, freeHeapMemory, usedHeapMemory / (1024 * 1024),
                cpuUsagePercentage,
                freeHeapPercentage, usedHeapPercentage);
    }


    public static class SystemInfo {

        private final double freeRamPercentage;
        private final long maxMemory;
        private final long freeHeapMemory;
        private final long usedHeapMemory;
        private final double cpuUsagePercentage;
        private final double freeHeapPercentage;
        private final double usedHeapPercentage;

        public SystemInfo(double freeRamPercentage, long maxMemory, long freeHeapMemory,
                long usedHeapMemory,
                double cpuUsagePercentage, double freeHeapPercentage, double usedHeapPercentage) {
            this.freeRamPercentage = freeRamPercentage;
            this.maxMemory = maxMemory;
            this.cpuUsagePercentage = cpuUsagePercentage;
            this.freeHeapPercentage = freeHeapPercentage;
            this.freeHeapMemory = freeHeapMemory;
            this.usedHeapMemory = usedHeapMemory;
            this.usedHeapPercentage = usedHeapPercentage;
        }

        public double getFreeRamPercentage() {
            return freeRamPercentage;
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

        public long getFreeHeapMemory() {
            return freeHeapMemory;
        }

        public long getUsedHeapMemory() {
            return usedHeapMemory;
        }

        public double getUsedHeapPercentage() {
            return usedHeapPercentage;
        }
    }
}
