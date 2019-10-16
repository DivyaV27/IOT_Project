import time
import grovepi
import os

gas_sensor=0
grovepi.pinMode(gas_sensor,"INPUT")
print("s")
while True:
    try:
        sensor_value=grovepi.analogRead(gas_sensor)
        print("sensor value = ",sensor_value)
	sens="./shell.sh "+str(sensor_value)
	os.system(sens)
        time.sleep(1.0)
    except IOError:
        print("Error")
