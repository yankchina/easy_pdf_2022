# encoding: utf-8
from gooey import Gooey,GooeyParser
from easy_pdf import pdf_convert_text

@Gooey (program_name = "PDF to Text", program_description = "Convert PDF to Text")
def main():
    parser = GooeyParser()
    parser.add_argument("pdf_file_name", help = "PDF file name", widget = "FileChooser")
    parser.add_argument("text_file_name", help = "Text file name", widget = "FileSaver")
    parser.add_argument("rectangle_coordinates", help = "Rectangle coordinates", widget = "TextField")
    args = parser.parse_args()
    pdf_convert_text(args.pdf_file_name, args.text_file_name, eval(args.rectangle_coordinates))
    pass

if __name__ == '__main__':
    main()
    pass