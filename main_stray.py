from pystray import *
from PIL import Image
from os import getcwd, listdir

class keysoundsTray:
    def __init__(self):
        super().__init__()

        self.active_state = True
        self.voice_state = True
        self.voice_list = [i for i in listdir(f"{getcwd()}/media/audio") if i[0] != "~"]
        self.img_path = f"{getcwd()}/media/icon/neutral.png"

        self.keysounds_icon()

    def keysounds_icon(self):
        icon = Icon(
            'test name',
            icon=Image.open(self.img_path),
            menu=self.keysounds_menu()
        )

        print("running...")
        print([x.checked for x in icon.menu.items[1]._action])
        
        icon.run()

        print("exit.")
    
    def keysounds_menu(self):
        return Menu(
            MenuItem("Activate", self.toggle_active, checked= lambda item: self.active_state),
            # SUBMENU
            MenuItem("Change Voice", Menu(
                lambda: [MenuItem(voice, lambda x, voice=voice: self.toggle_voice(voice), checked= lambda x: False) for voice in self.voice_list]
            )),
            MenuItem("Exit", lambda icon: icon.stop())
        )

    def toggle_active(self, icon, item):
        self.active_state = not item.checked
    
    def toggle_voice(self, voice):
        print(voice)


if __name__ == "__main__":
    keysounds_tray = keysoundsTray()