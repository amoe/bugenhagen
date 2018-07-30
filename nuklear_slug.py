
import lxml.html
import urllib.request

part_urls = []

part_url_template = "https://forum.egosoft.com/viewtopic.php?t=232789&postdays=0&postorder=asc&start=%d"

for n in range(0, 1471, 15):
    this_url = part_url_template % n
    part_urls.append(this_url)

print(part_urls)

for url in part_urls:
    etree = lxml.html.parse(urllib.request.urlopen(url))
    print(etree)
