from html_file import HTMLFile


def test_strict_select_one():
    """Test the HTMLFile class"""
    html_file = HTMLFile("tests/input.html")

    assert html_file.parsed_html().strict_select_one("title").text == "Example"
