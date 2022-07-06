# encoding: utf-8
from gooey import Gooey,GooeyParser
from EasyPdf import PdfConvertor

# 建立一个 GUI 窗口
# Create a GUI window
@Gooey (program_name = "PDF to Text", 
        required_cols=1,
        program_description = "Convert PDF to Text With Margin")
def main():
    parser = GooeyParser()
    parser.add_argument("pdf_path", help = "scan directory", widget = "DirChooser")
    parser.add_argument("margin_conf", help = "margin_conf",default='0.1,0.1,0.1,0.1')
    args = parser.parse_args()
    obj = PdfConvertor()
    margin_conf = tuple(map(float,args.margin_conf.split(',')))
    obj.bash_convert_with_margin(args.pdf_path, margin_conf=margin_conf)
    pass

if __name__ == '__main__':
    main()
    pass