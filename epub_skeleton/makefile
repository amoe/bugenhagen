clean:
	rm -f content.epub

# Need to use -X to avoid generating 'extra fields'
content.epub: clean content
	(cd content; zip -X -r9 ../content.epub .)

check: content.epub
	epubcheck content.epub
