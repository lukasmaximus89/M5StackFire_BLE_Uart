from m5stack import *
from m5ui import *
from uiflow import *
from ble import ble_uart
import time
import imu


setScreenColor(0x222222)

uart_ble = ble_uart.init('M5stackula')
imu0 = imu.IMU()

label0 = M5TextBox(21, 27, "Text", lcd.FONT_Default,0xFFFFFF, rotate=0)
label1 = M5TextBox(21, 40, "Text", lcd.FONT_Default,0xFFFFFF, rotate=0)

text = None

def buttonA_wasPressed():
  global text
  data = str(imu0.acceleration)
  #uart_ble.write('on')
  uart_ble.write(data)
  pass
btnA.wasPressed(buttonA_wasPressed)


while True:
    text = (uart_ble.read()).decode()
    label0.setText(str(text))
    label1.setText(str(uart_ble.read()))
    if text == 'on':
        rgb.setColorAll(0xff0000)
        speaker.tone(1800, 200)
        lcd.print('received', 0, 80, 0xffffff)
    if buttonA_wasPressed():
        uart_ble.write(b'0x6c')




