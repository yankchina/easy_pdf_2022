# encoding: utf-8
from EasyPdf import PdfConvertor

def main():
    margin_conf = (0.1, 0.1, 0.1, 0.1)
    obj = PdfConvertor()
    obj.convert_with_margin("test.pdf", "test.txt", margin_conf)
    obj.bash_convert_with_margin(".",margin_conf) 
    
    
if __name__ == '__main__':
    main()