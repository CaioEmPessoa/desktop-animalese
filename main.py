import os
import keyboard
import threading
from playsound import playsound

from main_stray import keysoundsTray

class keysounds():
    def __init__(self):
        super().__init__()

        self.location = os.path.realpath(os.path.join(
                    os.getcwd(), os.path.dirname(__file__)))
        
        self.tray = keysoundsTray()
        
        keyboard.on_press(self.on_key_press)
        
        print("running...")
        self.tray.icon.run()
        # when the icons kills itself

        # TODO: BYE SOUND WHEN EXITS
        print("exit")
        exit()

    def play_char(self, sound_file):

        sound_thread = threading.Thread(target=playsound, args=(sound_file,))
        sound_thread.start()

        
    def handle_keypress(self, char):
        sound_folder = f"{self.location}\\media\\audio\\{self.tray.active_voice}"
        char_list = os.listdir(sound_folder)

        # just proof of concept.
        if len(char_list) == 1:
            print(f"{sound_folder}\\{char_list[0]}", "PENIS")
            self.play_char(f"{sound_folder}\\{char_list[0]}")
            return

        # TODO: optimize this later.
        if char == "?":
            char = "interrogacao"
        elif char == "!":
            char = "exclamacao"
        elif char == "backspace":
            char = "space"
        elif char == "delete":
            char = "del"
        # if char not in list and not a special one, proceed to strip it down and play each separate letter for it.
        elif len(char) > 1 and char+".wav" not in char_list:
            for rchar in char:
                self.play_char(f"{sound_folder}\\{rchar}.wav")
            return

        self.play_char(f"{sound_folder}\\{char}.wav")

        
    def on_key_press(self, event):
        # do nothing when inactive.
        if self.tray.active_state == False:
            return
        
        char = event.name.lower()
        self.handle_keypress(char)

if __name__ == "__main__":
    keysounds_tray = keysounds()