# -*- coding: utf-8 -*-

import json

from pathlib import Path
from jinja2 import Environment, BaseLoader
from model.job import Job

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
        return Environment(loader=BaseLoader).from_string(fp.read())


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


def exclude_outdated(jobs):
    latest_jobs = []

    for job in jobs:
        recruits = [r for r in job['recruits'] if not r['is_outdated']]
        job['recruits'] = recruits
        latest_jobs.append(job)
    return latest_jobs


def run():
    job_models = [Job().dump(j) for j in get_jobs()]
    latest_jobs = exclude_outdated(job_models)

    table = create_table(latest_jobs)
    readme = generate_readme(table)
    write_readme(readme)


if __name__ == "__main__":
    run()
