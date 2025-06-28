import tkinter as tk

class AudioCue:
    def __init__(self):
        self.window_width = 1800
        self.window_height = 600
        self.root = tk.Tk()
        self.root.title("audiocue")
        self.root.geometry(f"{self.window_width}x{self.window_height}")

    @staticmethod
    def get_audio() -> list[str]:
        song_order = [
            "conch_sound.mp3",
            "opening_music.mp3",
            "bolero.mp3",
            "symphony_of_the_devil.mp3",
            "bomb_sound_effect.mp3",
            "lust.mp3",
            "piano_music.mp3",
            "guns_sound_effect.mp3",
            "greed.mp3",
            "illusion_with_speaking.mp3",
            "envy.mp3",
            "hush_hush_song.mp3",
            "dharma_music.mp3",
            "hush_hush_song.mp3"]

        ls = []
        for mp3 in song_order:
            ls.append("./audio/" + mp3)
        return ls

    def run_application(self):
        self.root.mainloop()


if __name__ == "__main__":

    audiocue = AudioCue()
    audiocue.run_application()