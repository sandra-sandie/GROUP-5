#NO.1

class Vechicle:
  def __init__(self,max_speed,mileage):
     self.max_speed = max_speed
     self.mileage = mileage
x = Vechicle(150,200)
print(x.max_speed,x.mileage)

# NO.2

class Vechicle:
     def __init__(self,name,speed,mileage):
         self.name = name
         self.speed = speed
         self.mileage = mileage
class Bus(Vechicle):
     pass
w = Bus("School Volvo",180,12 )
print("Vechicle Name :",w.name,"speed:",w.speed, "mileage:",w.mileage)

#NO.3

class Vechicle:
  def __init__(self,name,max_speed,mileage):
     self.name = name
     self.max_speed = max_speed
     self.mileage = mileage
  def seating_capacity(self,capacity):
   return f"The seating capacity of a {self.name} is {capacity} passengers"
class Bus(Vechicle): 
  def seating_capacity(self,capacity=50):
     return super().seating_capacity(capacity=50)
w = Bus("bus",150,200) 
print(w.seating_capacity())

#NO.4

class Vechicle:
     color = "white" 
     def __init__(self,name,speed,mileage):
         self.name = name
         self.speed = speed
         self.mileage = mileage

class Bus(Vechicle):
     pass

class Car(Vechicle):
     pass
w = Bus("School Volvo",180,12)
print("Color:",w.color,"," ,"Vechicle name:",w.name,"speed:",w.speed,"mileage:",w.mileage)

p = Car("Audi Q5",240,18)
print("Color:",p.color,"," ,"Vechicle name:",p.name,"speed:",p.speed,"mileage",p.mileage)

class Vechicle:
  def __init__(self,name,max_speed,mileage):
      self.name = name
      self.max_speed = max_speed
      self.mileage = mileage

  def Total_Bus_fare(self,Bus_fare):
     return f"Total Bus fare is {Bus_fare}"    
class Bus(Vechicle):
     def Total_Bus_fare(self,Bus_fare=5500.0):
      return super().Total_Bus_fare(Bus_fare=5500.0)

z = Bus("bus",150,200) 
print(z.Total_Bus_fare()) 

#NO.5

class Vechicle:
    def __init__(self,name,mileage,capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self): 
        return self.capacity * 100

class Bus(Vechicle):
    def fare(self):
        total = super().fare()
        total += total * 10 / 100
        return total

school_bus = Bus("School Volvo",12,50)
print("Total Bus fare is:", school_bus.fare())

 


