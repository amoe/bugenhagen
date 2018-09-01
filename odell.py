import docx
import pprint

# python-docx 0.8.7

PATH = "/home/amoe/martin_odell/Object-Oriented Methods a Foundation, Martin and Odell.docx"

doc = docx.Document(PATH)


# public api is

 # 'add_heading',
 # 'add_page_break',
 # 'add_paragraph',
 # 'add_picture',
 # 'add_section',
 # 'add_table',
 # 'core_properties',
 # 'element',
 # 'inline_shapes',
 # 'paragraphs',
 # 'part',
 # 'save',
 # 'sections',
 # 'settings',
 # 'styles',
 # 'tables'

for (index, paragraph) in enumerate(doc.paragraphs):
    print(index)
