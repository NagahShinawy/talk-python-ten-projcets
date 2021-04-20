"""
created by Nagaj at 18/04/2021

Handle journal operations
load journals, save journal, add new journal
"""

import json
import os
from typing import List
from projects.app4.constants import BREAK_LINE

import jinja2


def load() -> List[str]:
    """
    if file exist , add entries to data list
    :return: list of journals
    """
    data = []
    fullpath = get_full_path()
    if os.path.exists(fullpath):
        with open(fullpath, 'r') as fin:
            entries = fin.readlines()
            for entry in entries:
                data.append(entry)
            entries.append("#" * 30 + '\n')
    return data


def save(entries: List[str]):
    fullpath = get_full_path()
    print(f"saving text to '{fullpath}'")
    with open(fullpath, 'w') as f:
        for entry in entries:
            f.write(entry)
        f.write(BREAK_LINE)


def to_html(entries):
    html_path, saves_path = get_saves_path_and_file_path('_home.html')
    with open(html_path, 'r') as htmlfile:
        content = htmlfile.read()
    template = jinja2.Template(content)
    home = template.render(title='All Journals', entries=entries)
    saving__html_path = os.path.join(saves_path, 'home.html')
    print(f"saving html to '{saving__html_path}'")
    with open(saving__html_path, 'w') as f:
        f.write(home)


def to_json(entries: List[str]):
    json_path, saves_path = get_saves_path_and_file_path('journals.json')
    data = [{"journal": entry.strip()} for entry in entries]
    print(f"saving json to '{json_path}'")
    with open(json_path, 'w') as f:
        json.dump(data, f, indent=4)


def get_saves_path_and_file_path(filename):
    saves_path = os.path.dirname(get_full_path())
    file_path = os.path.join(saves_path, filename)
    return file_path, saves_path


def get_full_path():
    parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    app_dir = os.path.join(parent_dir, 'app4')
    filepath = os.path.join(
        app_dir, "saves", "journals.txt"
    )

    fullpath = os.path.abspath(filepath)
    return fullpath
