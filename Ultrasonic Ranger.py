# 초음파센서 거리측정

import RPi.GPIO as GPIO
import time
TRIG = 18
ECHO = 16

GPIO.setmode(GPIO.BOARD)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
start, end = 0, 0

def echo_action(channel):                   # 초음파를 쏴서 물체에 맞고 돌아오는 시간을 측정함
    global start, end
    if ((GPIO.input(ECHO)) == GPIO.HIGH):
        start = time.time()
    else:
        end = time.time()

GPIO.add_event_detect(ECHO, GPIO.BOTH, callback = echo_action)  # 함수를 라즈베리파이에 추가함

while True:
    try:
        GPIO.output(TRIG, GPIO.HIGH)
        time.sleep(0.00001)
        GPIO.output(TRIG, GPIO.LOW)
        elapsed = end - start
        if (elapsed < 0.1):                     # 돌아오는데 까지 많은 시간이 걸리면(0.1초 이상) 측정X
            dist = elapsed * 340 * 100 / 2      # 측정한 시간 = 물체에 맞고 돌아오는데 걸린 시간, 음파 = 340m/s
            print ("{:2f}cm".format(dist))      # 출력
        time.sleep(0.1)
    except KeyboardInterrupt:
        GPIO.cleanup()
        break