""" Software for Image processing """

from PIL import Image
import os
import processor
from sys import exit
import utility


def _select_image():
	""" Takes image path as input. """
	
	filename = input("Enter file name : ")
	try:
		file_path = os.path.join(os.getcwd(), filename)
		user_image = Image.open(file_path)
	except:
		print("Image not found")
		exit(1)
	else:
		processor.Picture(user_image)


if __name__ == "__main__":
	
	try :
		_select_image()
	except KeyboardInterrupt:
		utility.trigger_exit()