class Bike(object):
	def __init__(self, price, max_speed):
		self.price = price
		self.max_speed = max_speed
		self.miles = 0

	def displayInfo(self):
		print 'Bike price: $' + str(self.price) + ', max speed: ' + str(self.max_speed) + ', miles: ' + str(self.miles)
		return self

	def ride(self):
		print 'Riding'
		self.miles += 10
		return self

	def reverse(self):
		print 'Reversing'
		self.miles -= 5
		if self.miles < 0:
			self.miles = 0
		return self


bike1 = Bike(1000, 50)

for i in range(3):
	bike1.ride()

bike1.reverse().displayInfo()

bike2 = Bike(1500, 55)
bike2.ride().ride().reverse().reverse().displayInfo()

bike3 = Bike(2000, 69)
for i in range(3):
	bike3.reverse()

bike3.displayInfo()