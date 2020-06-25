class MyList():
    def __init__(self, original_dict):
        self.data = original_dict or {}

    def __getitem__(self, key):
        return f'{key} - {self.data[key]}'

    def __setitem__(self, key, value):
        self.data[key] = value + 1

    def __str__(self):
        return self.data.__str__()


ex = MyList({'post': 1})
ex['test'] = 2
print(ex['test'])
print(ex)
