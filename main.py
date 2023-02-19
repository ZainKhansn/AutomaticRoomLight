import utime
from servo import Servo
from machine import Pin
flags = "On"
led = Pin(11, Pin.OUT)

s1 = Servo(13)
s2 = Servo(12)# Servo pin is connected to GP0
trigger = Pin(14, Pin.OUT)
echo = Pin(15, Pin.IN)
#Setting up pins for two servos and motion sensor

def servo_Map(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
 
def servo_Angle(angle):
    if angle < 0:
        angle = 0
    if angle > 180:
        angle = 180
    s1.goto(round(servo_Map(angle,0,180,0,1024))) # Convert range value to angle value
    
def servo_Angle2(angle):
    if angle < 0:
        angle = 0
    if angle > 180:
        angle = 180
    s2.goto(round(servo_Map(angle,0,180,0,1024))) # Convert range value to angle value
#DEF servo code

def ultra():
   global flags
   while True:
       trigger.low()
       utime.sleep_us(2)
       trigger.high()
       utime.sleep_us(5)
       trigger.low()
       while echo.value() == 0:
           signaloff = utime.ticks_us()
           
       while echo.value() == 1:
           signalon = utime.ticks_us()
           
       timepassed = signalon - signaloff
       distance = (timepassed * 0.0343) / 2
       print("The distance from object is ",(distance/2.54),"in""\n")
      #Def distance sensor
       if (distance/2.54) <26 and flags == "On":
            led.value(1)

            for i in range(0,180,10):
                #on
                servo_Angle(i)
                utime.sleep(0.02)
                flags = "Off"
            utime.sleep(2)
            continue
      
       if (distance/2.54) <26 and flags == "Off":
            led.value(0)

            for i in range(180,0,-10):
                 #off
                  servo_Angle2(i)
                  utime.sleep(0.02)
                  flags = "On"
        
            utime.sleep(2)
            continue
       utime.sleep(.1)
#If distance of door(my door is 26 in wide) is less then turn light off else on
  
if __name__ == '__main__':
    
        ultra()
        
