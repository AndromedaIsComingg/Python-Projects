import tkinter as tk
from tkinter import Label, Button
import speedtest
import threading
import time

class NetworkSpeedTestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Network Speed Checker")
        self.root.geometry("400x200")

        self.label_result = Label(self.root, text="", font=("Helvetica", 14))
        self.label_result.pack(pady=30)

        self.button_start_test = Button(self.root, text="Start Speed Test", command=self.run_speed_test)
        self.button_start_test.pack(pady=10)

    def run_speed_test(self):
        self.label_result.config(text="Checking network speed..")
        threading.Thread(target=self.perform_speed_test).start()

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
            error_text = "Error retrieving speed test configuration \nPlease check your internet connection."
            self.label_result.config(text=error_text)
        except Exception as e:
            error_text = f"An error occurred: {str(e)}"
            self.label_result.config(text=error_text)

    @staticmethod
    def bytes_to_mb(bytes):
        KB = 1024  # Converts from bits per second to megabits per second
        MB = KB * 1024
        return int(bytes / MB)

if __name__ == "__main__":
    root = tk.Tk()
    app = NetworkSpeedTestApp(root)
    root.mainloop()
