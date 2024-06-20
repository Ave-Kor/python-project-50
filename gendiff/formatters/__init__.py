from gendiff.formatters.stylish import make_stylish
from gendiff.formatters.plain import make_plain
from gendiff.formatters.json import make_json


def formatting_diff(diff, format):
    if format == 'stylish':
        return make_stylish(diff)
    elif format == 'plain':
        return make_plain(diff).rstrip()
    elif format == 'json':
        return make_json(diff)
    else:
        return 'Unknown formatter!'
