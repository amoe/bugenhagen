import docx
import pprint
import random

# python-docx 0.8.7

PATH = "/home/amoe/martin_odell/Object-Oriented Methods a Foundation, Martin and Odell.docx"

doc = docx.Document(PATH)


# public api for document is

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

# for (index, paragraph) in enumerate(doc.paragraphs):
#     print(index)

all_paragraphs = doc.paragraphs
# index = random.randint(0, len(all_paragraphs))
index = 3636
some_para = all_paragraphs[index]

# API for  paragraph consists of 

 # 'add_run',
 # 'alignment',
 # 'clear',
 # 'insert_paragraph_before',
 # 'paragraph_format',
 # 'part',
 # 'runs',
 # 'style',
 # 'text'

print(index)
print(some_para.text)

for run in some_para.runs:
    print(run.text)

        # text = ''
        # for run in self.runs:
        #     text += run.text
        # return text
