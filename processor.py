from PIL import Image, ImageOps
import filterx
import utility
import os
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
		print("3-> Crop")
		print("4-> Flip")
		print("5-> Invert")
		print("6-> Mirror")
		print("7-> Add Border")
		print("8-> Merge")
		print("9-> Filter")
		print("10-> Save")

		choice = int(input("choice : "))
		if choice < 1 or choice > 10:
			raise ValueError
		else:
			self._image_controller(choice)

	def _image_controller(self, choice):
		if choice == 1:
			self.rotate()
		elif choice == 2:
			self.resize()
		elif choice == 3:
			self._crop()
		elif choice == 4:
			self.flip()
		elif choice == 5:
			self._invert()
		elif choice == 6:
			self._mirror()
		elif choice == 7:
			self.border()
		elif choice == 8:
			self.merge()
		elif choice == 9:
			filterx.Filter(self.image)
		elif choice == 10:
			self._save()

	def _save(self):
		filename = input("Save File as (filename + extension) : ")
		self.image.save(filename, format = self.image.format)
		self.options()

	def rotate(self):
		try:
			rotate_angle = int(input("Roation Angle : "))
		except ValueError:
			print("Invalid input")
		else:
			self.image.rotate(rotate_angle).show()
			if utility.savechanges():
				self.image = self.image.rotate(rotate_angle)
			self.options()

	def resize(self):
		print(f"Original Size : {self.current_size}")
		height, width = input("Enter resize size : ").split(" ")
		size = (int(width), int(height))
		self.image.resize(size, resample = 3).show()
		if utility.savechanges():
			self.image = self.image.resize(size, resample = 3)
		self.options()

	def _crop(self):
		size = list(input("Enter size (left, upper, right, lower) : ").split(" "))
		size = [int(x) for x in size]
		self.image.crop(size).show()
		if utility.savechanges():
			self.image = self.image.crop(size)
		self.options()

	def _filter(self):
		filterx.Filter(self.image)

	def flip(self):
		ImageOps.flip(self.image).show()
		if utility.savechanges():
			self.image = ImageOps.flip(self.image)
		self.options()

	def _invert(self):
		ImageOps.invert(self.image).show()
		if utility.savechanges():
			self.image = ImageOps.invert(self.image)
		self.options()

	def _mirror(self):
		ImageOps.mirror(self.image).show()
		if utility.savechanges():
			self.image = ImageOps.mirror(self.image)
		self.options()

	def border(self):
		width = int(input("Border width : "))
		color = list(input("Colour : ").split(" "))
		color = tuple(utility.check(color))
		ImageOps.expand(self.image, width, fill = color).show()
		if utility.savechanges():
			self.image = ImageOps.expand(self.image, width, fill = color)
		self.options()

	def merge(self):
		file_name = input("Enter filename : ")
		new_size = list()
		try:
			path = os.path.join(os.getcwd(), file_name)
			join_image = Image.open(path)
		except:
			print("Image not found")
			self.options()
		else:
			if self.image.width < join_image.width:
				new_size.append(self.image.width)
			else:
				new_size.append(join_image.width)
			if self.image.height < join_image.height:
				new_size.append(self.image.height)
			else:
				new_size.append(join_image.height)

			new_image = Image.new("RGB", (2*new_size[0], new_size[1]), (250, 250, 250))
			new_image.paste(self.image.resize(new_size, resample = 3), (0, 0))
			new_image.paste(join_image.resize(new_size, resample = 3), (new_size[0], 0))
			new_image.show()
			if utility.savechanges():
				filename = input("Save File as (filename + extension) : ")
				new_image.save(filename, format = "jpeg")
			self.options()
