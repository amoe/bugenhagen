import urllib.request
import bs4
import nuklear_slug_recipe
import pprint
import renderer
import archiver

PARSER = 'lxml'

this_recipe = nuklear_slug_recipe.NuklearSlugRecipe()

all_articles = []

for url in this_recipe.get_urls():
    page_data = urllib.request.urlopen(url)
    soup = bs4.BeautifulSoup(page_data, PARSER)
    
    these_articles = this_recipe.get_articles(soup)
    all_articles.extend(these_articles)

filtered_articles = filter(this_recipe.is_article_included, all_articles)

renderer = renderer.Renderer(epub_root_dir="epub_out")

extra_context = {
    'title': this_recipe.get_title()
}

renderer.make_epub(filtered_articles, extra_context)

archiver = archiver.Archiver()
archiver.archive()
