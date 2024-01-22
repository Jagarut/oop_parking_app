car = 0  
class Parking:
    def __init__(self) -> None:
        self.slot1 = []
        self.slot2 = []

    def park_car(self):
        print("Your car has been parked!")
        global car
        car += 1
        self.slot1.append(car)
        # return the car number. This represents the ticket_number
        return car 

    def return_car(self, tiket_number):
        slot1 = self.slot1
        for i in range(len(slot1)-1, 0, -1): 
            car = slot1[i]
            if car == int(tiket_number):
                break
            self.slot2.append(self.slot1.pop(-1))
        
        # print("slot2:", self.slot2)
        self.slot1.pop(-1)
        # print("slot2:", self.slot2)
       
        for i in range(len(self.slot2), 0, -1):
            self.slot1.append(self.slot2.pop(-1))

    def show_park_cars(self):
        # print("slot1:", self.slot1)
        # print("slot2:", self.slot2)
        print(f"There are {len(self.slot1)} cars in our parking!")
        for car in self.slot1:
            if car:
                print(car, end=" ")
            else:
                print("Currently our parking is empty!")
        print(" ")