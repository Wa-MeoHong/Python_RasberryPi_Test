# Class DHT11

import RPi.GPIO as GPIO
import time as t

DHT11_PIN = 36                  # BOARD 기준 36번 핀

class DHT11:
    def  __init__(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(DHT11_PIN, GPIO.OUT)

    def read(self):
        GPIO.setup(DHT11_PIN, GPIO.OUT)
        GPIO.output(DHT11_PIN, GPIO.HIGH)
        t.sleep(1)
        GPIO.output(DHT11_PIN, GPIO.LOW)
        t.sleep(0.02)
        GPIO.output(DHT11_PIN, GPIO.HIGH)
        count = 0
        while count < 35:
            count += 1
        GPIO.setup(DHT11_PIN, GPIO.IN)
        while GPIO.input(DHT11_PIN) == GPIO.LOW:
            break
        while GPIO.input(DHT11_PIN) == GPIO.HIGH:
            break
        while GPIO.input(DHT11_PIN) == GPIO.LOW:
            break
        
        DATA = [0, 0, 0, 0, 0]
        count = 0

        while count <= 40:
            i = 0
            while GPIO.input(DHT11_PIN) == GPIO.LOW:
                i += 1
            while GPIO.input(DHT11_PIN) == GPIO.HIGH:
                i += 1
            if (count > 0):
                DATA[int((count - 1) / 8)] <<= 1
                if i > 37:
                    DATA[int((count - 1) / 8)] |= 1
            count += 1
        
        if ((DATA[0] + DATA[1] + DATA[2] + DATA[3] % 256 == DATA[4])):
            return DATA
        else:
            print("checksum ERROR")
            return None

def main():
    dht11 = DHT11()
    while True:
        data  = dht11.read()
        if (data != None):
            hum = "{}.{}%".format (data[0], data[1])
            temp = "{}.{} deg".format (data[2], data[3])
            print("hum = {}, temp = {}".format(hum, temp))
            t.sleep(1)
        t.sleep(0.1)

if __name__ == "__main__":
    main()
    