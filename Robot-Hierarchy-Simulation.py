from abc import abstractmethod
class Robot:
    __battery_level=0
    def __init__(self,name,battery_level):
        self.name=name
        self.setBattery_level(battery_level)
    def status(self):
        print(self.name," ,battery level :",self.__battery_level," %")
    @abstractmethod
    def move(self):
        pass
    def getBattery_level(self):
        return self.__battery_level
    def setBattery_level(self,battery_level):
        self.__battery_level=battery_level
class GroundRobot(Robot):
    def __init__(self,name,battery_level,wheels):
        super().__init__(name,battery_level)
        self.wheels=wheels
    def move(self):
        print(self.name," is moving on ",self.wheels," wheels")
class AerialRobot(Robot):
    def __init__(self,name,battery_level,rotors):
        super().__init__(name,battery_level)
        self.rotors=rotors
    def move(self):
        print(self.name," is flying with ",self.rotors," rotors")
class FleetManagement:
    def __init__(self,robot):
        self.robot=robot
    def moveRobot(self):
        self.robot.move()
    def statusRobot(self):
        self.robot.status()
GroundBot=GroundRobot("GroundBot",90,4)
AirBot=AerialRobot("AirBot",85,6)
F1=FleetManagement(GroundBot)
F2=FleetManagement(AirBot)
F1.moveRobot()
F2.moveRobot()
F1.statusRobot()
F2.statusRobot()