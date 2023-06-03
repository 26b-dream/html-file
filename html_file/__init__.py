from __future__ import annotations

from extended_bs4 import ExtendedBeautifulSoup
from extended_path import ExtendedPath


class HTMLFile(ExtendedPath):
    def parsed(self) -> ExtendedBeautifulSoup:
        """Read and parse an html file"""

        # I don't know of any reason why you would want to use read_text instead of read_bytes for BeautifulSoup
        # For now this function will always just use read_bytes
        return ExtendedBeautifulSoup(self.read_bytes(), "lxml")

    def parsed_cached(self, reload: bool = False) -> ExtendedBeautifulSoup:
        """Read and parse an html file with caching"""

        # I don't know of any reason why you would want to use read_text instead of read_bytes for BeautifulSoup
        # For now this function will always just use read_bytes
        if not hasattr(self, "cached_parsed_html") or reload:
            self.cached_parsed_html = ExtendedBeautifulSoup(self.read_bytes_cached(reload), "lxml")

        return self.cached_parsed_html
