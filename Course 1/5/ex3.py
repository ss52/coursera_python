from multiprocessing import Process


def f(name):
    print("Name:", name)


p = Process(target=f, args=("Mike",))
# еще вариант создать класс унаследованный от Process и переопределить метод run

p.start()  # запуск процесса
p.join()  # ждем завершения всех запущенных процессов
