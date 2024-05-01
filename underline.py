import fitz
from fitz.utils import draw_line

# Open the PDF document
doc = fitz.open("C:/Users/dell/Desktop/pdf/GPS.pdf")

# Search text
search_text = "systems"

# Loop through each page of the document
for page in doc:
    # Get the text of the page
    text = page.get_text()

    # Get all occurrences of the search text on the page
    matches = page.search_for(search_text)

    # Loop through each occurrence of the search text
    for bbox in matches:
        # Get the bounding box of the word
        x0, y0, x1, y1 = bbox

        # Draw a line beneath the word
        draw_line(page, (x0, y1 + 2), (x1, y1 + 2), color=(0, 0, 1), width=1)

# Save the modified document
doc.save("C:/Users/dell/Desktop/pdf/underlinee.pdf")
doc.close()
