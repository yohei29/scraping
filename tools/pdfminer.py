import sys
import pprint




from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams, LTContainer
from pdfminer.pdfinterp import PDFPageInterpreter, PDFResourceManager
from pdfminer.pdfpage import PDFPage

laprm = LAParams(detect_vertical=True)
resource_mng = PDFResourceManager()
device = PDFPageAggregator(resource_mng, laparams=laprm)
