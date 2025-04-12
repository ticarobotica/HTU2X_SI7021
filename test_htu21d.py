from machine import Pin, I2C
from time import sleep
import HTU21D


i2c=I2C(0, sda=Pin(21), scl=Pin(22), freq=10000)
senzor_htu21=HTU21D.HTU21D(22,21)

while True:
    print("T=", round(senzor_htu21.temperature,2)," ","Humi=",round(senzor_htu21.humidity,2)," ", end="\r")
    sleep(1)
    