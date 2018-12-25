# coding=utf-8
from matplotlib import pyplot as plt
import time


def readData(file_path):
    date_file = open(file_path, 'r')
    linux_times = []
    times = []
    temps = []
    hus = []
    lines = date_file.readlines()
    for item in lines:
        str_item = item.strip("\n")
        str_time = str_item.split(",")[0]
        temp = str_item.split(",")[1]
        hu = str_item.split(",")[2]

        if float(hu) > 100:
            continue

        times.append(time)
        lt = time.strptime(str_time, "%Y-%m-%d %H:%M:%S")
        timeStamp = int(time.mktime(lt))
        linux_times.append(timeStamp)
        temps.append(float(temp))
        hus.append(float(hu))
    return linux_times, times, temps, hus


def drawPlot(times, temps, hus):
    plt.figure(1)
    plt.title("temperature of one day")
    plt.plot(times, temps, color='orange')
    max_temp = max(temps)
    min_temp = min(temps)
    plt.axhline(max_temp, color='red')
    plt.axhline(min_temp, color='blue')
    plt.figure(2)
    plt.title("humidity of one day")
    max_hu = max(hus)
    min_hu = min(hus)
    plt.axhline(max_hu, color='red')
    plt.axhline(min_hu, color='blue')
    plt.plot(times, hus)
    plt.show()


if __name__ == '__main__':
    linux_times, times, temps, hus = readData("records.txt")
    drawPlot(linux_times, temps, hus)
