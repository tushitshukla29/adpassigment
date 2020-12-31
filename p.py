from PyPDF2 import PdfFileMerger
import os
pdfs = [a for a in os.listdir() if a.endswith(".pdf")]
merger = PdfFileMerger()

for pdf in pdfs:
    merger.append(open(pdf,'b'))

with open("result.pdf","wb") as fout:
	merger.write(fout)
merger.close() 