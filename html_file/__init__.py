"""Class for html files"""
from __future__ import annotations

from typing import TYPE_CHECKING

from extended_bs4 import ExtendedBeautifulSoup
from extended_path import ExtendedPath

if TYPE_CHECKING:
    import os
    from datetime import date, datetime
    from typing import Any


class HTMLFile(ExtendedPath):
    """Class for html files"""

    def __init__(
        self,
        *_args: str | bytes | os.PathLike[str] | int | datetime | date | float,
    ) -> None:
        self.parsed_cached_value = None
        super().__init__()

    def parsed(self) -> ExtendedBeautifulSoup:
        """Read and parse an html file

        Returns:
            ExtendedBeautifulSoup: Parsed html file"""

        # I don't know of any reason why you would want to use read_text instead of read_bytes for BeautifulSoup. Unless
        # a specific need arises this function will always just use read_bytes
        return ExtendedBeautifulSoup(self.read_bytes(), "lxml")

    def parsed_cached(self, reload: bool = False) -> ExtendedBeautifulSoup:
        """Read a file, parse it using BeautifulSoup4, then cache the result

        Args:
            reload (bool, optional): If True, reload the file into the cache. Defaults to False.

        Returns:
            ExtendedBeautifulSoup: Parsed html file"""

        # I don't know of any reason why you would want to use read_text instead of read_bytes for BeautifulSoup. Unless
        # a specific need arises this function will always just use read_bytes
        if not self.parsed_cached_value or reload:
            self.parsed_cached_value = ExtendedBeautifulSoup(self.read_bytes_cached(reload), "lxml")

        return self.parsed_cached_value
