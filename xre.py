import fitz

def extract_xrefs(pdf_path):
    doc = fitz.open(pdf_path)
    xrefs = []

    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        for img_index in range(len(page.get_images())):
            img = page.get_images()[img_index]
            xrefs.append(img[0])  # Assuming the first element of the tuple is the xref

    doc.close()
    return xrefs

# Example usage:
pdf_path = "C:/Users/dell/Desktop/pdf/education.pdf"
xrefs = extract_xrefs(pdf_path)
print("XREFs found in the PDF:", xrefs)
