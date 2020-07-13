import time
import os


pid = os.fork()

if pid == 0:
    while True:
        # дочерний процесс, pid == 0
        # тут будет выполняться код дочернего процесса
        print("child: ", os.getpid())
        time.sleep(5)
else:
    # родительский процесс
    # а тут будет код родительского процесса. Магия!
    print("parent: ", os.getpid())
    os.wait()
