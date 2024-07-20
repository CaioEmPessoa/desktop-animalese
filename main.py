import os
import keyboard
import threading
from playsound import playsound

from main_stray import keysoundsTray

class keysounds:
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

    def play_sound(self, sound_file):
        try:
            playsound(sound_file)
        except:
            print(f"File not found: '.{sound_file[len(self.location):]}'")
            pass
        
    def handle_keypress(self, char):
        sound_folder = f"\\media\\audio\\{self.tray.active_voice}"

        if char == "?":
            char = "interrogacao"
        elif char == "!":
            char = "exclamacao"

        sound_file = f"{self.location}{sound_folder}\\{char}.wav"
        
        print(char)

        # Correctly create a thread to play the sound
        sound_thread = threading.Thread(target=self.play_sound, args=(sound_file,))
        sound_thread.start()
        
    def on_key_press(self, event):
        # do nothing when inactive.
        if self.tray.active_state == False:
            return
        
        char = event.name.lower()
        self.handle_keypress(char)

if __name__ == "__main__":
    keysounds_tray = keysounds()