from PIL import Image

class Picture:

	def __init__(self, image):
		self.image = image
		self.current_size = image.size
		self.options()
		

	def options(self):
		print()
		print("-------------------")
		print("   Select Choice ")
		print("-------------------")
		print("1-> Rotate")
		print("2-> Resize")
		print("3-> Spread Effect")
		print("4-> Save")


		choice = int(input("choice : "))
		if choice < 1 or choice > 4:
			raise ValueError
		else:
			self._image_controller(choice)

	def _image_controller(self, choice):
		if choice == 1:
			self.rotate()
		elif choice == 2:
			self.resize()
		elif choice == 3:
			self.spread_effect()
		elif choice == 4:
			self.save()

	def save():
		filename = input("Save File as (filename) : ")
		self.save(filename, format = 'jpeg')
		self._image_controller()

	def rotate(self):
		try:
			rotate_angle = int(input("Roation Angle : "))
		except ValueError:
			print("Invalid input")
		else:
			self.image.rotate(rotate_angle).show()
			self.options()

	def resize(self):
		print(f"Original Size : {self.current_size}")
		height, width = input("Enter resize size : ").split(" ")
		size = (int(width), int(height))
		self.image.resize(size, resample = 3).show()
		self.options()

	def spread_effect(self):
		spread_distance = int(input("Spread Effect : "))
		self.image.effect_spread(spread_distance).show()
		self.options()
