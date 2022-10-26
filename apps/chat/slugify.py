#!/usr/bin/python3
# -*- coding: utf-8 -*-
import re

from .transliterate import transliterate


def slugify(string):
    """Слагификация"""
    string = transliterate(string)
    pattern = r'[^\w+]'
    slug = str(re.sub(pattern, '-', string)).lower()
    return slug
