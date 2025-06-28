import tkinter as tk

class AudioCue:
    def __init__(self):
        self.window_width = 1800
        self.window_height = 600
        self.root = tk.Tk()
        self.root.title("audiocue")
        self.root.geometry(f"{self.window_width}x{self.window_height}")

    def run_application(self):
        self.root.mainloop()

if __name__ == "__main__":

    audiocue = AudioCue()
    audiocue.run_application()