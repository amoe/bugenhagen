import pickle
import pprint
import jinja2
import os
import pathlib

env = jinja2.Environment(
    loader=jinja2.FileSystemLoader('templates'),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True
)

with open('foo.pkl', 'rb') as handle:
    articles = pickle.load(handle)

tmpl = env.get_template('mytemplate.xhtml.j2')


output_dir = "expanded"
pathlib.Path(output_dir).mkdir(exist_ok=True) 

print("Rendering template")

for index, record in enumerate(articles):
    if record['user'] != 'NUKLEAR-SLUG':
        continue

    body = record['body']
    
    tmpl_params = {
        'title': "Article %d" % index,
        'body': body
    }

    result = tmpl.render(tmpl_params)

    output_path = os.path.join(output_dir, "article-%.4d.xhtml" % index)

    with open(output_path, 'w') as f:
        f.write(result)

print("Render done")

epub_root_dir = "epub_out"
pathlib.Path(epub_root_dir).mkdir(exist_ok=True)

def epub_root_render(source, target):
    content = env.get_template(source).render({})
    path = os.path.join(epub_root_dir, target)
    with open(path, 'w') as f:
        f.write(content)

epub_root_render('main.opf.j2', 'main.opf')
epub_root_render('mimetype.j2', 'mimetype')
epub_root_render('nav.xhtml.j2', 'nav.xhtml')

