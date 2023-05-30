from lxml import etree
import os

#################### FUNCTIONS ##############################

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

# Get the absolute path of the directory of the current script
setLocalDirectory()

xsl_path = "transform.xsl"

# Check if the file exists
fileExist(xsl_path)

# Parse the XSL file
xsl_tree = etree.parse(xsl_path)

# Parse the XML file
xml_tree = etree.parse("input.xml")

# Create a transformer
transform = etree.XSLT(xsl_tree)

# Apply the transformation
result_tree = transform(xml_tree)

# Write the result to a file
result_tree.write("output.xml", pretty_print=True, xml_declaration=True, encoding='UTF-8')
print("done !")


