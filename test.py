# encoding: utf-8
import glob
import os.path

pdf_files = glob.glob("*.pdf")
print(pdf_files)
for pdf_file in pdf_files:
    pdf_file_path = os.path.abspath(pdf_file)
    pdf_file_name = os.path.basename(pdf_file)
    text_file_name = pdf_file_name.replace(".pdf", ".txt")
    text_file_path = os.path.join(os.path.dirname(pdf_file_path), text_file_name)
    print(text_file_path)
    # pdf_convert_text_with_margin_percentage(pdf_file, pdf_file_name, 0.1)
    pass