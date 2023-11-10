import speedtest
import time
speed_test = speedtest.Speedtest(secure= True)

print("Checking network speed..")
time.sleep(2)
print("Checking network speed....")
time.sleep(2)
print("Checking network speed please wait.......")

def bytes_to_mb (bytes):
	KB = 1024 # Converts from bits per second to megabits per second
	MB = KB * 1024
	return int(bytes/MB)
download_speed = bytes_to_mb(speed_test.download())
upload_speed = bytes_to_mb(speed_test.upload())


print (f"your download speed is {download_speed} Mbps",)
print (f"your upload speed is {upload_speed} Mbps")
