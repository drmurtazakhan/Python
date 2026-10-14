
# run: python Remove_DOC_Properties.py

from docx import Document

doc = Document("your_file.docx")
core_props = doc.core_properties
core_props.author = ""
core_props.category = ""
core_props.comments = ""
core_props.identifier = ""
core_props.keywords = ""
core_props.last_modified_by = ""
core_props.subject = ""
core_props.title = ""
doc.save("your_file_cleaned.docx")
