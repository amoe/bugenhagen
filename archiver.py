import zipfile
import os.path

def epubzip(path):
    return zipfile.ZipFile(
        path, mode='w', compression=zipfile.ZIP_DEFLATED
    )


# These files should be added to the zip before the rest of the files.

EPUB_METADATA_FILES = [
    'mimetype',
    'META-INF/container.xml',
    'main.opf',
    'nav.xhtml',
]
metadata_set = set(EPUB_METADATA_FILES)

class Archiver(object):
    def __init__(self):
        pass

    def archive(self, base_epub_dir):
        to_add = []

        for metadata_file in EPUB_METADATA_FILES:
            to_add.append({'filename': os.path.join(base_epub_dir, metadata_file),
                           'arcname': metadata_file})


        for root, dirs, files in os.walk(base_epub_dir):
            relative_root = os.path.relpath(root, base_epub_dir)

            for f in files:
                if relative_root == '.':
                    relative_path = f
                else:
                    relative_path = os.path.join(relative_root, f)

                if relative_path not in metadata_set:
                    to_add.append(
                        {'filename': os.path.join(root, f),
                         'arcname': relative_path}
                    )


        with epubzip('out.epub') as z:
            for addition in to_add:
                z.write(**addition)
