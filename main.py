from buzzer_music import music
from time import sleep
from machine import Pin, I2C
from pico_i2c_lcd import I2cLcd

#https://onlinesequencer.net/3712491 Jingle Bells
song1 = '0 C5 1 41;2 A5 1 41;4 G5 1 41;6 F5 1 41;8 C5 2 41;13 C5 1 41;14 C5 1 41;15 C5 1 41;17 A5 1 41;19 G5 1 41;21 F5 1 41;23 D5 2 41;30 A#5 1 41;32 A5 1 41;28 D5 1 41;34 G5 1 41;36 E5 2 41;41 C6 1 41;43 C6 1 41;47 G5 1 41;49 A5 2 41;45 A#5 1 41;54 C5 1 41;56 A5 1 41;58 G5 1 41;60 F5 1 41;62 C5 2 41;67 C5 1 41;68 C5 1 41;69 C5 1 41;71 A5 1 41;73 G5 1 41;75 F5 1 41;77 D5 2 41;82 D5 1 41;84 A#5 1 41;86 A5 1 41;88 G5 1 41;90 C6 1 41;94 C6 1 41;92 C6 1 41;96 C6 1 41;98 D6 1 41;100 C6 1 41;102 A#5 1 41;104 G5 1 41;106 F5 2 41;110 C6 2 41;114 A5 1 41;116 A5 1 41;118 A5 2 41;122 A5 1 41;124 A5 1 41;126 A5 2 41;129 A5 1 41;131 C6 1 41;133 F5 1 41;135 G5 1 41;137 A5 2 41;141 A#5 1 41;143 A#5 1 41;145 A#5 1 41;147 A#5 1 41;149 A#5 1 41;151 A5 1 41;153 A5 1 41;155 A5 1 41;157 C6 1 41;159 C6 1 41;161 A#5 1 41;163 G5 1 41;165 F5 3 41'

#https://onlinesequencer.net/59849 Never gonna give you up (by 3CHO)
song2 = '0 A#4 1 0;0 D5 1 0;0 F5 1 0;6 C5 1 0;6 E5 1 0;6 G5 1 0;12 C5 1 0;16 C5 1 0;16 E5 1 0;16 G5 1 0;22 A5 1 0;22 F5 1 0;22 D5 1 0;28 C6 0.5 0;29 A#5 0.5 0;30 A5 1 0;32 F5 1 0;32 D5 1 0;32 A#4 1 0;38 C5 1 0;38 E5 1 0;38 G5 1 0;58 C5 1 0;59 C5 1 0;60 D5 1 0;61 F5 1 0;63 F5 1 0;64 F5 1 0;64 D5 1 0;64 A#4 1 0;44 C5 1 0;70 G5 1 0;70 E5 1 0;70 C5 1 0;80 C5 1 0;80 E5 1 0;80 G5 1 0;76 C5 1 0;86 A5 1 0;86 F5 1 0;86 D5 1 0;92 C6 1 0;93 A#5 1 0;94 A5 1 0;96 A#4 1 0;96 D5 1 0;96 F5 1 0;102 G5 1 0;102 E5 1 0;102 C5 1 0;108 C5 1 0;112 C5 1 0;112 E5 1 0;114 F5 1 0;116 A4 1 0;116 D5 1 0;116 F5 1 0'

#https://onlinesequencer.net/1256057 Hedwig's Theme (Harry Potter)
song3 = '0 B3 1 12;2 E4 1 12;5 G4 1 12;6 F#4 1 12;8 E4 2 12;12 B4 1 12;14 A4 3 12;19 F#4 2 12;23 E4 1 12;25 G4 1 12;26 F#4 1 12;28 D4 2 12;31 F#4 1 12;33 B3 4 12;33 B5 4 11;38 B5 1 11;40 E6 1 11;43 G6 1 11;44 F#6 1 11;46 E6 2 11;49 B6 1 11;51 D7 2 11;54 C#7 1 11;56 C7 2 11;59 A6 1 11;61 C7 1 11;63 B6 1 11;64 A#6 1 11;66 B5 2 11;69 G6 1 11;71 E6 5 11;80 G5 2 11;82 B5 2 11;77 B5 2 11;85 G5 2 11;87 D6 1 11;90 C#6 1 11;92 C6 1 11;95 A5 1 11;97 C6 1 11;99 B5 1 11;100 A#5 1 11;103 B4 5 11;106 G5 1 11;108 E5 8 12;38 B3 1 12;40 E4 1 12;51 D5 2 12;56 C5 2 12;66 B4 2 12'

