from __future__ import annotations

from extended_bs4 import ExtendedBeautifulSoup
from extended_path import ExtendedPath


class HTMLFile(ExtendedPath):
    def parsed_html(self) -> ExtendedBeautifulSoup:
        """Read and parse an html file with caching"""
        return ExtendedBeautifulSoup(self.read_bytes(), "lxml")
