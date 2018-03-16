# bugenhagen

A collection of scripts to help with generating ebooks.

## `add_titles`

This will read a tab separated file in the format (filename, title).
Then it will call the sub-script `add_to_start_of_element`, which will create
a new H1 element inside the `entry-content` div.
Useful for adding titles to otherwise title-less articles.

## `carldiggler.perl`

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

This is going to strip a given set of matches.  This is a postprocessing step
that can be run after the `extract_article_content` step.
