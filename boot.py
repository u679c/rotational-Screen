# This file is executed on every boot (including wake-boot from deepsleep)
# import esp
# esp.osdebug(None)
# import webrepl
# webrepl.start()

from machine import Pin, PWM
import time
import network
import socket


wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect("u679c_wifi", "419123liu")


led2 = Pin(2, Pin.OUT)
key = Pin(4, Pin.IN, Pin.PULL_UP)

if wlan.isconnected():
    print("连接成功")
else:
    while not wlan.isconnected():
        time.sleep_ms(300)
        led2.value(1)
        time.sleep_ms(300)
        led2.value(0)
led2.value(1)
key_done = False
while True:
    if key.value() == 0 and not key_done:
        udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        dest_addr = ("192.168.101.2", 5555)
        send_data = "旋转屏幕"
        udp_socket.sendto(send_data.encode('utf-8'), dest_addr)
        udp_socket.close()
        key_done = True
    else:
        key_done = False
    time.sleep_ms(100)
