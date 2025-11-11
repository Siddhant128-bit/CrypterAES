from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.popup import Popup
import os
import enc_dec
# import aes_engine

# Window.size = (400, 600)

class MainScreen(Screen):
    pass

class EncryptScreen(Screen):
    pass

class DecryptScreen(Screen):
    pass

class AESApp(App):
    selected_file = None
    mode = None

    def build(self):
        return Builder.load_file("main.kv")

    # --- Open file chooser popup ---
    def open_file_dialog(self, mode):
        self.mode = mode

        layout = BoxLayout(orientation='vertical')
        chooser = FileChooserListView(path='.', filters=['*.*'])
        layout.add_widget(chooser)

        select_btn = Button(text='Select', size_hint_y=0.1)
        layout.add_widget(select_btn)

        popup = Popup(title='Select File', content=layout, size_hint=(0.9, 0.9))

        def select_file(instance):
            if chooser.selection:
                self.selected_file = chooser.selection[0]
                screen = self.root.get_screen(mode)
                screen.ids.status.text = f"Selected: {self.selected_file}"
            popup.dismiss()

        select_btn.bind(on_press=select_file)
        popup.open()

    def encrypt_selected(self):
        if not self.selected_file:
            self.root.get_screen("encrypt").ids.status.text = "Select file"
            return
        try:
            pw=enc_dec.generate_password()
            print(f"password: {pw}")
            output = self.selected_file + ".enc"  
            enc_dec.encrypt_file(self.selected_file,output,pw)
            self.root.get_screen("encrypt").ids.status.text = f"Password → {pw} \n File → {output} "
        
        except Exception as e:
            self.root.get_screen("encrypt").ids.status.text = f"Error: {str(e)}"

    def decrypt_selected(self, password):
        if not self.selected_file or not password:
            self.root.get_screen("decrypt").ids.status.text = "Select file and enter password"
            return
        try:
            output = self.selected_file.replace(".enc", "")  # placeholder
            enc_dec.decrypt_file(self.selected_file,output,password)
            self.root.get_screen("decrypt").ids.status.text = f"Decrypted → {output}"
            os.remove(self.selected_file)
        except Exception as e:
            self.root.get_screen("decrypt").ids.status.text = f"Error: {str(e)}"

    def select_file(self, mode):
        self.open_file_dialog(mode)


if __name__ == "__main__":
    AESApp().run()
