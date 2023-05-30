from lxml import etree
import os
import argparse
import re

#################### FUNCTIONS ##############################

def add_word_to_xml_path(inputPath, RenamedPart):
    # Define the pattern to match ".xml" at the end of the string
    pattern = r"\.xml$"

    # Perform a case-insensitive search and replace using regex
    newPath = re.sub(pattern, f"_{RenamedPart}.xml", inputPath, flags=re.IGNORECASE)

    # Return the updated path
    return newPath


def getArgs():
    # Create an argument parser
    parser = argparse.ArgumentParser(description="Process a file.")

    # Add an argument for the input file
    parser.add_argument("inputFile", help="Path to the input file")

    # Parse the command-line arguments
    args = parser.parse_args()

    return args

def fileExist(path):
    # Check if the file exists
    if not os.path.exists(path):
        print("The file does not exist.")
    else:
        # Try to open the file
        try:
            with open(path) as f:
                print("The file can be opened.")
        except OSError as e:
            print(f"The file cannot be opened: {e}")

def setLocalDirectory():
    # Get the absolute path of the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Change the current working directory
    os.chdir(script_dir)

#####################   MAIN   ################################

if __name__ == "__main__":

    # Parse the command-line arguments
    args = getArgs()
    input_path = args.inputFile

    print("Processing file:", input_path)

    output_path = add_word_to_xml_path(input_path, "pretty")

    # Get the absolute path of the directory of the current script
    setLocalDirectory()

    # Check if file exist
    fileExist(input_path)

    # Parse the XML file
    tree = etree.parse(input_path)

    print("encoding of input and output files: {}".format(tree.docinfo.encoding))
    # Write the parsed tree back out with pretty printing
    tree.write(output_path, pretty_print=True, xml_declaration=True, encoding=tree.docinfo.encoding)

    print("document {} created !".format(output_path))
