class Car(object):
	def __init__(self, price, speed, fuel, mileage):
		self.price = price
		self.speed = speed
		self.fuel = fuel
		self.mileage = mileage
		if (price > 10000):
			self.tax = 0.15
		else:
			self.tax = 0.12
	
	def display_all(self):
		return '${}, {}mph, {}gal, {}mpg, {}% tax'.format(self.price, self.speed, self.fuel, self.mileage, int(self.tax * 100))

car = Car(35000, 200, 20, 100)
print car.display_all()

car = Car(30000, 160, 15, 96)
print car.display_all()

car = Car(33000, 220, 20, 100)
print car.display_all()

car = Car(25000, 222, 22, 112)
print car.display_all()

car = Car(2, 1, 0.001, 1000)
print car.display_all()

