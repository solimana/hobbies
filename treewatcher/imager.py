# rclone sync /home/solipi5/Desktop/hobbies/treewatcher/images gdrive:hobbies/windowimager/images -vv
# https://rclone.org/drive/#making-your-own-client-id
# source myenv/bin/activate
#crontab -e
# */1 * * * * /usr/bin/python3 /home/solipi5/Desktop/hobbies/treewatcher/imager.py
# */1 * * * * /usr/bin/rclone sync /home/solipi5/Desktop/hobbies/treewatcher/images gdrive:hobbies/windowimager/images -vv

from picamera2 import Picamera2
import time
from datetime import datetime
import pytz

# Initialize the camera
camera = Picamera2()

# Set the camera resolution to 2592x1944 (maximum for Arducam 5MP)
camera.configure(camera.create_still_configuration())

# Start the camera
camera.start()

# Get the current date and time in Eastern Time
eastern_time_zone = pytz.timezone("US/Eastern")
current_time = datetime.now(eastern_time_zone).strftime("%Y-%m-%d_%H-%M-%S")

# Create the filename using the current date and time
filename = f"/home/solipi5/Desktop/hobbies/treewatcher/images/tak_{current_time}.jpg"

# Capture and save the image with the generated filename
camera.capture_file(filename)

# Stop the camera
camera.stop()

print("Picture taken and saved as photo.jpg")
