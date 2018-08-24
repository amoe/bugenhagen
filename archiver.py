import zipfile

def epubzip(path):
    return zipfile.ZipFile(
        path, mode='w', compression=zipfile.ZIP_DEFLATED
    )


with epubzip('out.zip') as z:
    z.write('templates/mimetype.j2', arcname='mimetype')
    

