import fitz

# Open the PDF document
doc = fitz.open("C:/Users/dell/Desktop/pdf/registration.pdf")

# Open the image file
image_file = "C:/Users/dell/Desktop/pdf/wsulogo.png"

# Iterate through each page of the document
for page_number in range(len(doc)):
    page = doc.load_page(page_number)
    # Define the rectangle where you want to insert the image (adjust as needed)
    page_width = page.rect.width
    page_height = page.rect.height
   
    img_width = 40
    img_height =50
    x0 = page_width - img_width - 100  # 20 points margin from the right edge
    y0 = page_height - img_height - 10  # 20 points margin from the top edge
    rect = fitz.Rect(x0, y0, x0 + img_width, y0 + img_height)

    # Insert the image into the page
    page.insert_image(
        rect,
        filename=image_file,
        rotate=0  # No rotation
    )
   

# Save the modified document
doc.save("insertimg.pdf")
doc.close()