package com.example.gateway.inbound;

public class SystemInfoDTO {
    private double cpuUsage;
    private long totalMemory;
    private long freeMemory;
    private double percentOfCpuUsed;
    private double percentOfRamUsed;
    private String currentTime;

    public SystemInfoDTO(double cpuUsage, long totalMemory, long freeMemory, double percentOfCpuUsed,
            double percentOfRamUsed, String currentTime) {
        this.cpuUsage = cpuUsage;
        this.totalMemory = totalMemory;
        this.freeMemory = freeMemory;
        this.percentOfCpuUsed = percentOfCpuUsed;
        this.percentOfRamUsed = percentOfRamUsed;
        this.currentTime = currentTime;
    }

    public double getCpuUsage() {
        return cpuUsage;
    }

    public void setCpuUsage(double cpuUsage) {
        this.cpuUsage = cpuUsage;
    }

    public long getTotalMemory() {
        return totalMemory;
    }

    public void setTotalMemory(long totalMemory) {
        this.totalMemory = totalMemory;
    }

    public long getFreeMemory() {
        return freeMemory;
    }

    public void setFreeMemory(long freeMemory) {
        this.freeMemory = freeMemory;
    }

    public double getPercentOfCpuUsed() {
        return percentOfCpuUsed;
    }

    public void setPercentOfCpuUsed(double percentOfCpuUsed) {
        this.percentOfCpuUsed = percentOfCpuUsed;
    }

    public double getPercentOfRamUsed() {
        return percentOfRamUsed;
    }

    public void setPercentOfRamUsed(double percentOfRamUsed) {
        this.percentOfRamUsed = percentOfRamUsed;
    }

    public String getCurrentTime() {
        return currentTime;
    }

    public void setCurrentTime(String currentTime) {
        this.currentTime = currentTime;
    }
}
