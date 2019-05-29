from threading import Thread
import time


class Compute(Thread):
    def __init__(self, data):
        Thread.__init__(self)
        self.data = data

    def run(self):
        for x in self.data:
            print(x)
            time.sleep(3)
        print('Thread is completed')


if __name__ == '__main__':
    dd = range(100)
    thread_a = Compute(dd)
    thread_a.start()
    print('Thread is started')
