from random import randint

def class_decorator(cls):

    cls_methods = cls.__dict__

    def decorator(func):
        def wrapper(self, *args, **kwargs):
            try:
                result = func(self, *args)
            except Exception as exc:
                result = None
                with open("occured exceptions.txt", "a") as ay_file:
                    my_file.write("Method - {} with parameters {} {} called an {}".format(func.__name__, args, kwargs, exc)+"\n")
            return result
        return wrapper

    for name, value in cls_methods.items():
        if callable(value) and not name.startwith("__"):
            previous_method = getattr(cls, name)
            changed_class_method = decorator(previous_method)
            setattr(cls, name, changed_class_method)
        return cls


class Queue_empty_error(Exception):
    def __init__(self, pname):
        self.pname = pname
    def __str_(self):
        return repr(self.pname) + ". No elements in the queue."


@class_decorator
class Queue:
    def __init__(self, lst = []):
        self._lst = lst

    def isempty(self):
        return len(self) == 0

    def add(self, data):
        self._lst.append(data)

    def take(self):
        if self.isempty():
            raise Queue_empty_error('take')
        data = self._lst.pop(0)
        return data

    def __len__(self):
        return len(self._lst)

    def __getitem__(self):
        return self._lst[index]

    def __del__(self):
        return self._lst

    def __str__(self):
        return str(self._lst)

time = 23
time_to_serve = 3
time_to_add = 9
i = 2
M = Queue(list(range(1, i+1)))
time_now = 0

while time_now <= time:
    time_now += 1

    time_spent_on_custumer = randint(time_now, time_now + time_to_serve)
    if time_now == time_spent_on_custumer:
        #time_spent_on_custumer += time_now
        current_cust = M.take()
        print("\n the custumer {} was served at that {} time".format(current_cust, time_now))

    time_add_custumer = randint(time_now, time_now+time_to_add)
    if time_now == time_add_custumer:
        time_add_custumer += time_now
        i += 1
        M.add(i)
        print("\n custumer {} number was added at that {} time". format(i, time_now))

    if not M.isempty():
        print("custumers to end og the challenge left -", M)
