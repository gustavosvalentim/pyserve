MIMETYPES = {
    'html': {
        'ext': '.html',
        'mimetype': 'text/html',
        'read_type': 'r'
    },
    'js': {
        'ext': '.js',
        'mimetype': 'application/js',
        'read_type': 'r'    
    },
    'css': {
        'ext': '.css',
        'mimetype': 'text/css',
        'read_type': 'r',    
    },
    'jpg': {
        'ext': '.jpg',
        'mimetype': 'image/jpg',
        'read_type': 'rb'    
    },
    'gif': {
        'ext': '.gif',
        'mimetype': 'image/gif',
        'read_type': 'rb'
    },
    'png': {
        'ext': '.png',
        'mimetype': 'image/png',
        'read_type': 'rb'
    },
    'ico': {
        'ext': '.ico',
        'mimetype': 'image/x-icon',
        'read_type': 'rb'
    }
}


def get_mimetype(filename):
    for mime in MIMETYPES:
        if filename.endswith(MIMETYPES[mime]['ext']):
            return MIMETYPES[mime]

    return None

def is_mimetype(filename, ext):
    if not filename.endswith(ext):
        return False

    return True