from docx import Document
from docxcompose.composer import Composer

files = ["D:/output/pp.docx", "D:/output/tt.docx","D:/output/pu.docx"]
composed = "D:/output/composed.docx"

result = Document(files[0])
result.add_page_break()
composer = Composer(result)

for i in range(1, len(files)):
    doc = Document(files[i])

    if i != len(files) - 1:
        doc.add_page_break()

    composer.append(doc)

composer.save(composed)