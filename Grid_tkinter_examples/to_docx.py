# to_docx_create.py

# Remember! First: pip install python-docx

import docx
doc = docx.Document()
doc.add_paragraph('Say Hello!')
doc.save('say_hello.docx')