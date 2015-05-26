__author__ = 'jeanlouis.mbaka'

import dirsize
import matplotlib.pyplot as plt
import unittest
import sys, getopt


def draw_pie_chart(data_dict):
	"""
	Display directories and files sizes in pie chart.

	:param data_dict: diction of {}
	"""
	labels = [key for key in data_dict.keys()]
	values = [value for value in data_dict.values()]

	colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']
	explode = [0.1] * len(labels)
	plt.pie(values, labels=labels, startangle=90, explode=explode, colors = colors, autopct='%1.1f%%')
	plt.axis('equal')
	plt.show()


if __name__ == "__main__":

	# Read arguments from the second position
	argv = sys.argv[1:]

	target_directory = ""

	try:
		# opts that require argument must be followed by a colon (:) e.g. d:
		opts, args = getopt.getopt(argv, "hd:", ["directory="])
	except getopt.GetoptError:
		# Error: print usage
		print("pie.py -d <directory>")
		sys.exit(2)

	for opt, arg in opts:
		if opt == "-h":
			# Help: print usage
			print("pie.py -d <directory>")
			sys.exit()
		elif opt in ("-d", "--directory"):
			target_directory = arg

	print("Directory is {0}".format(target_directory))

	# Get data & draw
	data_dict = dirsize.get_dir_size(target_directory)
	draw_pie_chart(data_dict)