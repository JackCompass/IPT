from PIL import ImageFilter, ImageOps, Image
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
		print("5-> MinFilter")
		print("6-> Greyscale")
		print("7-> Solarize")
		print("8-> Black & White")
		print("9-> Sepia")
		choice = int(input("choice : "))
		if choice < 1 or choice > 9:
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
		elif choice == 5:
			self.minfilter()
		elif choice == 6:
			self.greyscale()
		elif choice == 7:
			self.Solarize()
		elif choice == 8:
			self.blackwhite()
		elif choice == 9:
			self.sepia()

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

	def minfilter(self):
		self.image.filter(ImageFilter.MinFilter(size = 3)).show()
		if utility.savechanges():
			self.image = self.image.filter(ImageFilter.MinFilter(size = 3))
		self.Options()

	def greyscale(self):
		cutoff = int(input("cutoff : "))
		ImageOps.autocontrast(self.image, cutoff).show()
		if utility.savechanges():
			self.image = ImageOps.autocontrast(self.image, cutoff)
		self.Options()

	def Solarize(self):
		threshold = int(input("Threshold : "))
		ImageOps.solarize(self.image, threshold).show()
		if utility.savechanges():
			self.image = ImageOps.Solarize(self.image, threshold)
		self.Options()

	def blackwhite(self):
		copy_image = self.image.copy()
		pixel = copy_image.load()
		for x in range(copy_image.width):
			for y in range(copy_image.height):
				color = pixel[x, y]
				avg_color = color[0] + color[1] + color[2]
				pixel[x, y] = (avg_color, avg_color, avg_color)

		copy_image.show()
		if utility.savechanges():
			self.image = copy_image
		self.Options()

	def sepia(self):
		copy_image = self.image.copy()
		pixel = copy_image.load()	
		for x in range(copy_image.width):
			for y in range(copy_image.height):
				color = pixel[x, y]
				avg_red = int((.393 * color[0]) + (.769 * color[1]) + (.189 * color[2]))
				avg_green = int((.349 * color[0]) + (.686 * color[1]) + (.168 * color[2]))
				avg_blue = int((.272 * color[0]) + (.534 * color[1]) + (.131 * color[2]))
				pixel[x, y] = (avg_red, avg_green, avg_blue)

		copy_image.show()
		if utility.savechanges():
			self.image = copy_image
		self.Options()