# -*- coding: utf-8 -*-

import sys
import re
from typing import List


def find_links_in_text(text: str) -> List[str]:
    """Find links in a text and return a list of URLs."""

    link_pattern = re.compile(r'((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'\".,<>?«»“”‘’]))')

    raw_links = re.findall(link_pattern, text)

    links = [
        str(raw_link[0]).rstrip('/') for raw_link in raw_links
    ]

    return links


def find_links_in_file(filename: str) -> List[str]:
    """Find links in a file and return a list of URLs from text file."""

    with open(filename, mode='r', encoding='utf-8') as file:
        readme = file.read()
        index_section = readme.find('## Index')
        content = readme[index_section:]

    links = find_links_in_text(content)

    return links


def check_duplicate_links(links: List[str]) -> bool:
    """Check for duplicated links and return True or False."""

    print('Checking for duplicated links...')

    seen = {}
    duplicates = []
    has_duplicate = False

    for link in links:
        if link not in seen:
            seen[link] = 1
        else:
            if seen[link] == 1:
                duplicates.append(link)

    if not duplicates:
        print(f'No duplicate links.')
    else:
        print(f'Found duplicate links: {duplicates}')
        has_duplicate = True
    
    return has_duplicate


if __name__ == '__main__':
    num_args = len(sys.argv)

    if num_args < 2:
        print('No .md file passed')
        sys.exit(1)

    links = find_links_in_file(sys.argv[1])

    has_duplicate = check_duplicate_links(links)