#https://onlinesequencer.net/2079142 Mission Impossible (loop)
song4 = '0 G4 1 34;3 G4 1 34;6 A#4 1 34;8 C5 1 34;10 G4 1 34;13 G4 1 34;16 F4 1 34;18 F#4 1 34;20 G4 1 34;23 G4 1 34;26 A#4 1 34;28 C5 1 34;30 G4 1 34;33 G4 1 34;36 F4 1 34;38 F#4 1 34;40 G4 1 34;43 G4 1 34;46 A#4 1 34;48 C5 1 34;50 G4 1 34;53 G4 1 34;56 F4 1 34;58 F#4 1 34;60 G4 1 34;63 G4 1 34;66 A#4 1 34;68 C5 1 34;70 G4 1 34;73 G4 1 34;76 F4 1 34;78 F#4 1 34;40 A#6 1 23;41 G6 1 23;42 D6 6 23;50 A#6 1 23;51 G6 1 23;52 C#6 6 23;60 A#6 1 23;61 G6 1 23;62 C6 6 23;70 A#5 1 23;71 C6 1 23;80 G4 1 34;83 G4 1 34;86 A#4 1 34;88 C5 1 34;90 G4 1 34;93 G4 1 34;96 F4 1 34;98 F#4 1 34;100 G4 1 34;103 G4 1 34;106 A#4 1 34;108 C5 1 34;110 G4 1 34;113 G4 1 34;116 F4 1 34;118 F#4 1 34;120 G4 1 34;123 G4 1 34;126 A#4 1 34;128 C5 1 34;130 G4 1 34;133 G4 1 34;136 F4 1 34;138 F#4 1 34;140 G4 1 34;143 G4 1 34;146 A#4 1 34;148 C5 1 34;150 G4 1 34;153 G4 1 34;156 F4 1 34;80 A#5 1 23;81 G5 1 23;82 F#6 6 23;90 A#5 1 23;91 G5 1 23;92 F6 6 23;100 A#5 1 23;101 G5 1 23;102 E6 6 23;110 D#6 1 23;111 D6 1 23;120 G6 1 23;123 G6 1 23;126 A#6 1 23;128 C7 1 23;130 G6 1 23;133 G6 1 23;136 F6 1 23;138 F#6 1 23;140 G6 1 23;143 G6 1 23;146 A#6 1 23;148 C7 1 23;150 G6 1 23;153 G6 1 23;156 F6 1 23;159 F7 1 23;160 G7 16 23;162 G7 14 23;165 G7 11 23;168 G7 8 23;172 G7 4 23'

