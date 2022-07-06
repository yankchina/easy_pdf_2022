# encoding: utf-8
import glob
import os
from typing import Tuple

Rect  = Tuple[int, int, int, int]

def rectangle_inside(rect1:Rect,rect2:Rect):
    if rect1[0] >= rect2[0] and rect1[1] >= rect2[1] and rect1[2] <= rect2[2] and rect1[3] <= rect2[3]:
        return True
    else:
        return False
    
def get_rectangle_coordinates(page_size: Tuple, margin_conf:Tuple) -> Rect:
    page_width, page_height = page_size
    x1 = round(margin_conf[0] * page_width)
    x2 = round(page_width - margin_conf[2] * page_width) + 1
    y1 = round(margin_conf[1] * page_height)
    y2 = round(page_height - margin_conf[3] * page_height) + 1
    return (x1, y1, x2, y2)

def get_all_pdf_files(path: str) -> list:
    return glob.glob(os.path.join(path, "*.pdf"))

def get_output_file_path(pdf_file: str) -> str:
    pdf_file_path = os.path.abspath(pdf_file)
    pdf_file_name = os.path.basename(pdf_file)
    text_file_name = pdf_file_name.replace(".pdf", ".txt")
    text_file_path = os.path.join(os.path.dirname(pdf_file_path), text_file_name)
    return text_file_path