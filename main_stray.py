from pystray import *
from PIL import Image
from os import getcwd, listdir

from rw import read_data, write_data

class keysoundsTray():
    def __init__(self):
        super().__init__()

        self.voice_list = [i for i in listdir(f"{getcwd()}/media/audio/") if i[0] != "~"]
        self.img_path = f"{getcwd()}/media/icon/neutral.png"

        self.data = read_data()

        self.active_state = True
        self.active_voice = self.data["voice"]

        print(self.active_voice)

        if len(self.voice_list) <= 0:
            raise Exception("None voices where found. Please add one or reinstall the program.")

        self.keysounds_icon()

    def keysounds_icon(self):
        self.icon = Icon(
            'test name',
            icon=Image.open(self.img_path),
            menu=self.keysounds_menu()
        )
    
    def keysounds_menu(self):
        return Menu(
            MenuItem("Activate", self.toggle_check, checked= lambda item: self.active_state),
            # VOICES SUBMENU
            MenuItem("Change Voices", Menu(
                lambda: [MenuItem(
                      # name       x=icon class        command when clicked                        check if curent item is selected      radio style for button
                        voice, lambda x, voice=voice: self.toggle_radio(voice.text), checked= lambda x, voice=voice: self.radio_check(voice), radio=True
                        ) for voice in self.voice_list]
            )),
            MenuItem("Exit", lambda icon: self.icon.stop())
        )


    def toggle_check(self, icon, item):
        self.active_state = not item.checked
    
    # RADIO BUTTONS HANDLER
    def toggle_radio(self, item):
        if item in self.voice_list:
            self.active_voice = item
            self.data["voice"] = self.active_voice
            write_data(self.data)
    
    def radio_check(self, item):
        if item in self.voice_list and item == self.active_voice:
            return True
        else:
            return False


if __name__ == "__main__":
    keysounds_tray = keysoundsTray()