# #encapsulation
class Phone:
    __battery="30%"
    def printbattery(self):
        print(self.__battery)
iphone15=Phone()
iphone15.printbattery()