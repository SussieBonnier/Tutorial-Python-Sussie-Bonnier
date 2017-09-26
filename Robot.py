# print(900 * 200 * 1.25 + 100 * 1.06)
# robot_price = 900
# robot_count = 2
# robot_tax = 1.25
# book_price = 100
# book_count = 2
# book_tax = 1.06
# print(robot_price*robot_count*robot_tax+book_price*book_count*book_tax)

# robot={
# "price":900,
# "count":2,
# "tax":1.25,
# }
# print(robot["price"] *robot["count"]*robot["tax"])

class Product:
	price=0
	count=0
	tax=1.25
	def price_with_tax(self):
		return self.price * self.count * self.tax
robot=Product()
robot.price=900
robot.count=1
robot.tax=1.25
book=Product()
book.price=100
book.count=1
book.tax=1.06
# print(robot.price*robot.count*robot.tax+book.price*book.count*book.tax)
 
print(robot.price_with_tax()+book.price_with_tax())