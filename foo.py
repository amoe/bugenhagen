import docx
import pprint
import random
import lxml
import sys

# python-docx 0.8.7

PATH = "/home/amoe/martin_odell/Object-Oriented Methods a Foundation, Martin and Odell.docx"

doc = docx.Document(PATH)
for para in doc.paragraphs:
    for run in para.runs:
        print(dir(run.element))

