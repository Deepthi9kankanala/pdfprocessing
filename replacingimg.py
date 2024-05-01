import fitz

def img_replace(page, xref, new_image_path):
    # Get the rectangle of the old image
    old_image_rect = page.get_image_rects(xref)
    if not old_image_rect:  # Check if old_image_rect is empty
        print("Error: Old image not found or invalid.")
        return

    # Remove the old image
    page.delete_image(xref)

    # Insert the new image at the same position if the old image rectangle is valid
    if old_image_rect[0].width > 0 and old_image_rect[0].height > 0:  # Access the first rectangle object in the list
        page.insert_image(old_image_rect[0], filename=new_image_path)
    else:
        print("Error: Invalid old image rectangle.")

def replace_image_in_pdf(pdf_path, page_number, xref_list, new_image_path):
    doc = fitz.open(pdf_path)
    page = doc[page_number]  # Page numbers are 0-based in PyMuPDF

    for xref in xref_list:
        # Replace the existing image with the new image
        img_replace(page, xref, new_image_path)

    doc.save("goos.pdf")
    doc.close()

# Example usage:
pdf_path = "education.pdf"
page_number = 0  # Replace with the page number where the image is located
xref_list = [14]  # Replace with the xref of the old image
new_image_path = "newimg.jpg"  # Replace with the path to the new image

replace_image_in_pdf(pdf_path, page_number, xref_list, new_image_path)
