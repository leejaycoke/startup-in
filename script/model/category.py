# -*- coding: utf-8 -*-

from constants.class_enum import ClassEnum


class Category(ClassEnum):

    FRONTEND = ClassEnum("프론트엔트")
    BACKEND = ClassEnum("백엔드")
    ANDROID = ClassEnum("안드로이드")
    IOS = ClassEnum("iOS")
