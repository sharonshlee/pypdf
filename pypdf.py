"""
pip3 install PyPDF2

Writing a reproduced PDF
1. Following the offical documentation(https://pypdf2.readthedocs.io/en/3.0.0/user/extract-text.html) of PyPDF2,
try to write a code that will extract and print the text from the PDF.

2. Try to extract and print only the text of the third page of the PDF.

3. Create a new PDF file that contains only the first page.

4. The last page of the PDF is rotated by accident.
Save a new pdf file where the last page is rotated back so it’s readable again.

5. Reproduce a new PDF file where all the occurences of the word “demonstrate” to “exhibit”.

6. Reproduce a new PDF with a watermark applied to all of the pages.
Use this watermark PDF. The final output should look like this:
"""
from io import BytesIO

# from PyPDF2 import PdfReader, PdfWriter, PageObject

# reader = PdfReader("resume.pdf")
# 1.
# for page in reader.pages:
#     print(page.extract_text())

# 2.
# print(reader.pages[2].extract_text())

# 3.
# pdf_writer = PdfWriter()
#
# first_page = reader.pages[0]
# pdf_writer.add_page(first_page)
#
# with open('first_page_resume.pdf', 'wb') as resumefile:
#     pdf_writer.write(resumefile)


# 4.
# writer = PdfWriter()
#
# for page in reader.pages:
#     writer.add_page(page)
# writer.pages[-1].rotate(-90)
#
# with open("resume_rotate.pdf", "wb") as fp:
#     writer.write(fp)

# # 5.Reproduce a new PDF file where all the occurences of the word “demonstrate” to “exhibit”.
# from PyPDF2 import PdfReader, PdfWriter
#
# reader = PdfReader("plain_text_pdf/plain_text.pdf")
#
# writer = PdfWriter()
#
# for page in reader.pages:
#     # Update the content in the PDF page object
#     writer.add_page(page.extract_text().replace("Demonstrate", "exhibit"))
#
# with open("resume_replaced.pdf", "wb") as fp:
#     writer.write(fp)

# 6. Reproduce a new PDF with a watermark applied to all of the pages.
# from PyPDF2 import PdfReader, PdfWriter
#
# reader = PdfReader("resume.pdf")
# water_mark_reader = PdfReader("watermark.pdf")
# writer = PdfWriter()
#
# for page in reader.pages:
#     page.merge_page(water_mark_reader.pages[0])
#     writer.add_page(page)
#
# with open("resume_watermarked.pdf", "wb") as file:
#     writer.write(file)


