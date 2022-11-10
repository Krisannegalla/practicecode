class GasStation:
  def __init__(self, vehicle, fuel):
    self.vehicle = vehicle
    self.fuel = fuel

class Vehicle(GasStation):
  def __init__(self, vehicle, fuel, quantity):
    super().__init__(vehicle, fuel)
    self.quantity = quantity

  def gasBill(self):
    limit = 30
    php_None = "Php None"
    diesel = 92.50
    gasoline = 97.24
    if self.fuel == "Gasoline" and self.quantity <= 30:
      print("Total Amount: " + str(gasoline * self.quantity))
    if self.fuel == "Diesel" and self.quantity <= 30:
      print("Total Amount: " + str(diesel * self.quantity))
    if self.quantity > limit:
      print("Fuel Limit is 30 Liters")
      print("Total Amount: " + php_None)
    
myHonda = Vehicle("Honda CR-V", "Gasoline", 20)
print("Vehicle: " + myHonda.vehicle + ", " + "Fuel: " + myHonda.fuel + ", " + "No.Liters: " + str(myHonda.quantity))
myHonda.gasBill()

print("\n")

myToyota = Vehicle("Toyota Corolla", "Diesel", 30)
print("Vehicle: " + myToyota.vehicle + ", " + "Fuel: " + myToyota.fuel + ", " + "No.Liters: " + str(myToyota.quantity))
myToyota.gasBill()

print("\n")


myKia = Vehicle("Kia Sorento", "Gasoline", 26)
print("Vehicle: " + myKia.vehicle + ", " + "Fuel: " + myKia.fuel + ", " + "No.Liters: " + str(myKia.quantity))
myKia.gasBill()
