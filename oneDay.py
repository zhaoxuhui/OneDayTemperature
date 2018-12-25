# coding=utf-8
import Adafruit_DHT
import time
import datetime

# 定义sensor型号为DHT22
sensor = Adafruit_DHT.DHT22
# BCM number
pin = 26


def getTemp():
    try:
        hu, temp = Adafruit_DHT.read_retry(sensor, pin)
        return temp, hu
    except:
        print("error\nFailed to read sensor data!")
        return 0, 0


if __name__ == '__main__':
    while True:
        f_out = open("records.txt", 'wa+')
        record_item = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')
        tem, hu = getTemp()
        print(record_item + ' temperature:{0:0.1f}°C humidity:{1:0.1f}%'.format(tem, hu))
        record_item += "," + tem.__str__() + "," + hu.__str__() + "\n"
        f_out.write(record_item)
        f_out.close()
        time.sleep(5)
