from PIL import ImageFilter
import random
import utility

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
		print("2-> Distortion")
		print("3-> Gaussian Blur")
		print("4-> Kernel")


		choice = int(input("choice : "))
		if choice < 1 or choice > 4:
			raise ValueError
		else:
			self._filter_controller(choice)

	def _filter_controller(self, choice):
		if choice == 1:
			self._Blur()
		elif choice == 2:
			self.Distortion()
		elif choice == 3:
			self.gaussian()
		elif choice == 4:
			self.kernel()

	def _Blur(self):
		self.image.filter(ImageFilter.EDGE_ENHANCE).show()
		if utility.savechanges():
			self.image = self.image.filter(ImageFilter.EDGE_ENHANCE)
		self.Options()

	def Distortion(self):
		size = list(input("Enter 3DLUT values : ").split(" "))
		table_size = self._check_size(size)
		total = 1
		for num in table_size:
			total *= num
		while True:
			table = [round(random.random(), 2) for i in range(0, 3 * total)]
			self.image.filter(ImageFilter.Color3DLUT(table_size, table)).show()
			if utility.savechanges():
				self.image = self.image.filter(ImageFilter.Color3DLUT(table_size, table))
			check = int(input("Enter 0 for exit : "))
			if not check:
				break
		self.Options()

	def _check_size(self, size):
		try:
			_, _, _ = size
		except ValueError as e:
			raise ValueError(
				"Size should be either an integer or a tuple of three integers."
			) from e
		except TypeError:
			size = (size, size, size)
		size = [int(x) for x in size]
		for size1D in size:
			if not 2 <= size1D <= 65:
				raise ValueError("Size should be in [2, 65] range.")
		return size

	def gaussian(self):
		radius = int(input("Radius : "))
		self.image.filter(ImageFilter.GaussianBlur(radius)).show()
		if utility.savechanges():
			self.image = self.image.filter(ImageFilter.GaussianBlur(radius))
		self.Options()

	def kernel(self):
		kernel = utility.apply_kernel()
		self.image.filter(ImageFilter.Kernel((3,3), kernel)).show()
		if utility.savechanges():
			self.image = self.image.filter(ImageFilter.Kernel((3,3), kernel))
		self.Options()

