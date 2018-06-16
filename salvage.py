#! /usr/bin/env python3

# Here we define a structure that is used for scraping Salvage pages.
# There are several elements.

# A certain set of urls, currently these are paths, but they should actually
# be URLs that will be downloaded using wget.
# The wget command is as such:
#   wget -p -k -e robots=off -w 10 -H -U 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.6) Gecko/20070802 SeaMonkey/1.1.4' -i ~/all-dig.list

article_urls = [
    "content/salvage.zone/in-print/salvage-perspectives-3-or-whats-a-hell-for/index.html",
    "content/salvage.zone/in-print/neither-westminster-nor-brussels/index.html",
    "content/salvage.zone/in-print/technically-female-women-machines-and-hyperemployment/index.html",
    "content/salvage.zone/online-exclusive/the-realism-of-audacity-rethinking-revolutionary-strategy-today/index.html",
    "content/salvage.zone/in-print/corbyn-labour-and-the-present-crisis/index.html",
    "content/salvage.zone/in-print/the-political-is-political-in-conversation-with-yasmin-nair/index.html",
    "content/salvage.zone/in-print/white-overseers-of-the-world/index.html",
    "content/salvage.zone/in-print/year-v/index.html",
    "content/salvage.zone/in-print/from-choice-to-polarity-politics-of-in-and-and-art/index.html",
    "content/salvage.zone/articles/extract-from-blacklivesmatter-to-black-liberation/index.html",
    "content/salvage.zone/in-print/the-new-swedish-fascism-an-introduction/index.html",
    "content/salvage.zone/in-print/finance-economics-and-politics/index.html",
    "content/salvage.zone/in-print/the-abasement-of-trauma/index.html",
    "content/salvage.zone/in-print/benghazi/index.html"
]

# It's probably useful to allow specifying selectors in terms of both xpath
# and CSS.  Xpath is kind of more general, because you can do things like get
# the values of dependent attributes.

# CSS selector that will be used to locate the title of the page.
# This will added as the content of an h1 element at the top of the page.
title_selector = '.entry-title'


body_selector = '.entry-content'

# <meta property="article:published_time" content="2016-07-08T15:20:21-05:00"/>

date_selector = "//meta[@property='article:published_time']/@content"

# The algorithm will basically go:
# Mirror the pages using wget.
# Tidy the pages using html5tidy.
# For each page:
#   Build a DOM tree in memory
#   Copy the contents of .entry-content
#   Strip extraneous tags from this
#   Add an h1 element
#   Add a title element
# Sort by date (possibly)
# Generate sorted spine
# Write sorted spine and manifest
