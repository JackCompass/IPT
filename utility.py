def savechanges():
		try:
			flag = int(input("Process change : "))
		except ValueError:
			print("Invalid input to filter.")
		else:
			return flag

def apply_kernel():
		print("Available Kernel") 
		print("1 : Sharpen") # (0, -1, 0, -1, 5, -1, 0, -1, 0)
		print("2 : Identity") # (0, 0, 0, 0, 1, 0, 0, 0, 0)
		print("3 : Outline") # (-1 -1 -1 -1 8 -1 -1 -1 -1)
		print("4 : Blur") # (0.0625 0.125 0.0625 0.125 0.25 0.125 0.0625 0.125 0.0625)
		print("5 : Emboss") # (-2, -1, 0, -1, 1, 1, 0, 1, 2)
		print("6 : Left Sobel") # (1 0 -1 2 0 -2 1 0 -1)
		print("7 : Right Sobel") # (-1 0 1 -2 0 2 -1 0 1)
		print("8 : Top Sobel") # (1 2 1 0 0 0 -1 -2 -1)
		print("9 : Bottom Sobel") # (-1 -2 -1 0 0 0 1 2 1)
		print("10 : Manual Kernel") 

		choice = int(input("Choice : "))
		if choice < 1 or choice > 10:
			raise ValueError
		else:
			if choice == 1:
				sharpen = [0, -1, 0, -1, 5, -1, 0, -1, 0]
				return sharpen
			elif choice == 2:
				identity = [0, 0, 0, 0, 1, 0, 0, 0, 0]
				return identity
			elif choice == 3:
				outline = [-1, -1, -1, -1, 8, -1, -1, -1, -1]
				return outline
			elif choice == 4:
				blur = [0.0625, 0.125, 0.0625, 0.125, 0.25, 0.125, 0.0625, 0.125, 0.0625]
				return blur
			elif choice == 5:
				emboss = [-2, -1, 0, -1, 1, 1, 0, 1, 2]
				return emboss
			elif choice == 6:
				left_sobel = [1, 0, -1, 2, 0, -2, 1, 0, -1]
				return left_sobel
			elif choice == 7:
				right_sobel = [-1, 0, 1, -2, 0, 2, -1, 0, 1]
				return right_sobel
			elif choice == 8:
				top_sobel = [1, 2, 1, 0, 0, 0, -1, -2, -1]
				return top_sobel
			elif choice == 9:
				bottom_sobel = [-1, -2, -1, 0, 0, 0, 1, 2, 1]
				return bottom_sobel
			elif choice == 10:
				manual_kernel = list(input("Enter kernel : ").split(" "))
				kernel = [int(x) for x in manual_kernel]
				if not len(kernel) == 9:
					raise ValueError("Input must be a list of 9 values")

				return kernel

def check(size):
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
			if not 0 <= size1D <= 265:
				raise ValueError("Size should be in [0, 265] range.")
		return size