# -*- coding: utf-8 -*-

import json
import sys
import locale

from jinja2 import Environment, PackageLoader, select_autoescape, BaseLoader
from os import listdir
from pathlib import Path

from model.category import Category
from model.job import Job
from pprint import pprint
from marshmallow import Schema, EXCLUDE

PROJECT_PATH = Path(__file__).parent.parent.absolute()

RECRUITS_DIR = PROJECT_PATH.joinpath("jobs")
README_PATH = PROJECT_PATH.joinpath("README.md")
TEMPLATE_PATH = PROJECT_PATH.joinpath("TEMPLATE.md")
DB_PATH = PROJECT_PATH.joinpath("db.json")
HTML_TEMPLATE = PROJECT_PATH.joinpath("./script/table.html")


def read_jobs():
    jobs = []

    for recruit_file in RECRUITS_DIR.iterdir():
        with open(recruit_file) as fp:
            jobs.append(fp.read())

    return jobs


def get_jobs():
    jobs = read_jobs()
    return [json.loads(r) for r in jobs]


def create_template_engine():
    with open(HTML_TEMPLATE) as fp:
        html_templte = fp.read()
    return Environment(loader=BaseLoader).from_string(html_templte)


def create_table(jobs):
    engine = create_template_engine()
    return engine.render(jobs=jobs)


def read_template():
    with open(TEMPLATE_PATH) as fp:
        return fp.read()


def generate_readme(table):
    template = read_template()
    return template.replace('{TEMPLATE}', table)


def write_readme(readme):
    with open(README_PATH, 'w') as fp:
        fp.write(readme)


def run():
    jobs = [Job().dump(j) for j in get_jobs()]
    pprint(jobs)
    table = create_table(jobs)
    readme = generate_readme(table)
    write_readme(readme)


if __name__ == "__main__":
    run()
