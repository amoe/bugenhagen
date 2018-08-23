import pickle
import pprint
import jinja2
import os
import pathlib
import shutil

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

compiled_articles = []

for index, record in enumerate(articles):
    if record['user'] != 'NUKLEAR-SLUG':
        continue

    body = record['body']
    
    tmpl_params = {
        'title': "Article %d" % index,
        'body': body
    }

    result = tmpl.render(tmpl_params)

    article_basename = "article-%.4d.xhtml" % index
    output_path = os.path.join(output_dir, article_basename)

    with open(output_path, 'w') as f:
        f.write(result)

    compilation_record = {
        'basename': article_basename,
        'article_path': output_path
    }

    compiled_articles.append(compilation_record)

print("Render done")

epub_root_dir = "epub_out"
pathlib.Path(epub_root_dir).mkdir(exist_ok=True)

def epub_root_render(source, target, context={}):
    content = env.get_template(source).render(context)
    path = os.path.join(epub_root_dir, target)
    with open(path, 'w') as f:
        f.write(content)


article_subdirectory = 'articles'

article_target_dir = os.path.join(epub_root_dir, article_subdirectory)
pathlib.Path(article_target_dir).mkdir(exist_ok=True)


epub_root_render('main.opf.j2', 'main.opf')
epub_root_render('mimetype.j2', 'mimetype')
epub_root_render('nav.xhtml.j2', 'nav.xhtml', {'articles': compiled_articles,
                                               'article_subdirectory': article_subdirectory})

for article in compiled_articles:
    shutil.copy(article['article_path'], article_target_dir)
