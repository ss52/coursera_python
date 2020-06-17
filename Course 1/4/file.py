import os.path
import tempfile  # tempfile.gettempdir()


class File():
    def __init__(self, file_path):
        self.path = file_path
        if not os.path.exists(file_path):
            with open(file_path, 'w'):
                pass
        self.current = 0

    def read(self):
        with open(self.path, 'r') as file:
            text = file.read()
        return text

    def write(self, str):
        with open(self.path, 'w') as file:
            file.write(str)

    def __add__(self, second_file):
        text_1 = self.read()
        text_2 = second_file.read()
        text = text_1 + text_2

        new_path = os.path.join(tempfile.gettempdir(), 'temp.txt')
        new_file = File(new_path)
        new_file.write(text)

        return new_file

    def __str__(self):
        return os.path.abspath(self.path)

    def __iter__(self):
        return self

    def __next__(self):
        with open(self.path, 'r') as file:
            lines = file.read().splitlines()

        if self.current < len(lines):
            text = lines[self.current]
            self.current += 1
        else:
            raise StopIteration

        return text


# file_obj_1 = File('file_1')
# file_obj_2 = File('file_2')

# file_obj_1.write('test')
# file_obj_2.write('super')

# file_obj_3 = file_obj_1 + file_obj_2

# print(type(file_obj_3))
# print(file_obj_3)
# print(file_obj_3.read())
