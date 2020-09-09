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


		choice = int(input("choice : "))
		if choice < 1 or choice > 2:
			raise ValueError
		else:
			self._image_controller(choice)

	def _image_controller(self, choice):
		if choice == 1:
			self.rotate()
		elif choice == 2:
			self.resize()

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
