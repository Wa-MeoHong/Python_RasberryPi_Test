# SG90 servo_motor test
import RPi.GPIO as GPIO
import time

pin = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)

# 초기값 설정
p = GPIO.PWM(pin, 50)       # 50Hz로 시작
p.start(0)                  # duty_cycle은 0으로 설정
left_angle = 12
center_angle = 5
right_angle = 2

# setAngle 함수
def setAngle(angle):        
    p.ChangeDutyCycle(angle)
    time.sleep(0.5)

# 진짜 메인
try: 
    while True:
        var = input("Enter L/C/R : ")
        if var == 'R' or var == 'r':
            setAngle(right_angle)
        elif var == 'C' or var == 'c':
            setAngle(center_angle)
        elif var == 'L' or var == 'l':
            setAngle(left_angle)
        else:
            p.stop()
            break
        print("=================================")

# 예외 처리
except KeyboardInterrupt:
    p.stop()
GPIO.cleanup()