#https://onlinesequencer.net/142684 Star Wars Theme Song
song5 = '2 C5 2 8;8 G5 2 8;10 G5 2 8;0 C5 2 8;13 F5 1 8;14 E5 1 8;15 D5 1 8;18 C6 2 8;20 C6 2 8;24 G5 2 8;26 G5 2 8;29 F5 1 8;30 E5 1 8;31 D5 1 8;34 C6 2 8;36 C6 2 8;40 G5 2 8;42 G5 2 8;45 F5 1 8;46 E5 1 8;47 F5 1 8;48 D5 2 8;56 C5 2 8;58 C5 2 8;64 G5 2 8;66 G5 2 8;69 F5 1 8;70 E5 1 8;71 D5 1 8;80 G5 2 8;82 G5 2 8;85 F5 1 8;86 E5 1 8;87 D5 1 8;90 C6 2 8;92 C6 2 8;96 G5 2 8;98 G5 2 8;101 F5 1 8;102 E5 1 8;103 F5 1 8;104 D5 2 8;56 C5 2 9;58 C5 2 9;64 G5 2 9;66 G5 2 9;69 F5 1 9;70 E5 1 9;71 D5 1 9;80 G5 2 9;82 G5 2 9;96 G5 2 9;98 G5 2 9;104 D5 2 9;85 F5 1 9;86 E5 1 9;87 D5 1 9;101 F5 1 9;102 E5 1 9;103 F5 1 8;74 C6 2 8;76 C6 2 8;74 C6 2 11;76 C6 2 11;90 C6 2 11;92 C6 2 11;103 F5 1 9;108 C5 2 8;110 C5 2 8;116 G5 2 8;118 G5 2 8;121 F5 1 8;122 E5 1 8;123 D5 1 8;126 C6 2 8;128 C6 2 8;132 G5 2 8;134 G5 2 8;137 F5 1 8;138 E5 1 8;139 D5 1 8;144 C6 2 8;148 G5 2 8;150 G5 2 8;153 F5 1 8;154 E5 1 8;155 F5 1 8;156 D5 2 8;108 C5 2 9;110 C5 2 9;116 G5 2 9;118 G5 2 9;132 G5 2 9;134 G5 2 9;148 G5 2 9;150 G5 2 9;156 D5 2 9;142 C6 2 8;142 C6 2 11;144 C6 2 11;126 C6 2 11;128 C6 2 11;121 F5 1 9;122 E5 1 9;123 D5 1 9;137 F5 1 9;138 E5 1 9;139 D5 1 9;153 F5 1 9;154 E5 1 9;155 F5 1 9;108 A3 1 2;109 A3 1 2;110 G3 1 2;111 G3 1 2;115 A3 1 2;114 A3 1 2;113 G3 1 2;118 A3 1 2;119 A3 1 2;120 A3 1 2;122 G3 1 2;121 G3 1 2;123 G3 1 2;116 G3 1 2;117 G3 1 2;124 A3 1 2;125 A3 1 2;154 B3 1 2;160 C5 2 8;162 C5 2 8;168 G5 2 8;170 G5 2 8;173 F5 1 8;174 E5 1 8;175 D5 1 8;178 C6 2 8;180 C6 2 8;184 G5 2 8;186 G5 2 8;189 F5 1 8;190 E5 1 8;191 D5 1 8;194 C6 2 8;196 C6 2 8;200 G5 2 8;202 G5 2 8;205 F5 1 8;206 E5 1 8;207 F5 1 8;208 D5 2 8;162 C5 2 9;160 C5 2 9;168 G5 2 9;170 G5 2 9;184 G5 2 9;186 G5 2 9;200 G5 2 9;202 G5 2 9;208 D5 2 9;173 F5 1 9;174 E5 1 9;175 D5 1 9;189 F5 1 9;190 E5 1 9;191 D5 1 9;205 F5 1 9;206 E5 1 9;207 F5 1 9;178 C6 2 11;180 C6 2 11;194 C6 2 11;154 B3 2 2;156 B3 2 2;160 A3 1 2;161 A3 1 2;162 G3 1 2;163 G3 1 2;165 G3 1 2;166 A3 1 2;167 A3 1 2;168 G3 1 2;169 G3 1 2;170 A3 1 2;171 A3 1 2;172 A3 1 2;173 G3 1 2;174 G3 1 2;175 G3 1 2;176 A3 1 2;177 A3 1 2;196 C6 2 11;208 B3 2 2;160 C5 2 6;162 C5 2 6;168 G5 2 6;170 G5 2 6;178 C6 2 6;180 C6 2 6;184 G5 2 6;186 G5 2 6;194 C6 2 6;196 C6 2 6;200 G5 2 6;202 G5 2 6;208 D5 2 6;189 F5 1 6;190 E5 1 6;191 D5 1 6;205 F5 1 6;206 E5 1 6;207 F5 1 6;173 F5 1 6;174 E5 1 6;175 D5 1 6;206 B3 2 2;130 A3 1 2;131 A3 1 2;132 A3 1 2;133 G3 1 2;134 G3 1 2;135 G3 1 2;138 B3 1 2;140 B3 1 2;141 B3 1 2;139 B3 1 2;136 A3 1 2;137 A3 1 2;142 A3 1 2;143 A3 1 2;144 A3 1 2;145 G3 1 2;147 G3 1 2;146 G3 1 2;149 G3 1 2;148 A3 1 2;151 A3 1 2;152 A3 1 2;150 G3 1 2;153 B3 1 2;182 A3 1 2;183 A3 1 2;184 A3 1 2;185 G3 1 2;186 G3 1 2;187 G3 1 2;188 A3 1 2;189 A3 1 2;190 B3 1 2;191 B3 1 2;192 B3 1 2;193 B3 1 2;194 A3 1 2;195 A3 1 2;196 A3 1 2;198 G3 1 2;197 G3 1 2;199 G3 1 2;200 A3 1 2;201 G3 1 2;202 G3 1 2;203 A3 1 2;204 A3 1 2;205 B3 1 2;212 A3 1 2;213 A3 1 2;214 G3 1 2;215 G3 1 2;217 G3 1 2;218 A3 1 2;219 A3 1 2;220 G3 1 2;221 G3 1 2;223 A3 1 2;222 A3 1 2;224 A3 1 2;225 G3 1 2;226 G3 1 2;227 G3 1 2;228 A3 1 2;229 A3 1 2;234 A3 1 2;235 A3 1 2;236 A3 1 2;237 G3 1 2;238 G3 1 2;239 G3 1 2;240 A3 1 2;241 A3 1 2;242 B3 1 2;243 B3 1 2;244 B3 1 2;245 B3 1 2;246 A3 1 2;247 A3 1 2;248 A3 1 2;249 G3 1 2;250 G3 1 2;251 G3 1 2;252 A3 1 2;253 G3 1 2;254 G3 1 2;255 A3 1 2;256 A3 1 2;257 B3 1 2;258 B3 2 2;260 B3 2 2;212 C5 2 3;214 C5 2 3;220 G5 2 3;222 G5 2 3;225 F5 1 3;226 E5 1 3;227 D5 1 3;230 C6 2 3;232 C6 2 3;236 G5 2 3;238 G5 2 3;241 F5 1 3;242 E5 1 3;243 D5 1 3;248 C6 2 3;246 C6 2 3;252 G5 2 3;254 G5 2 3;257 F5 1 3;258 E5 1 3;259 F5 1 3;260 D5 2 3;262 D5 2 3;266 D5 2 3;264 D5 2 3;268 D5 2 3;270 C#5 2 3;272 C#5 2 3;274 C5 2 3;276 B4 2 3;278 A#4 2 3'

