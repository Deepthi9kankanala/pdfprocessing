import sys #used for systC:/Users/dell/Desktop/pdf/GPS.pdfem-specific parameters and functions.
from PyPDF2 import PdfReader
import os # provides operating system dependent functionality for creating directories (os.makedirs) and checking if directories exist (os.path.exists).

# Create a directory for saving the output images
output_dir = "C:/Users/dell/Desktop/pdf/extractedimgs"
os.makedirs(output_dir, exist_ok=True) #exist_ok=True argument ensures that the directory is created if it doesn't already exist.

pdfreader = PdfReader("C:/Users/dell/Desktop/pdf/GPS.pdf")
#extractingimages
first_page = pdfreader.pages[0] #frst page of pdf
count = 0 #to keep track of num of extraced images
for image_file in first_page.images: #iterates over each image found
    with open(output_dir + str(count) + image_file.name, "wb") as fp: #for each img opens a new file in binary write mode
        # original image file name (str(count) + image_file.name).
        fp.write(image_file.data)
        print(f"Image file {count}: {str(count) + image_file.name}")
        #prints a message indicating the name of the extracted image file
        sys.stdout.flush() #lushes the standard output buffer to ensure that the print statement is immediately visible in the console
        count += 1
