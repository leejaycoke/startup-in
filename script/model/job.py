# -*- coding: utf-8 -*-

from marshmallow import Schema, fields
from model.category import Category
from model.career import Career

from datetime import datetime
from datetime import timedelta


class Recruit(Schema):

    description = fields.Str()
    category = fields.Function(lambda f: Category.of(f['category']).title)
    limit = fields.Function(
        lambda f: datetime.strptime(f['limit'], '%Y-%m-%d').date())
    link = fields.Url()
    minimum_career = fields.Function(
        lambda f: Career.of(f['minimum_career']).title)
    minimum_qualifications = fields.List(fields.Str())
    preferred_qualifications = fields.List(fields.Str())
    is_tomorrow_limit = fields.Method('calculate_is_tomorrow_limit')

    def calculate_is_tomorrow_limit(self, job):
        limit_date = datetime.strptime(job['limit'], '%Y-%m-%d').date()
        return (datetime.now() + timedelta(days=1)).date() == limit_date


class Company(Schema):

    name = fields.Str()
    link = fields.Url()
    series_step = fields.Str()


class Job(Schema):

    company = fields.Nested(Company())
    recruits = fields.List(fields.Nested(Recruit()))
