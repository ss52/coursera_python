import functools
import json


def to_json(func):
    @functools.wraps(func)
    def wrapped(*args, **kwagrs):
        result = func(*args, **kwagrs)
        return json.dumps(result)

    return wrapped


# @to_json
# def get_data():
#     return {'data': 42}


# print(get_data())
