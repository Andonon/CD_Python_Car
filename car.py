'''Car assignment at Coding Dojo for Python basics. 
by: Troy Center, troycenter1@gmail.com, Coding Dojo Python fundamentals, June 2017
'''
#pylint: disable=C0103
class Car(object):
    '''This is a class for the Car assignment in Python fundamentals.
    '''
    def __init__(self, price, speed, fuel, mileage, tax=0.12):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if self.price > 10000:
            self.tax = 0.15
        else:
            self.tax = tax

    def display_all(self):
        '''This function will display the car detail in a string, human readable.
        '''
        print "Price: ", self.price
        print "Speed: ", self.speed
        print "Fuel: ", self.fuel
        print "Mileage: ", self.mileage
        print "Tax: ", self.tax
        return self

car1 = Car(2000, "25mph", "Full", "15mpg")
car1.display_all()
car2 = Car(2000, "5mph", "Not Full", "105mpg")
car2.display_all()
car3 = Car(2000, "15mph", "King of Full", "95mpg")
car3.display_all()
car4 = Car(2000, "25mph", "Full", "25mpg")
car4.display_all()
car5 = Car(2000, "45mph", "Empty", "25mpg")
car5.display_all()
car6 = Car(20000000, "35mph", "Empty", "15mpg")
car6.display_all()


