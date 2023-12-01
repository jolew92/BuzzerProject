from machine import Pin, PWM
import utime

# Ustawienia pinów dla buzzer'a
buzzer_pin = 26
buzzer_pwm = PWM(Pin(buzzer_pin))

# Ustawienia pinów dla diod LED
red_led_pin = 6
yellow_led_pin = 0  # Zmieniono pin na 0
green_led_pin = 11

red_led = Pin(red_led_pin, Pin.OUT)
yellow_led = Pin(yellow_led_pin, Pin.OUT)
green_led = Pin(green_led_pin, Pin.OUT)

# Ustawienia pinów dla przycisków
play_button_pin = 21
pause_button_pin = 28
stop_button_pin = 27

play_button = Pin(play_button_pin, Pin.IN, Pin.PULL_UP)
pause_button = Pin(pause_button_pin, Pin.IN, Pin.PULL_UP)
stop_button = Pin(stop_button_pin, Pin.IN, Pin.PULL_UP)

# Melodia "Jingle Bells"
melody = [
    (659, 200), (659, 200), (659, 400), (659, 200), (659, 200), (659, 400),
    (659, 200), (784, 200), (523, 400), (587, 200), (659, 200), (784, 400),
    (659, 200), (523, 200), (587, 400), (587, 200), (587, 200), (587, 200),
    (587, 200), (659, 200), (784, 200), (523, 400), (587, 200), (659, 200),
    (784, 400), (659, 200), (523, 200), (587, 400), (523, 200), (523, 200), (523, 400),
]

def play_melody():
    for note in melody:
        buzzer_pwm.freq(note[0])
        buzzer_pwm.duty_u16(500)
        utime.sleep_ms(note[1])
        buzzer_pwm.duty_u16(0)
        utime.sleep_ms(20)

def main():
    playing = False

    while True:
        if play_button.value() == 0 and not playing:
            play_melody()
            playing = True
        elif pause_button.value() == 0 and playing:
            # Pauza
            buzzer_pwm.duty_u16(0)
            playing = False
            while pause_button.value() == 0:  # Poczekaj na zwolnienie przycisku pauzy
                utime.sleep_ms(50)
        elif stop_button.value() == 0:
            # Zatrzymaj i zacznij od nowa
            buzzer_pwm.duty_u16(0)
            playing = False
            while stop_button.value() == 0:  # Poczekaj na zwolnienie przycisku stopu
                utime.sleep_ms(50)
            utime.sleep_ms(500)  # Oczekiwanie na zakończenie poprzedniej melodii

        # Obsługa diod LED
        if playing:
            green_led.off()
            yellow_led.off()
            red_led.on()
            utime.sleep_ms(100)  # Krótkie opóźnienie, aby diody migały były bardziej widoczne
            green_led.on()
            yellow_led.off()
            red_led.off()
            utime.sleep_ms(100)
        elif not playing and buzzer_pwm.duty_u16() > 0:
            green_led.off()
            yellow_led.on()
            red_led.off()
            utime.sleep_ms(100)  # Krótkie opóźnienie, aby dioda żółta była bardziej widoczna
        else:
            green_led.off()
            yellow_led.off()
            red_led.on()

if __name__ == "__main__":
    main()
