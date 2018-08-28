import zipfile
import os.path

def epubzip(path):
    return zipfile.ZipFile(
        path, mode='w', compression=zipfile.ZIP_DEFLATED
    )


base_epub_dir = "epub_skeleton/content"

def do_archive(zf, base_dir):
    mimetype_full_path = os.path.join(base_epub_dir, 'mimetype')

    zf.write(mimetype_full_path, arcname='mimetype')

with epubzip('out.epub') as z:
    do_archive(z, base_epub_dir)
