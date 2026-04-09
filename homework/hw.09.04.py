# Comprehensive Task: Home Appliance Management System 
# You are tasked with building a Home Appliance Management System using abstract classes 
# and interfaces in Python. This system will allow users to interact with various types of home 
# appliances, simulate their behavior, and track their statuses. 
# Step 1: Create the Abstract Class Appliance 
# 1. Define the abstract class: 
# ○ Use the abc module to create an abstract class Appliance. 
# ○ Add the following: 
# ■ Abstract Method: turn_on() – should print a message indicating that 
# the appliance has been turned on. 
# ■ Abstract Method: turn_off() – should print a message indicating that 
# the appliance has been turned off. 
# ■ Concrete Method: status() – should print "Appliance is 
# currently OFF." by default. 
# 2. Attributes: 
# ○ Add an instance attribute is_on (default: False). 
# ○ Modify turn_on() and turn_off() to update this attribute when implemented.

from abc import ABC,abstractmethod

class Appliance(ABC):
    def __init__(self, is_on = False):
        self.is_on = is_on


    @abstractmethod
    def turn_on():

        print("turned on")

    @abstractmethod
    def turn_off():
        print("turned off")

    def status():
        print("Appliance is currently OFF.")

    
#Step 2: Create Concrete Subclasses 
# 1. Define WashingMachine: 
# ○ Implements turn_on() – prints "Washing machine started. Ready to 
# wash clothes!". 
# ○ Implements turn_off() – prints "Washing machine stopped. 
# Goodbye!". 
# 2. Define TV: 
# ○ Implements turn_on() – prints "TV is now ON. Enjoy your show!". 
# ○ Implements turn_off()  – prints "TV is already OFF." 
# 3. Define Refrigerator: 
# ○ Implements turn_on() – prints "Refrigerator is now ON. Cooling 
# has started.". 
# ○ Implements turn_off() – prints "Refrigerator is now OFF. Be 
# careful, food might spoil!".

class AE(Exception):
    ...



class inter(ABC):
    @abstractmethod
    def connect_to_wifi(ssid, password):
        ...
    @abstractmethod
    def control_via_app(command):
        ...



class WashingMachine(Appliance, inter):
    def __init__(self):
        super().__init__()

    def turn_on():
        if self.is_on:
            raise AE("wm already on")
        self.is_on = True
        print("washing machine started")

    def turn_off():
        if not self.is_on:
            raise AE("wm already off")
        self.is_on = False
        print("washing machine is off")

    def connect_to_wifi(self, ssid, password):
        print("connected to wifi") #todo

    def control_via_app(command):
        ...




class TV(Appliance, inter):
    def __init__(self):
        super().__init__()

    def turn_on():
        if self.is_on:
            raise AE("tv already on")
        self.is_on = True
        print("TV started")

    def turn_off():
        if not self.is_on:
            raise AE("tv already off")
        self.is_on = False
        print("TV is off")

    def connect_to_wifi(self, ssid, password):
        print("connected to wifi") #todo


        
class ref(Appliance):
    def __init__(self):
        super().__init__()

    def turn_on():
        if self.is_on:
            raise AE("ref already on")
        self.is_on = True
        print("ref started")

    def turn_off():
        if not self.is_on:
            raise AE("ref already off")
        self.is_on = False
        print("ref is off")

        


#
#
#Step 3: Add an Interface for Smart Appliances 
# 1. Create an Interface-Like Abstract Class: 
# ○ Define SmartAppliance using the abc module. 
# ○ Add the following abstract methods: 
# ■ connect_to_wifi(ssid, password) – for connecting the appliance 
# to a Wi-Fi network. 
# ■ control_via_app(command) – for controlling the appliance remotely 
# via an app. 
# 2. Modify Subclasses to Support Smart Features: 
# ○ Add smart capabilities to WashingMachine and TV by implementing the 
# SmartAppliance interface. 
# ○ Example implementation for connect_to_wifi(): 
# ■ Prints "Connecting to Wi-Fi network '{ssid}'...". 
# ■ On success, prints "Connected successfully!". 
# ○ Example implementation for control_via_app(command): 
# ■ Prints "Executing command: {command} via app.". 
# 3. Do not make a refrigerator a smart appliance. #

