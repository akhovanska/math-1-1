# Виконати задачу Т19.9 з використанням метакласів замість
# декоратора. А саме, описати метаклас, який додає до створюваних ним
# класів save() та load().


class MetaClass(type):

    def __new__(cls, *args):

        def save(cls):
            cls_methods = cls.__dict__
            print(cls_methods)
            with open('saved19.txt', 'w') as f:

                for name, value in cls_methods.items():
                    if not name.startswith("__"):
                        f.write(f'{name}={value}\n')
                        print(f'Записано в файл: {name}={value}')

        def load(cls):
            # cls_methods = cls.__dict__
            with open('saved19.txt') as f:
                data = f.readlines()
                for line in data:
                    name = line.strip().split('=')[0]
                    value = line.strip().split('=')[1]
                    print(f'Загружено атрибути: {name}={value}')
                    setattr(cls, name, value)
            # return cls

        cls = super().__new__(cls, *args)
        setattr(cls, load.__name__, load)  # добавляємо методи в клас
        setattr(cls, save.__name__, save)
        return cls


class Point2(metaclass=MetaClass):
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def __str__(self):
        return f'({self._x}), ({self._y})'

    def load(self):
        pass
    
    def save(self):
        pass


class Point3(metaclass=MetaClass):
    def __init__(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def get_z(self):
        return self._z

    def __str__(self):
        return f'({self._x}), ({self._y}), ({self._z})'

    def save(self):
        pass
    
    def load(self):
        pass

p = Point2(1, 3)
p.save()
p.load()
print('\nPoint3: ')
p3 = Point3(5, 4, 3)
p3.save()
p3.load()
print(Point2.__dict__)
