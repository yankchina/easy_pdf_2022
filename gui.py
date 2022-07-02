# encoding: utf-8
from email.policy import default
from gooey import Gooey,GooeyParser
from easy_pdf import pdf_convert_text_with_margin_percentage

# 建立一个 GUI 窗口
# Create a GUI window
@Gooey (program_name = "PDF to Text", program_description = "Convert PDF to Text")
def main():
    parser = GooeyParser()
    parser.add_argument("pdf_file_name", help = "PDF file name", widget = "FileChooser")
    parser.add_argument("text_file_name", help = "Text file name", widget = "FileSaver")
    parser.add_argument("margin_percentage", help = "margin_percentage",default='0.1')
    args = parser.parse_args()
    pdf_convert_text_with_margin_percentage(args.pdf_file_name, args.text_file_name, float(args.margin_percentage))
    pass

if __name__ == '__main__':
    main()
    pass