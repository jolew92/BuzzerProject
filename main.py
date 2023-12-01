from buzzer_music import music
from time import sleep
from machine import Pin

#https://onlinesequencer.net/3712491 Jingle Bells
song1 = '0 C5 1 41;2 A5 1 41;4 G5 1 41;6 F5 1 41;8 C5 2 41;13 C5 1 41;14 C5 1 41;15 C5 1 41;17 A5 1 41;19 G5 1 41;21 F5 1 41;23 D5 2 41;30 A#5 1 41;32 A5 1 41;28 D5 1 41;34 G5 1 41;36 E5 2 41;41 C6 1 41;43 C6 1 41;47 G5 1 41;49 A5 2 41;45 A#5 1 41;54 C5 1 41;56 A5 1 41;58 G5 1 41;60 F5 1 41;62 C5 2 41;67 C5 1 41;68 C5 1 41;69 C5 1 41;71 A5 1 41;73 G5 1 41;75 F5 1 41;77 D5 2 41;82 D5 1 41;84 A#5 1 41;86 A5 1 41;88 G5 1 41;90 C6 1 41;94 C6 1 41;92 C6 1 41;96 C6 1 41;98 D6 1 41;100 C6 1 41;102 A#5 1 41;104 G5 1 41;106 F5 2 41;110 C6 2 41;114 A5 1 41;116 A5 1 41;118 A5 2 41;122 A5 1 41;124 A5 1 41;126 A5 2 41;129 A5 1 41;131 C6 1 41;133 F5 1 41;135 G5 1 41;137 A5 2 41;141 A#5 1 41;143 A#5 1 41;145 A#5 1 41;147 A#5 1 41;149 A#5 1 41;151 A5 1 41;153 A5 1 41;155 A5 1 41;157 C6 1 41;159 C6 1 41;161 A#5 1 41;163 G5 1 41;165 F5 3 41'
#    https://onlinesequencer.net/59849 Never gonna give you up (by 3CHO)
song2 = '0 A#4 1 0;0 D5 1 0;0 F5 1 0;6 C5 1 0;6 E5 1 0;6 G5 1 0;12 C5 1 0;16 C5 1 0;16 E5 1 0;16 G5 1 0;22 A5 1 0;22 F5 1 0;22 D5 1 0;28 C6 0.5 0;29 A#5 0.5 0;30 A5 1 0;32 F5 1 0;32 D5 1 0;32 A#4 1 0;38 C5 1 0;38 E5 1 0;38 G5 1 0;58 C5 1 0;59 C5 1 0;60 D5 1 0;61 F5 1 0;63 F5 1 0;64 F5 1 0;64 D5 1 0;64 A#4 1 0;44 C5 1 0;70 G5 1 0;70 E5 1 0;70 C5 1 0;80 C5 1 0;80 E5 1 0;80 G5 1 0;76 C5 1 0;86 A5 1 0;86 F5 1 0;86 D5 1 0;92 C6 1 0;93 A#5 1 0;94 A5 1 0;96 A#4 1 0;96 D5 1 0;96 F5 1 0;102 G5 1 0;102 E5 1 0;102 C5 1 0;108 C5 1 0;112 C5 1 0;112 E5 1 0;114 F5 1 0;116 A4 1 0;116 D5 1 0;116 F5 1 0'


#One buzzer on pin 0
mySong = music(song1, pins=[Pin(26)])
mySong2 = music(song2, pins=[Pin(26)])

buttonRed = Pin(28, Pin.IN, Pin.PULL_UP) # Start/Stop
buttonYellow = Pin(27, Pin.IN, Pin.PULL_UP) # Reverse
buttonGreen = Pin(21, Pin.IN, Pin.PULL_UP) # Reset

#play_button_pin = 21

#buttonGreen = Pin(play_button_pin, Pin.IN, Pin.PULL_DOWN)

ledRed = Pin(6, Pin.OUT)
ledYellow = Pin(1, Pin.OUT) 
ledGreen = Pin(11, Pin.OUT)
counter = 0

while True:
    #if buttonGreen.value() == 0:
        #print(mySong.tick())
    print(buttonGreen.value())
    sleep(0.04)
    
 