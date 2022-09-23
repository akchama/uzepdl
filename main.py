import customtkinter
import urllib.request
from helpers import get_monitor_from_coord

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    WIDTH = 780
    HEIGHT = 520
    video_url_string = ""

    def __init__(self):
        super().__init__()

        current_screen = get_monitor_from_coord(self.winfo_x(), self.winfo_y())
        screen_width = current_screen.width
        screen_height = current_screen.height
        x_coordinate = int((screen_width / 2) - (self.WIDTH / 2))
        if not current_screen.is_primary:
            x_coordinate = x_coordinate + 1920
        y_coordinate = int((screen_height / 2) - (self.HEIGHT / 2))
        self.title("CustomTkinter complex_example.py")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}+{x_coordinate}+{y_coordinate}")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)  # call .on_closing() when app gets closed

        self.video_url = customtkinter.CTkEntry(master=self, placeholder_text="Video URL")
        self.video_url.pack(padx=20, pady=10)
        audio_url_text = customtkinter.CTkEntry(master=self, placeholder_text="Audio URL").pack(padx=20, pady=10)

        button = customtkinter.CTkButton(master=self, text="START DOWNLOAD", command=self.button_event)\
            .pack(padx=20, pady=10)

    def button_event(self):
        print("Download started...")
        urllib.request.urlretrieve(self.video_url.get(), 'video_name.mp4')
        print("Download finished.")

    def change_appearance_mode(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def on_closing(self, event=0):
        self.destroy()


if __name__ == "__main__":
    app = App()
    app.mainloop()
