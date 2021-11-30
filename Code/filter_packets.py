#!/usr/bin/python3
import sys


def filter():
	# Filter the raw text file (Node*.txt) so that only ICMP Echo Requests and Replies show
	print("Filtering Packets...")
	for i in [1, 2, 3, 4]:
		print("		Filtering File " + str(i) + "...")
		# Open The files
		file = open(sys.path[0]+"/../Captures/Node" + str(i) + ".txt", "r")
		loop = True

		while loop is True:
			line1 = file.readline()  # Metric Headers
			# If the file is no more
			if line1 == "\n" or line1 == '':
				loop = False

			line2 = file.readline()  # Metrics
			line3 = file.readline()  # Empty line

			# FILTER THROUGH THE DATA
			all_data = ''
			data = True
			while data is not False:
				# Read in the data
				data_line = file.readline()
				all_data += data_line
				if data_line == "\n" or data_line == '':
					data = False  # End the loop

			# OUTPUT ECHO REQUESTS AND REPLIES
			# Continue only if the Metrics line includes ICMP Echo Requests and Replies
			if "ICMP" in line2 and "(ping)" in line2 and "Echo" in line2:
				if "request" in line2 or "reply" in line2:
					# Put the Filtered packet into its own output file (Node*_filtered.txt)
					output_file = open(sys.path[0]+"/../Captures/Node" + str(i) + "_filtered.txt", "a")
					output_file.write(line1)
					output_file.write(line2)
					output_file.write(line3)
					output_file.write(all_data)
	# Close files
	file.close()
	output_file.close()
