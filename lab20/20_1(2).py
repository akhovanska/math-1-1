import matplotlib.pyplot as plt


def func01(n):
    return ((n-1)**4-(n+2)**4)/((2* n +1 ) ** 3 + (n - 1) ** 3)


def gety(f, x):
    n = x.size
    y = np.zeros(n)
    for i in range(n):
        y[i] = f(x[i])
    return y


def vect(fgen, a, b, step=1):
    x = np.arange(a, b, step)
    y = np.zeros_like(x, dtype=float)
    gen = fgen(a, step)
    for i in range(x.size):
        y[i] = next(gen)
    return x, y


def plot_seq(x, y, b=None, eps=0.01, forall=True):
    if b is None:
        plt.plot(x, y, ".b")
        return y[-1]
    else:

        k = -1
        prev = False
        for i in range(y.size):
            if abs(y[i] - b) < eps:
                if not prev:
                    k = i
                    prev = True
            else:
                prev = False

        if not prev:
            return

        begin = 0 if forall else k


        plt.plot(x[begin:], y[begin:], ".b")
        plt.plot(np.array((x[begin], x[-1])), np.array((b, b)), "-r")
        plt.plot(np.array((x[begin], x[-1])), np.array((b - eps, b - eps)), "--g")
        plt.plot(np.array((x[begin], x[-1])), np.array((b + eps, b + eps)), "--g")
        # Підписуємо вісі
        plt.xlabel("n")
        plt.ylabel("a(n)")
        # Встановлюємо зріз ділянки, яка показує графік
        plt.axis([x[begin], x[-1], b - eps*2, b + eps*2])
        # Повертаємо номер останнього елемента послідовності,
        # який потрапив у проміжок за даним розбиттям
        return x[k]


if __name__ == "__main__":
    t = (1, 200, 1)  # параметри розбиття: (початок, кінець, крок)
    # x = np.arange(*t)
    # y = gety(func01, x)
    x, y = vect(func01_gen, *t)
    # print(x, y)
    # print(plot_seq(x, y))
    b = -1.3  # границя
    eps = 0.01
    print(plot_seq(x, y, b, eps, True))
    plt.show()
