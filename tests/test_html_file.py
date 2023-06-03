from html_file import HTMLFile


def test_parsed():
    file = HTMLFile("tests/test_parsed.html")
    file.write("<title>Example</title>")
    assert file.parsed().strict_select_one("title").text == "Example"
    file.delete()


def test_parsed_cached_changed_file():
    file = HTMLFile("tests/test_parsed_cached_changed_file.html")
    file.write("<title>Example</title>")
    file.parsed_cached()
    file.write("")
    assert file.parsed_cached().strict_select_one("title").text == "Example"
    file.delete()


def test_parsed_cached_updating_cache():
    file = HTMLFile("tests/test_parsed_cached_updating_cache.html")
    file.write("<title>Example</title>")
    file.parsed_cached()
    file.write("<title>Title</title>")
    assert file.parsed_cached(True).strict_select_one("title").text == "Title"
    file.delete()
