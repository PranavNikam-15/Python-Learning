# Base class
class Device:
    def __init__(self, name):
        self.name = name

    def power_on(self):
        print(f"{self.name} is powered on")

    def power_off(self):
        print(f"{self.name} is powered off")


# Camera device
class CameraDevice(Device):
    def take_photo(self):
        print(f"{self.name} takes a photo")


# Music device
class MusicDevice(Device):
    def play_music(self):
        print(f"{self.name} is playing music")


# SmartPhone inherits CameraDevice and MusicDevice -> Hybrid
class SmartPhone(CameraDevice, MusicDevice):
    def make_call(self, number):
        print(f"{self.name} is calling {number}")


# Using the SmartPhone
phone = SmartPhone("iPhone 17")

phone.power_on()       # From Device
phone.take_photo()     # From CameraDevice
phone.play_music()     # From MusicDevice
phone.make_call("1234567890")  # From SmartPhone
phone.power_off()      # From Device