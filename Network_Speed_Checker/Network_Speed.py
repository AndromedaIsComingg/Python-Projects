import tkinter as tk
from tkinter import Label, Button
import speedtest
import threading
import time
import pygame

class NetworkSpeedTestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Network Speed Checker")
        self.root.geometry("400x200")

        self.label_result = Label(self.root, text="", font=("Helvetica", 14))
        self.label_result.pack(pady=10)

        self.button_start_test = Button(self.root, text="Start Speed Test", command=self.run_speed_test)
        self.button_start_test.pack(pady=10)

        pygame.mixer.init()

        # Background sound
        pygame.mixer.music.load("/Users/Adebisi/Documents/Python_Projects/Network_Speed_Checker/sounds/backgroud.wav")  # Replace with the path to your background sound file
        self.volume = 0.2  # Initial volume for background sound
        pygame.mixer.music.set_volume(self.volume)

        # Start test sound
        self.start_test_sound = pygame.mixer.Sound("/Users/Adebisi/Documents/Python_Projects/Network_Speed_Checker/sounds/fx.wav")  # Replace with the path to your start test sound file
        self.start_test_volume = 1  # Initial volume for start test sound
        self.start_test_sound.set_volume(self.start_test_volume)

        # Create a channel for the start test sound
        self.start_test_channel = pygame.mixer.Channel(1)

        # Play the background sound immediately
        threading.Thread(target=self.play_background_sound, daemon=True).start()

        # Bind the window closing event to the method
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def run_speed_test(self):
        # Play the start test sound when the button is clicked
        threading.Thread(target=self.play_start_test_sound).start()

        self.label_result.config(text="Checking network speed..")
        threading.Thread(target=self.perform_speed_test).start()

    def play_background_sound(self):
        # Play the background sound continuously
        pygame.mixer.music.play(-1)

    def play_start_test_sound(self):
        # Set the volume for the start test sound and play it on the designated channel
        self.start_test_channel.play(self.start_test_sound)

    def perform_speed_test(self):
        try:
            speed_test = speedtest.Speedtest(secure=True)

            # Simulate a delay to show the progress
            for _ in range(5):
                time.sleep(2)
                self.label_result.config(text=self.label_result.cget("text") + ".")

            download_speed = self.bytes_to_mb(speed_test.download())
            upload_speed = self.bytes_to_mb(speed_test.upload())

            result_text = f"Your download speed is {download_speed} Mbps\nYour upload speed is {upload_speed} Mbps"
            self.label_result.config(text=result_text)

        except speedtest.ConfigRetrievalError:
            error_text = "Error retrieving speed test configuration. \nPlease check your internet connection."
            self.label_result.config(text=error_text)
        except Exception as e:
            error_text = f"An error occurred: {str(e)}"
            self.label_result.config(text=error_text)

        finally:
            # Stop the start test sound when the network speed is displayed
            self.start_test_channel.stop()

    def on_closing(self):
        # Stop the background sound when the user closes the app
        pygame.mixer.music.stop()
        self.root.destroy()

    @staticmethod
    def bytes_to_mb(bytes):
        KB = 1024  # Converts from bits per second to megabits per second
        MB = KB * 1024
        return int(bytes / MB)

if __name__ == "__main__":
    root = tk.Tk()
    app = NetworkSpeedTestApp(root)
    root.mainloop()
