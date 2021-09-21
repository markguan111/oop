import HW2_CarClass as CC

year_model = 488
make = 'porsche'
#speed = print("your current speed is 0")

Car1 = CC.Car(year_model,make)

n = 0 
while n < 5:
    Car1.accelerate()
    print("The current speed is:",Car1.get_speed())
    n += 1

i = 0
while i < 5:
    Car1.brake()
    print("The current speed is:",Car1.get_speed())
    i += 1

