from pdf2docx import Converter

pdf_file = 'C:\\Users\\Furkan\\Downloads\\Lecture10 (1).pdf'
docx_file = 'sample1.docx'

cv = Converter(pdf_file)
cv.convert(docx_file)
cv.close()