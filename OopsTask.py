
'''write a python program to create laptop object'''

class laptop():
    def __init__(self,brand,price,model,os):
        self.brand=brand
        self.price=price
        self.model=model
        self.os=os
    def power_on(self):
        print(f"Your laptop is on")
    def shutting_down(self):
        print(f"Your laptop is  shutting down")
    def restart(self):
        print(f"UPDATE your laptop")
    def battery_status(self,level):
        print(f"Your battery level is {level} ")

obj=laptop("HP","65000","RYZEN 3","windows")
obj.power_on()
obj.shutting_down()
obj.restart()
obj.battery_status("55")
print(obj.brand)
print(obj.price)
print(obj.model)
print(obj.os)
