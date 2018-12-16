import sys

from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams, LTContainer, LTTextBox
from pdfminer.pdfinterp import PDFPageInterpreter, PDFResourceManager
from pdfminer.pdfpage import PDFPage

PDF = '../../datas/000232384.pdf'

def find_textboxes_resoursivy(layout_obj):
    if isinstance(layout_obj,LTTextBox):
        return [layout_obj]

    if isinstance(layout_obj, LTContainer):
        boxes = []
        for child in layout_obj:
            boxes.extend(find_textboxes_resoursivy(child))

        return boxes
    return []

laparams = LAParams(detect_vertical=True)
resource_manager = PDFResourceManager()
device = PDFPageAggregator(resource_manager, laparams=laparams)
interpreter = PDFPageInterpreter(resource_manager,device)

with open(PDF, 'rb') as f:
    for page in PDFPage.get_pages(f):
        interpreter.process_page(page)
        layout = device.get_result()
        boxes = find_textboxes_resoursivy(layout)
        boxes.sort(key=lambda b:(-b.y1, b.x0))

        for box in boxes:
            print('-' * 10)

            print(box.get_text().strip())