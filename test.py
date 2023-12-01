from machine import Pin
import utime

# Ustawienia pinu dla diody LED
yellow_led_pin = 0
yellow_led = Pin(yellow_led_pin, Pin.OUT)

# Włącz diodę na kilka sekund
yellow_led.on()
utime.sleep(5)  # 5 sekund
yellow_led.off()