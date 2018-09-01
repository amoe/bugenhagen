import urllib.request
import bs4
import nuklear_slug_recipe
import pprint
import renderer
import archiver
import unittest

class UrllibUrlRetriever(object):
    def retrieve(self, url):
        return urllib.request.urlopen(url).read()

class StubUrlRetriever(object):
    def retrieve(self, url):
        return "<html></html>"

class Driver(object):
    def __init__(self, retriever):
        self.retriever = retriever

    def run(self):
        PARSER = 'lxml'
        this_recipe = nuklear_slug_recipe.NuklearSlugRecipe()

        all_articles = []

        for url in this_recipe.get_urls():
            page_data = self.retriever.retrieve(url)
            soup = bs4.BeautifulSoup(page_data, PARSER)

            these_articles = this_recipe.get_articles(soup)
            all_articles.extend(these_articles)

        filtered_articles = filter(this_recipe.is_article_included, all_articles)

        renderer_obj = renderer.Renderer(epub_root_dir="epub_out")

        extra_context = {
            'title': this_recipe.get_title()
        }

        renderer_obj.make_epub(filtered_articles, extra_context)

        archiver_obj = archiver.Archiver()
        archiver_obj.archive("epub_out")

#driver = Driver(UrllibUrlRetriever())
driver = Driver(StubUrlRetriever())
driver.run()
