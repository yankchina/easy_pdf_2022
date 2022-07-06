#!/bin/python3
# encoding: utf-8
import fitz
import codecs
from typing import Any, Tuple
from .utils import *


class PdfConvertor:
    
    def __init__(self) -> None:
        print(u"pdf_convertor.py is loaded")
        pass
    
    def bash_convert_with_margin(self, dir_path:str, margin_conf: Tuple) -> bool:
        dir_path = os.path.abspath(dir_path)
        print(dir_path)
        pdf_files = get_all_pdf_files(dir_path)
        print(pdf_files)
        for pdf_file in pdf_files:
            pdf_file_path = os.path.join(dir_path, pdf_file)
            text_file_path = get_output_file_path(pdf_file)
            print(u"converting {0} -> {1}".format(pdf_file_path,text_file_path))
            self.convert_with_margin(pdf_file_path, text_file_path, margin_conf)
        pass
    
    def convert_with_margin(self, pdf_file_path: str, output_file_path: str, margin_conf: Tuple) -> bool:
        try:
            flag = False
            pdf_object = fitz.open(pdf_file_path)
            lines = []
            page_index = 0
            for page in pdf_object:
                page_size = (page.rect.width, page.rect.height)
                rectangle_coordinates = get_rectangle_coordinates(page_size, margin_conf)
                lines.append(self.__extract_text_inside_rectangle(pdf_object, page_index, rectangle_coordinates))
                page_index += 1
            with codecs.open(output_file_path, "w", encoding="utf-8") as output_file:
                output_file.write("\n".join(lines))
            print(u"convertion success {0}->{1}".format(pdf_file_path, output_file_path))
            flag = True
            return flag
        except Exception as e:
            print(e)
            flag = False
        else:
            flag = False
        finally:
            return flag   # return True if convertion success, otherwise return False
    
    def __extract_text_inside_rectangle(self, pdf_object:Any, page_index:int, rectangle_coordinates:Rect) -> str:
        return_string = u""
        try:
            page = pdf_object[page_index]
            if not rectangle_inside(rectangle_coordinates, (0, 0, page.rect.width, page.rect.height)):
                raise Exception("rectangle_coordinates out of page range")
            blocks = page.get_text("blocks")
            for index, block in enumerate(blocks):
                if block[-1] == 0:
                    block_rect = (int(block[0]), int(block[1]), int(block[2]), int(block[3]))
                    if rectangle_inside(block_rect, rectangle_coordinates):
                        return_string += block[4]
        except Exception as e:
            print(e)
        else:
            pass
        finally:
            return return_string