# LCD
i2c = I2C(1, sda=Pin(2), scl=Pin(3), freq=400000) # object to communicate with the LCD screen over the I2C protocol
I2C_ADDR = i2c.scan()[0] # this will store the first I2C address found when we scan the bus
lcd = I2cLcd(i2c, I2C_ADDR, 2, 16) # object to set up the I2C connection from the libery 
 
lcd.hide_cursor()

#One buzzer on pin 0
mySong = music(song1, pins=[Pin(26)])
mySong2 = music(song2, pins=[Pin(26)])
mySong3 = music(song3, pins=[Pin(26)])
mySong4 = music(song4, pins=[Pin(26)])
mySong5 = music(song5, pins=[Pin(26)])

playlist = [mySong, mySong2, mySong3, mySong4, mySong5]
songTitles = ["Jingle Bells", "Never gonna\ngive you up", "Hedwig's Theme\nHarry Potter", "Mission\nImpossible", "Star Wars\nTheme Song"]

songNumber = 0

buttonChangeSong = Pin(27, Pin.IN, Pin.PULL_UP) # Start/Stop
buttonReset = Pin(28, Pin.IN, Pin.PULL_UP) # Reverse
buttonStartStop = Pin(20, Pin.IN, Pin.PULL_UP) # Reset
playflag = 0
pauseflag = []
resetflag = []
changescreenflag = 0

i = 0
while i < len(playlist):
    pauseflag.append(0)
    resetflag.append(0)
    i = i + 1

lcd.clear()
lcd.putstr("Press green\n")
lcd.putstr("to start :)\n")


while True:
    nowPlaying = playlist[songNumber]
    if buttonStartStop.value() == 0:
        if playflag == 0:
            playflag = 1
            changescreenflag = 1
            if resetflag[songNumber] == 1:
                nowPlaying.restart()
                resetflag[songNumber] = 0
            else:
                nowPlaying.resume()
                pauseflag[songNumber] = 0
        elif playflag == 1:
            playflag = 0
            pauseflag[songNumber] = 1
            nowPlaying.stop()
            lcd.clear()
            lcd.putstr("Pause\n")
            sleep(1)
            
    if buttonReset.value() == 0:
        nowPlaying.stop()
        nowPlaying.clearLights()
        lcd.clear()
        lcd.putstr("Reset\n")
        sleep(1)
        playflag = 0
        pauseflag[songNumber] = 0
        resetflag[songNumber] = 1
        changescreenflag = 1    
        
    if buttonChangeSong.value() == 0:
        nowPlaying.stop()
        nowPlaying.clearLights()
        playflag = 0
        resetflag[songNumber] = 1
        pauseflag[songNumber] = 0
        if songNumber == len(playlist)-1:
            songNumber = 0
        else:
            songNumber = songNumber + 1
        lcd.clear()
        lcd.putstr("New song\n")
        sleep(0.5)
        lcd.clear()
        lcd.putstr(songTitles[songNumber] + "\n")
        sleep(1)
        changescreenflag = 1

    if playflag == 0 and changescreenflag == 1:
        lcd.clear()
        changescreenflag = 0
        if pauseflag[songNumber] == 0:
            lcd.putstr("Press green\n")
            lcd.putstr("to start :)\n")
            
    if playflag == 1 and changescreenflag == 1:
        lcd.clear()
        changescreenflag = 0
        lcd.putstr(songTitles[songNumber] + "\n")
    elif playflag == 1 and changescreenflag == 0:
        nowPlaying.tick()
        
    sleep(0.04)