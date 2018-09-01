import pickle
import pprint
import jinja2
import os
import pathlib
import shutil
import uuid
import subprocess

env = jinja2.Environment(
    loader=jinja2.FileSystemLoader('templates'),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True
)

class Renderer(object):
    def __init__(self, epub_root_dir):
        self.epub_root_dir = epub_root_dir

    def epub_root_render(self, source, target, context={}):
        content = env.get_template(source).render(context)
        path = os.path.join(self.epub_root_dir, target)

        target_dir = os.path.dirname(path)
        pathlib.Path(target_dir).mkdir(exist_ok=True)

        with open(path, 'w') as f:
            f.write(content)


    def make_epub(self, articles, extra_context={}):
        tmpl = env.get_template('mytemplate.xhtml.j2')

        output_dir = "expanded"
        pathlib.Path(output_dir).mkdir(exist_ok=True) 

        print("Rendering template")

        compiled_articles = []

        for index, record in enumerate(articles):
            tmpl_params = {
                'title': "Article %d" % index,
                'body': record.body
            }

            result = tmpl.render(tmpl_params)

            article_basename = "article-%.4d.xhtml" % index
            output_path = os.path.join(output_dir, article_basename)

            with open(output_path, 'w') as f:
                f.write(result)

            compilation_record = {
                'id': uuid.uuid4(),
                'basename': article_basename,
                'article_path': output_path
            }

            compiled_articles.append(compilation_record)

        print("Render done")

        print("Creating epub structure")

        pathlib.Path(self.epub_root_dir).mkdir(exist_ok=True)

        article_subdirectory = 'articles'

        article_target_dir = os.path.join(self.epub_root_dir, article_subdirectory)
        pathlib.Path(article_target_dir).mkdir(exist_ok=True)

        articles_context = {
            'articles': compiled_articles,
            'article_subdirectory': article_subdirectory
        }

        articles_context.update(extra_context)


        self.epub_root_render('main.opf.j2', 'main.opf', articles_context)
        self.epub_root_render('mimetype.j2', 'mimetype')
        self.epub_root_render('nav.xhtml.j2', 'nav.xhtml', articles_context)
        self.epub_root_render('container.xml', 'META-INF/container.xml')

        for article in compiled_articles:
            shutil.copy(article['article_path'], article_target_dir)

        print("Done")
