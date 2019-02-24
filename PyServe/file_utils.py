def getFileBytes(filepath, read_mode='r', encoding='utf-8'):
    try:
        _file = open(filepath, read_mode)
    except IOError:
        return None

    _file_content = _file.read()

    if not type(_file_content) is bytes:
        _file_content = _file_content.encode(encoding)

    _file.close()

    return _file_content