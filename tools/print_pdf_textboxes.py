import sys

from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams, LTContainer
from pdfminer.pdfinterp import PDFPageInterpreter, PDFResourceManager
from pdfminer.pdfpage import PDFPage

PDF = '../../datas/000232384.pdf'

laparams = LAParams(detect_vertical=True)
resource_manager = PDFResourceManager()
device = PDFPageAggregator(resource_manager, laparams=laparams)
interpreter = PDFPageInterpreter(resource_manager,device)

with open(PDF, 'rb') as f:
    for page in PDFPage.get_pages(f):
        interpreter.process_page(page)
        layout = device.get_result()