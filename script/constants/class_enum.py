# -*- coding: utf-8 -*-


class ClassEnum(object):

    def __init__(self, title):
        self.title = title

    @classmethod
    def of(cls, value):
        return cls.__getattribute__(cls, value)
