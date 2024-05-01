import fitz
doc = fitz.open("C:/Users/dell/Desktop/pdf/GPS.pdf")  # open some supported document

# iterate over the pages
for page in doc:
    img_number = 0  # for enumerating images per page
    # iterate over the image blocks
    for block in page.get_text("dict")["blocks"]:
        # skip if no image block
        if block["type"] != 1:
            continue
        # build filename, like 'img17-3.jpg'
        name = f"img{page.number}-{img_number}.{block['ext']}"
        out = open(name, "wb")
        out.write(block["image"])  # write the binary content
        out.close()
        img_number += 1  # increase image counter