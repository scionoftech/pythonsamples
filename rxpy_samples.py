import rx

'''' Sample 1 '''


def push_five_strings(observer):
    observer.on_next("Alpha")
    observer.on_next("Beta")
    observer.on_next("Gamma")
    observer.on_next("Delta")
    observer.on_next("Epsilon")
    observer.on_completed()


class PrintObserver(rx.Observer):

    def on_next(self, value):
        print("Received {0}".format(value))

    def on_completed(self):
        print("Done!")

    def on_error(self, error):
        print("Error Occurred: {0}".format(error))


dis = rx.disposables.CompositeDisposable()
dis.add(rx.Observable.create(push_five_strings).subscribe(PrintObserver()))
dis.dispose()

'''' Sample 2 '''

import rx

dis = rx.disposables.CompositeDisposable()


class PrintObserver(rx.Observer):

    def on_next(self, value):
        print("Received {0}".format(value))

    def on_completed(self):
        print("Done!")

    def on_error(self, error):
        print("Error Occurred: {0}".format(error))


dis.add(rx.Observable.of("Alpha", "Beta", "Gamma", "Delta", "Epsilon").subscribe(PrintObserver()))
dis.clear()
print(dis.is_disposed)

'''' Sample 3 '''


class RxAsync:
    dis = rx.disposables.CompositeDisposable()

    def on_success(self, reponse):
        pass

    def on_failure(self, error):
        pass

    def getobservable(self, observer):
        pass

    def doWork(self, process_id):
        self.process_id = process_id
        dis.add(rx.Observable.create(self.getobservable).
                subscribe(on_next=lambda value: self.on_success(value),
                          on_completed=lambda: print("Completed trades"),
                          on_error=lambda e: self.on_failure(e)))

    def clear_dis(self):
        dis.clear()


class Test(RxAsync):

    def work(self):
        ll = []
        for i in range(100000):
            ll.append(i)
        return ll

    def work_t(self):
        ll = []
        for i in range(10):
            ll.append(i)
        return ll

    def getobservable(self, observer):
        if self.process_id is 1:
            observer.on_next(self.work())
        elif self.process_id is 2:
            observer.on_next(self.work_t())
        observer.on_completed()

    def on_success(self, reponse):
        print(reponse)

    def on_failure(self, error):
        print(error)


t = Test()
t.doWork(1)
