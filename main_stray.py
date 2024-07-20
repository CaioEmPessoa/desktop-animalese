from pystray import *
from PIL import Image
from os import getcwd, listdir

class keysoundsTray:
    def __init__(self):
        super().__init__()

        self.lang_list = [i for i in listdir(f"{getcwd()}/media/audio") if i[0] != "~"]
        self.voice_list = [i for i in listdir(f"{getcwd()}/media/audio/pt-br/") if i[0] != "~"]
        self._path = f"{getcwd()}/media/icon/neutral.png"

        self.active_state = True
        self.active_lang = "None"
        self.active_voice = "None"

        if len(self.voice_list) <= 0:
            raise Exception("None voices where found. Please add one or reinstall the program.")

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
            MenuItem("Activate", self.toggle_check, checked= lambda item: self.active_state),
            # LANG SUBMENU
            MenuItem("Change Language", Menu(
                lambda: [MenuItem(
                      # name       x=icon class        command when clicked                        check if curent item is selected      radio style for button
                        lang, lambda x, lang=lang: self.toggle_radio(lang.text), checked= lambda x, lang=lang: self.radio_check(lang), radio=True
                        ) for lang in self.lang_list] # in a loop of all languages
            )),
            # VOICES SUBMENU
            MenuItem("Change Voices", Menu(
                lambda: [MenuItem(
                        voice, lambda x, voice=voice: self.toggle_radio(voice.text), checked= lambda x, voice=voice: self.radio_check(voice), radio=True
                        ) for voice in self.voice_list]
            )),
            MenuItem("Exit", lambda icon: icon.stop())
        )

    def toggle_check(self, icon, item):
        self.active_state = not item.checked
    
    # RADIO BUTTONS HANDLER
    def toggle_radio(self, item):
        if item in self.voice_list:
            self.active_voice = item
        elif item in self.lang_list:
            self.active_lang = item
    
    def radio_check(self, item):
        # Could be in one if statemant but I prefer this way, better organized
        if item in self.voice_list and item == self.active_voice:
            return True
        elif item in self.lang_list and item == self.active_lang:
            return True
        else:
            return False


if __name__ == "__main__":
    keysounds_tray = keysoundsTray()