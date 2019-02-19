from jrdb import urlcodec


def test_encode():
    urls = ['http://hoge/', 'http://fuga/']
    actual = urlcodec.encode(urls)
    expected = b'x\x9c\xcb())\xb0\xd2\xd7\xcf\xc8OO\xd5\xd7\xc9\x80p\xd2J\xd3\x13\xf5\x01qo\x08\x81'
    assert actual == expected


def test_decode():
    data = b'x\x9c\xcb())\xb0\xd2\xd7\xcf\xc8OO\xd5\xd7\xc9\x80p\xd2J\xd3\x13\xf5\x01qo\x08\x81'
    actual = urlcodec.decode(data)
    expected = ['http://hoge/', 'http://fuga/']
    assert actual == expected
