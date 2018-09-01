import docx
import pprint
import random
import lxml
import sys

# python-docx 0.8.7

PATH = "/home/amoe/martin_odell/Object-Oriented Methods a Foundation, Martin and Odell.docx"

doc = docx.Document(PATH)
print(len(doc.inline_shapes))

