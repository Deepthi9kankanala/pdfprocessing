import fitz  # import package PyMuPDF

# Open input PDF 
doc = fitz.open("C:/Users/dell/Desktop/pdf/GPS.pdf")

# Loop through all pages in the document
for page_number in range(len(doc)):
    # Load current page
    page = doc.load_page(page_number)

    # Search for "are" on the current page, results in a list of rectangles
    rects = page.search_for("potholes")

    # Mark all occurrences in one go
    page.add_highlight_annot(rects)

# Save the document with these changes
doc.save("C:/Users/dell/Desktop/pdf/Highlighting.pdf")
