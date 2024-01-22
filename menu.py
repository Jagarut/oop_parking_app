import sys
from parking import Parking

class Menu:
    def __init__(self) -> None:
        self.parking = Parking()
        self.choices = {
            "P": self.parking.park_car,
            "R": self.retriev_car,
            "D": self.parking.show_park_cars,
            "Q": self.quit
        }

    def display_options(self):
        print("""
              Parking Options:

                P. Park Car
                R. Retrieve Car
                D. Show All Parked Cars
                Q. Quit
              """)
    
    def run(self):
        '''Display options and respond to choices.'''
        while True:
            self.display_options()
            choice = input("What do you want to do: ")
            action = self.choices.get(choice.strip().upper())
            if action:
                action()
            else:
                print(f"{choice} is not a valid choice")

    def retriev_car(self):
        # print(self.parking.show_park_cars())
        try:
            car_number = int(input("What is your car ticket number: "))
        
            if car_number in self.parking.slot1:
                self.parking.return_car(car_number)
            else:
                print("That car is not in our parking lot!")
        except:
            print("We need a number")

    def quit(self):
        print("Thanks for using our parking. Have a nice day!")
        sys.exit(0)

if __name__ == "__main__":
    Menu().run()