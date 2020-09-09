from PIL import Image

class Picture:

	def __init__(self, image):
		self.image = image
		self.options()

	def options(self):
		print()
		print("-------------------")
		print("   Select Choice ")
		print("-------------------")
		print("1-> rotation")

		choice = int(input("choice : "))
		if choice < 1 or choice > 1:
			raise ValueError
		else:
			self._image_controller(choice)

	def _image_controller(self, choice):
		if choice == 1:
			self.rotation()

	def rotation(self):
		try:
			rotation_angle = int(input("Roation Angle : "))
		except ValueError:
			print("Invalid input")
		else:
			rotated_image = self.image.rotate(rotation_angle)
			rotated_image.show()
