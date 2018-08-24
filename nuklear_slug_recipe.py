import bugenhagen

class NuklearSlugArticle(bugenhagen.Article):
    def __init__(self, user, body):
        self.user = user
        self.body = body
        
class NuklearSlugRecipe(bugenhagen.Recipe):
    self.seen = set()

    def get_urls(self):
        part_urls = []
        part_url_template = "https://forum.egosoft.com/viewtopic.php?t=232789&postdays=0&postorder=asc&start=%d"

        for n in range(0, 1471, 15):
            this_url = part_url_template % n
            part_urls.append(this_url)

        return part_urls
        

    def get_articles(self, soup):
        these_articles = []

        result = soup.find_all('span', class_='postbody')

        print("Found %d postbodies" % len(result))

        all_containing_tds = []

        for post_body_span in result:
            containing_td = post_body_span.parent
            all_containing_tds.append(containing_td)

        for post_td in all_containing_tds:
            if not post_td in self.seen:
                containing_row1 = post_td.find_previous('td', class_=['row1', 'row2'])
                previous_row1 = containing_row1.find_previous('td', class_=['row1', 'row2'])
                name_span = previous_row1.find('span', class_='name')
                user_name = name_span.get_text(strip=True)
                post_markup = post_td.prettify()

                post_record = NuklearSlugArticle(user_name, post_markup)

                these_articles.append(post_record)
                self.seen.add(post_td)

        return these_articles
