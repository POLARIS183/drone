# This code is © POLARIS183 2022.
# It is short, but it can instantly stop a Tello drone's motors.'
# Please use this if the Tello Acrobatics file causes the drone to crash.
from djitellopy import Tello
tello = Tello()
# Connect to drone, emergency stop.
tello.connect()
tello.emergency()