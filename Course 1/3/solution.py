class FileReader:
    def __init__(self, file_name):
        self.file_name = file_name

    def read(self):
        try:
            with open(self.file_name, 'r') as file:
                text = file.read()
        except FileNotFoundError:
            text = ""

        return text


# with open('some_file.txt', 'w') as file:
#     file.write('some text')
#
# reader = FileReader('some_file.txt')
# line = reader.read()
# print(line)
