from json import JSONDecoder


def parse_object_pairs(pairs):
    return pairs


data = """
{"foo": {"baz": 42}, "foo": 7}
"""

decoder = JSONDecoder(object_pairs_hook=parse_object_pairs)
obj = decoder.decode(data)
print(obj[0])
