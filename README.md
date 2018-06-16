# bugenhagen

A collection of scripts to help with generating ebooks.

## `add_titles`

This will read a tab separated file in the format (filename, title).
Then it will call the sub-script `add_to_start_of_element`, which will create
a new H1 element inside the `entry-content` div.
Useful for adding titles to otherwise title-less articles.

## `extract_article_content.perl`

Will extract the HTML content of the `entry-content` div.

## `extract_article_dates.perl`

Will create tab-separated output of article dates.  This uses a META tag
to get the real date.

## `extract_article_titles.perl`

Creates the tab-separated input file that can later be used by `add_titles`.

## `generate_manifest_and_spine.perl`

Creates manifest and spine entries in the OPF file for the ebook, in EPUB 3
format.

## `strip_images.perl`

This is going to strip some useless tags from the article content.  This is a
postprocessing step that can be run after the `extract_article_content` step.

## `extract_article_v0.perl`

A previous version of `extract_article_content` that expects to locate 
the article content in a different HTML structure; specifically it just takes
the content of the first `article` element verbatim.

## `driver.perl`

This works with `extract_article_v0` as a wrapper script.  It just runs the
`tidy` program on the output before and after, to eliminate spurious changes
caused by the parsing and re-parsing of the output.
