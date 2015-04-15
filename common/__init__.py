from decimal import Decimal
from html import unescape
import pytz
import re
from setuptools.compat import unicode
from common.titlecase import titlecase

__author__ = 'Nhung'


def american_to_decimal(odds):
    if unicode(odds).lower() in {'pk', 'pick', 'ev'}:
        return Decimal(2)

    else:
        odds = Decimal(odds)

        if odds >= 100:
            return 1 + (odds / 100)

        elif odds <= -100:
            return 1 - (100 / odds)

        else:
            raise ValueError('odds must be >= 100 or <= -100')

def datetime_to_UTC(datetime, original_time_zone):
    return pytz.timezone(original_time_zone).localize(datetime).astimezone(pytz.utc)

def clean(s):
	return unescape(re.sub(r'(?: Jr$|Sr$)|(?:(?:^| )[A-Z](?= |$))|St(?= )', '\g<0>.', titlecase(re.sub(r'\s+', ' ', re.sub(r'(?:\(.+?\))', '', s)).strip())))
