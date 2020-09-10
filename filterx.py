from PIL import ImageFilter

class Filter:

	def __init__(self, image):
		self.image = image
		self.Options()


	def Options(self):
		print()
		print("-------------------")
		print("   Select Choice ")
		print("-------------------")
		print("1-> Edge Enhance")

		choice = int(input("choice : "))
		if choice < 1 or choice > 1:
			raise ValueError
		else:
			self._filter_controller(choice)

	def _filter_controller(self, choice):
		if choice == 1:
			self._Blur()

	def _Blur(self):
		self.image = self.image.filter(ImageFilter.EDGE_ENHANCE)
		self.image.show()