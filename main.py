import os
import keyboard
import threading
from playsound import playsound

location = os.path.realpath(os.path.join(
            os.getcwd(), os.path.dirname(__file__)))

print(location)

def play_sound(sound_file):
    try:
        playsound(sound_file)
    except:
        pass
    
def handle_keypress(char):
    sound_folder = "\\audio\\pt-br"

    if char == "?":
        char = "interrogacao"
    elif char == "!":
        char = "exclamacao"

    sound_file = f"{location}{sound_folder}\\{char}.wav"
    
    # Correctly create a thread to play the sound
    sound_thread = threading.Thread(target=play_sound, args=(sound_file,))
    sound_thread.start()
    
def on_key_press(event):
    print(event.name)
    char = event.name.lower()
    handle_keypress(char)

keyboard.on_press(on_key_press)
keyboard.wait() 