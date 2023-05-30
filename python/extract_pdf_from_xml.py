import base64
import xml.etree.ElementTree as ET

# Parse the XML file
tree = ET.parse('input.xml')

# Find the Base64 string
root = tree.getroot()
base64_string = root.find('./xpathrequest').text

# Decoding the Base64 string
decoded_bytes = base64.b64decode(base64_string)

# Writing to a file
with open("output.pdf", "wb") as f:
    f.write(decoded_bytes)
