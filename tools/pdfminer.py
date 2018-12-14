import sys
import os
# sys.path.append('C:\Users\yohei\Anaconda3')
import pdfminer
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams, LTContainer
from pdfminer.pdfinterp import PDFPageInterpreter, PDFResourceManager
from pdfminer.pdfparser import PDFPage

# laprm = LAParams(detect_vertical=True)
# resource_mng = PDFResourceManager()
# device = PDFPageAggregator(resource_mng, laparams=laprm)
