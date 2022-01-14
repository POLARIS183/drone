# Hi, I'm POLARIS183, and this is my attempt to get a Tello drone to do some cool tricks!
# I'm writing this code on behalf of my friend, who runs the drone.
# First things first - I'm going to import the Tello function from PyPi:djitellopy, along with time.
# You can see this on Github - https://github.com/damiafuentes/DJITelloPy.
from djitellopy import Tello
import time
print("This code is © POLARIS183 2022, using DJITelloPy.")
time.sleep(1)
print("This can be accessed on Github at https://github.com/damiafuentes/DJITelloPy.")
time.sleep(1)
print("If, at any point, something goes wrong with this program, use tello.emergency() to emergency stop, and contact me on northpolaris@protonmail.com.")
time.sleep(1)
print("Thanks for running this code! The program will connect in two seconds. Make sure the drone and computer are about 1 metre away.")
time.sleep(2)
# Disclaimer's out of the way...
tello = Tello()
# Now, I have to connect the program...
tello.connect()
# And get it to take off!
tello.takeoff()
# Now, it's time for the fun stuff...
print(tello.get_height())
tello.move_left(100)
tello.flip_back()
tello.set_speed(10)
tello.move_forward(100)
tello.rotate_clockwise(120)
tello.set_speed(100)
tello.move_forward(100)
# All good things must come to an end...
tello.land()
tello.end()
