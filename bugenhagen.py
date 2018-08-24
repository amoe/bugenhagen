# An article is basically a struct with fields at least 'body'.
class Article(object):
    pass

class Recipe(object):
    def get_urls(self):
        raise NotImplementedError

    # Takes 1 bs4 object and returns a list of Article objects.
    def get_articles(self, soup):
        raise NotImplementedError
