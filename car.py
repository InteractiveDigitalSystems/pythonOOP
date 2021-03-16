from engine import Engine
from vehicle import Vehicle

class Car (Vehicle):
    def __init__(self, licensePlate="", color="", numberOfSeats=0):
        self.engine = Engine()
        self.licensePlate = licensePlate

    def start(self):
        print('start')
    
    def stop(self):
        self.engine.stop()

    
    def drive(self):
        self.engine.drive()