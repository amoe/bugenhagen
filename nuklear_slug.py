import urllib.request
import time
import bs4
import pprint

PARSER = 'lxml'

part_urls = []

part_url_template = "https://forum.egosoft.com/viewtopic.php?t=232789&postdays=0&postorder=asc&start=%d"

for n in range(0, 1471, 15):
    this_url = part_url_template % n
    part_urls.append(this_url)


POST_BODY_XPATH = "//span[@class='postbody']"

def f7(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]

for url in part_urls[0:1]:
    print(url)
    page_data = urllib.request.urlopen(url)
    soup = bs4.BeautifulSoup(page_data, PARSER)
    result = soup.find_all('span', class_='postbody')

    
    print("Found %d postbodies" % len(result))

    all_containing_tds = []

    for post_body_span in result:
        containing_td = post_body_span.parent
        all_containing_tds.append(containing_td)

    seen = set()

    all_posts = []

    
    for post_td in all_containing_tds:
        if not post_td in seen:
            containing_row1 = post_td.find_previous('td', class_=['row1', 'row2'])
            previous_row1 = containing_row1.find_previous('td', class_=['row1', 'row2'])
            name_span = previous_row1.find('span', class_='name')
            user_name = name_span.get_text(strip=True)
            post_markup = post_td.prettify()

            post_record = {
                'user': user_name,
                'body': post_markup
            }

            all_posts.append(post_record)
            seen.add(post_td)
            
pprint.pprint(all_posts)


    
    # etree = lxml.html.parse()
    # post_body_node = etree.xpath(POST_BODY_XPATH)

    # # scan upwards
    
    # result = post_body_node.xpath("./ancestor::td[@class='row1']")
    # print(result)
    
    # time.sleep(5)
