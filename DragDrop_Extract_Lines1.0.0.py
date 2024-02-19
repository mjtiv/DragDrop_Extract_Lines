#!/usr/bin/env python3.6

import sys

"""

Program Extracts Lines from a Large File That Normally Crashes Excel 

Will Prompt User for Number of Lines Because Sometimes Files are Very Wide Instead of Very Long

"""



def modify_output_file_name(input_file_name):


    """

    Takes an input file name and examines it for slashes

    : Param input_file_name: Name of file being parsed

    : Return abridged_file_name: Modified File Name for Output

    """

    print ("Examining File Name for Slashes")
    print ("")

    # Check the file for "\"
    if (input_file_name.__contains__("\\")) == True:

        # Split the file name based on the slash
        split_file_name = input_file_name.split("\\")

        # Simplified file name (last value in list)
        simp_file_name = split_file_name[-1]

    # Check the file for "/" (aka Bash or Macs)
    elif (input_file_name.__contains__("//")) == True:

        # Split the file name based on the slash
        split_file_name = input_file_name.split("/")

        # Simplified file name (last value in list)
        simp_file_name = split_file_name[-1]

    # File Name Contains No Slashes
    else:
        simp_file_name = input_file_name

    # Create a New Abridged File Name
    abridged_file_name = "Abridged_" + simp_file_name

    print ("New Abridged File Name:" + abridged_file_name)
    print ("")
    print ("Done Extracting File Name")
    print ("")

    return (abridged_file_name)


def extract_lines_from_file(input_file_name, number_lines_extract):

    """

    Loops over the lines of the file and outputs the requested number

    : Param input_file_name: Name of file being parsed
    : Param number_lines_extract: Number of lines to extract

    : Return NONE:

    """

    # Convert number of lines to a float
    number_lines_extract = float(number_lines_extract)

    # Modify the output file name
    abridged_file_name = modify_output_file_name(input_file_name)

    # Open both files
    input_file = open(input_file_name, 'r')
    output_file = open(abridged_file_name, 'w')

    # Create a counter
    counter = 0

    # Start Looping over the file
    for line in input_file:

        if counter < number_lines_extract:

            # Write the line to file
            output_file.write(line)

            # Add to the counter
            counter += 1
        
        else:
            break

    # Close both files
    input_file.close()
    output_file.close()

    return ()



def main():

    # File Get Dragged and Dropped Onto Program
    input_file_name = sys.argv[1]
    #input_file_name = r"C:\Users\mjtom\Desktop\Parsing_GTF_File\Homo_sapiens.GRCh38.111.gtf"
    #input_file_name = 'Homo_sapiens.GRCh38.111.gtf'



    ##########################################################################
    ######################## DO NOT CHANGE BELOW #############################
    ##########################################################################

    print ("Starting Program")
    print ("")
    print ("")
    print ("")

    print ("Name of File--Full Pathway")
    print (input_file_name)
    print ("")
    print ("")
 
    # Prompt the User for Number of Lines
    number_lines_extract = input("How Many Lines of File Would you like to extract? ")

    # Extracts the Lines from the File and Creates New File
    extract_lines_from_file(input_file_name, number_lines_extract)

    print ("Done Running Program")
    print ("")
    print ("")
    # Create a Prompt to Keep Window Open
    input("Press enter to exit;")

    
main()        


############################### VERSION CONTROL #################################

# DragDrop_Extract_Lines1.0.0.py
# - First working version of code to extract lines from a file








