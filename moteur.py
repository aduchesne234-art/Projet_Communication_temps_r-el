from machine import Pin, PWM
import time

class moteur:
    def __init__(self, pin_ena, pin_in1, pin_in2):
        self.in1 = Pin(pin_in1, Pin.OUT, value=0)
        self.in2 = Pin(pin_in2, Pin.OUT, value=0)
        self.ena = PWM(Pin(pin_ena), freq=1000)

    def open_door(self, vitesse=100):
        self.ena.duty_u16(int((vitesse * 65535) / 100))
        self.in2.value(0)
        self.in1.value(1)
        time.sleep_ms(3000)
        self.in1.value(0)

    def close_door(self, vitesse=100):
        self.ena.duty_u16(int((vitesse * 65535) / 100))
        self.in1.value(0)
        self.in2.value(1)
        time.sleep_ms(3000)
        self.in2.value(0)

    def stop(self):
        self.in1.value(0)
        self.in2.value(0)
        self.ena.duty_u16(0)