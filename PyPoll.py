# Import the datetime class from the datetime module.
import datetime
# Use the now() attribute on the datetime class to get the present time.
now = datetime.datetime.now()
# Print the present time.
print("The time right now is ", now)


# Import the datetime class from the datetime module.
import datetime as dt
# Use the now() attribute on the datetime class to get the present time.
now = dt.datetime.now()
# Print the present time.
print("The time right now is ", now)

# import csv file
import csv
dir(csv)

# The dir() function will return all the functions available on that variable.
dir({'Arapahoe': 422829, 'Denver': 463353, 'Jefferson': 432438})

# A data type, like str. The dir() function will return all the attributes and methods that can be used with the str data type.
dir(str)
dir(int)
dir(float)
dir(bool)
dir(list)
dir(tuple)
dir(dict)
dir(datetime)
dir(random)
dir(numpy)


# Assign a variable for the file to load and the path.
file_to_load = 'Resources/election_results.csv'

# Open the election results and read the file.
election_data = open(file_to_load, 'r')

# To do: perform analysis.

# Close the file.
election_data.close()

# Open the election results and read the file
with open(file_to_load) as election_data:

     # To do: perform analysis.
     print(election_data)

# Indirect path to the file
import os
dir(os)

dir(os.path)


import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Open the election results and read the file.
with open(file_to_load) as election_data:

# Print the file object.
     print(election_data)

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file.
open(file_to_save, "w")
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Use the open statement to open the file as a text file.
outfile = open(file_to_save, "w")
# Write some data to the file.
outfile.write("Hello World")
# Close the file
outfile.close()

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

# Write some data to the file.
 txt_file.write("Hello World")
# Write three counties to the file.
 txt_file.write("Arapahoe")
 txt_file.write("Denver")
 txt_file.write("Jefferson")

 # To separate "Arapahoe" and "Denver" by a comma and space, we need to add them to the end of the county name in the write() function as follows:
 # Write three counties to the file.
 with open(file_to_save, "w") as txt_file:
     txt_file.write("Hello World, ")
     txt_file.write("Arapahoe, ")
     txt_file.write("Denver, ")
     txt_file.write("Jefferson")

# Another method to write to a file
# To separate "Arapahoe" and "Denver" by a comma and space, we need to add them to the end of the county name in the write() function as follows:
 # Write three counties to the file.

# Another method to write three counties to the file.
with open(file_to_save, "w") as txt_file:
     txt_file.write("Arapahoe, Denver, Jefferson")

# Another method to write three counties to the file.
with open(file_to_save, "w") as txt_file:
     txt_file.write("Arapahoe\nDenver\nJefferson\n")


# Skiil Drill
with open(file_to_save, "w") as txt_file:
     txt_file.write("Counties in the election\n ---------------------\nArapahoe\nDenver\nJefferson\n")

# 3.4.4 Read the Election Results
# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Open the election results and read the file.
with open(file_to_load) as election_data:
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
# To do: read and analyze the data here.

# Print each row in the CSV file.
    for row in file_reader:
     print(row)

# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
    print(headers)

# 3.4.5 commit your code



