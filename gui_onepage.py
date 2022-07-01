# encoding: utf-8
from gooey import Gooey,GooeyParser
from easy_pdf import display_pdf_text_one_page

@Gooey (program_name = "PDF to Text", program_description = "Convert PDF to Text")
def main():
    parser = GooeyParser()
    parser.add_argument("pdf_file_name", help = "PDF file name", widget = "FileChooser")
    parser.add_argument("--page_index", help = "Page index", widget = "IntegerField",gooey_options={
    'min': 0, 
    'max': 5, 
    'increment': 1 
})
    args = parser.parse_args()
    print(args)
    display_pdf_text_one_page(args.pdf_file_name, int(args.page_index))
    pass

if __name__ == '__main__':
    main()
    pass