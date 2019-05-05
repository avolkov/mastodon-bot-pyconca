# Write your code here :-)
import time
from adafruit_circuitplayground.express import cpx

while True:
    print(cpx.temperature, end='\n')
    time.sleep(5)