# -*- coding: utf-8 -*-

from marshmallow import Schema, fields
from model.category import Category
from model.career import Career

from datetime import date
from datetime import datetime as dt
from datetime import timedelta


class Recruit(Schema):

    description = fields.Str()
    category = fields.Function(lambda f: Category.of(f['category']).title)
    limit_date = fields.Function(
        lambda f: dt.strptime(f['limit_date'], '%Y-%m-%d').date())
    link = fields.Url()
    minimum_career = fields.Function(
        lambda f: Career.of(f['minimum_career']).title)
    minimum_qualifications = fields.List(fields.Str())
    preferred_qualifications = fields.List(fields.Str())
    is_tomorrows_limit = fields.Method('calculate_is_tomorrows_limit')
    is_outdated = fields.Method('calculate_is_outdated')

    def calculate_is_tomorrows_limit(self, recruit):
        limit_date = dt.strptime(recruit['limit_date'], '%Y-%m-%d').date()
        tomorrow = date.today() + timedelta(days=1)
        return tomorrow == limit_date

    def calculate_is_outdated(self, recruit):
        limit_date = dt.strptime(recruit['limit_date'], '%Y-%m-%d').date()
        return limit_date < date.today()


class Company(Schema):

    name = fields.Str()
    link = fields.Url()
    series_step = fields.Str()


class Job(Schema):

    company = fields.Nested(Company())
    recruits = fields.List(fields.Nested(Recruit()))
