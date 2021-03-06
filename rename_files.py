from os import listdir, rename, getcwd, chdir
from shutil import copy

def rename_files():
	# Get file names from a folder, change this path to your dir
	file_list = listdir("/home/kibe/Django/Python/Udacity/rename_files/udacity-prank/prank")
	# print (file_list)

	# Rename each file in file_list using the translate string method
	# First get the current working dir
	this_dir = getcwd()
	# Now change the dir to the dir with files
	chdir("/home/kibe/Django/Python/Udacity/rename_files/udacity-prank/prank")
	
	for file_name in file_list:
		
		rename(file_name, file_name.translate(file_name.maketrans("0123456789", "          "))) # To avoid ValueError: the first two maketrans arguments must have equal length
		print (file_name)
	# Go back to our working dir
	chdir(this_dir)

	

rename_files()