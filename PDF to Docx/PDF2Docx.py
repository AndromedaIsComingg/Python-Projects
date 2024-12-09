# pip install pdf2docx

from pdf2docx import Converter

pdf_file = "MAC_803_Ori.pdf"

docx_file = "MAC_803.docx"

material = Converter(pdf_file)
material.convert(docx_file)


material.close()



