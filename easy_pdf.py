# enconding: utf-8
from typing import Tuple, Any
import fitz
import codecs

Rect  = Tuple[int, int, int, int]


def get_page_size(page:Any) -> Tuple[int, int]:
    return page.rect.width, page.rect.height

def rectangle_inside(rect1:Rect,rect2:Rect):
    if rect1[0] >= rect2[0] and rect1[1] >= rect2[1] and rect1[2] <= rect2[2] and rect1[3] <= rect2[3]:
        return True
    else:
        return False

def extract_text_inside_page_rectangle(page:Any, page_index:int, rectangle_coordinates:Rect) -> str:
    return_string = u""
    blocks = page.get_text("blocks")
    for index, block in enumerate(blocks):
        if block[-1] == 0:
            block_rect = (int(block[0]), int(block[1]), int(block[2]), int(block[3]))
            if rectangle_inside(block_rect, rectangle_coordinates):
                return_string += block[4]
    return return_string

def extract_text_one_page(pdf_object:Any, pdf_page_index:int, rectangle_coordinates:Rect) -> str:
    return_string = u""
    try:
        page = pdf_object[pdf_page_index]
        ## 查看一下范围是否超越了页面范围
        if not rectangle_inside(rectangle_coordinates, (0, 0, page.rect.width, page.rect.height)):
            raise Exception("rectangle_coordinates out of page range")
        return_string = extract_text_inside_page_rectangle(page, pdf_page_index, rectangle_coordinates)
    except Exception as e:
        print(e)
    else:
        pass
    finally:
        return return_string
    

def extract_text_all_pages(pdf_object:Any, rectangle_coordinates:Rect) -> str:
    return_string = u""
    index = 0
    for page in pdf_object:
        return_string += extract_text_one_page(pdf_object, index, rectangle_coordinates)
        index += 1
    return return_string


def pdf_convert_text(pdf_file_name:str, text_file_name:str, rectangle_coordinates:Rect) -> None:
    pdf_object = fitz.open(pdf_file_name)
    file_text_string = extract_text_all_pages(pdf_object, rectangle_coordinates)
    with codecs.open(text_file_name, "w", "utf-8") as f:
        f.write(file_text_string)
    print("convert pdf to text success")
    
def pdf_convert_text_with_margin_percentage(pdf_file_name:str, text_file_name:str, margin_percentage:float) -> None:
    pdf_object = fitz.open(pdf_file_name)
    page_width, page_height = get_page_size(pdf_object[0])
    rectangle_coordinates = (int(page_width * margin_percentage), int(page_height * margin_percentage), int(page_width * (1 - margin_percentage)), int(page_height * (1 - margin_percentage)))
    pdf_convert_text(pdf_file_name, text_file_name, rectangle_coordinates)
    pass

def display_pdf_text_one_page(pdf_file_name:str, page_index:int) -> None:
    pdf_object = fitz.open(pdf_file_name)
    page = pdf_object[page_index]
    for box in page.get_text("blocks"):
        if box[-1] == 0: ##<- 0 is text, 1 is image, 2 is line
            print(box[0:5])
    pass