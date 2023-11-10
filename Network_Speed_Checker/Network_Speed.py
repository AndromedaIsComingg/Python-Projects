import speedtest
import time
speed_test = speedtest.Speedtest(secure= True)
print("Checking network download speed..")
time.sleep(2)
print("Checking network download speed....")
time.sleep(2)
print("Checking network download speed.......")

def bytes_to_mb (bytes):
	KB = 1024 # Convert from bits per second to megabits per second
	MB = KB * 1024
	return int(bytes/MB)
download_speed = bytes_to_mb(speed_test.download())
print (f"your download speed is {download_speed} MB")