import pygame
import serial
from time import sleep

pygame.init()
port = serial.Serial("/dev/ttyACM0", baudrate=9600, timeout=3.0)
while True:
    dist = int(port.readline().decode('utf-8')[:-1:])
    print(dist)
    if dist < 10:
        playSound()
        while int(port.readline().decode('utf-8')) < 10:
            pass

