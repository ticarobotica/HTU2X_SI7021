from machine import Pin, SoftI2C
from time import sleep
import si7021

i2c=SoftI2C(sda=Pin(21), scl=Pin(22), freq=100000)
senzor_si=si7021.SI7021(i2c)

while True:
    print("Temp =", round(senzor_si.temperature(),2), " ","Humi = ", round(senzor_si.humidity(),2), " ", end="\r")
    sleep(1)
    