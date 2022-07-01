# enconding: utf-8
from typing import Tuple, Any
import fitz

Rect  = Tuple[int, int, int, int]

def rectangle_inside(rect1:Rect,rect2:Rect):
    if rect1[0] >= rect2[0] and rect1[1] >= rect2[1] and rect1[2] <= rect2[2] and rect1[3] <= rect2[3]:
        return True
    else:
        return False

def extract_text_inside_page_rectangle(page:Any, page_index:int, rectangle_coordinates:Rect) -> str:
    return_string = u""
    blocks = page.getText("blocks")
    for index, block in enumerate(blocks):
        if block[-1] == 0:
            block_rect = (int(block[0]), int(block[1]), int(block[2]), int(block[3]))
            if rectangle_inside(block_rect, rectangle_coordinates):
                return_string += block[4]
    return return_string

def extract_text_one_page(pdf_file_name:str, pdf_page_index:int, rectangle_coordinates:Rect) -> str:
    return_string = u""
    try:
        pdf = fitz.open(pdf_file_name)
        page = pdf[pdf_page_index]
        ## 查看一下范围是否超越了页面范围
        if not rectangle_inside(rectangle_coordinates, (0, 0, page.rect.width, page.rect.height)):
            raise Exception("rectangle_coordinates out of page range")
        return_string = extract_text_inside_page_rectangle(page, pdf_page_index, rectangle_coordinates)
    except Exception as e:
        pass
    else:
        pass
    finally:
        return return_string
    
    
if __name__ == '__main__':
    pdf_file_name = "./test.pdf"
    rect = (80,100,510,730)
    value_string = extract_text_one_page(pdf_file_name, 2, rect)
    print(value_string)