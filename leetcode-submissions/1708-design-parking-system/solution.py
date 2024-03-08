class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.medium = medium
        self.small = small
        self.big_current = 0
        self.medium_current = 0
        self.small_current = 0
        

    def addCar(self, carType: int) -> bool:
        match carType:
            case 1:
                if (self.big_current + 1 <= self.big):
                    self.big_current += 1
                    return True
                
            case 2:
                if (self.medium_current + 1 <= self.medium):
                    self.medium_current += 1
                    return True
            
            case 3:
                if (self.small_current + 1 <= self.small):
                    self.small_current += 1
                    return True
        
        return False
                
                
        


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
