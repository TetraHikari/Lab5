
#create Abstract transportation class which has 3 properties start_place, end_place, distance

from abc import ABC, abstractmethod

class Transportation(ABC):
    def __init__(self, start_place, end_place, distance):
        self.start_place = start_place
        self.end_place = end_place
        self.distance = distance

    @abstractmethod
    def calculate_fare(self):
        pass

#Menth:Train class
class Train(Transportation):
    def calculate_fare(self):
        total_station = self.end_place - self.start_place
        return total_station * 5
    

    
    