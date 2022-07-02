# encoding: utf-8
from easy_pdf import get_page_size,pdf_convert_text_with_margin_percentage
import fitz

pdf = fitz.open("test.pdf")
page = pdf[0]
page_width, page_height = get_page_size(page)
print(page_width, page_height)
pdf_convert_text_with_margin_percentage("test.pdf", "test.txt", 0.1)
