class MatrixLayers:
    def __init__(self, a):
        self.a = a
        self.n = len(a)
        self.m = len(a[0])

    def p(self):
        return min(self.n // 2, self.m // 2)

    def coords(self, k):
        t = l = k
        b = self.n - 1 - k
        r = self.m - 1 - k
        res = []
        for j in range(l, r + 1):
            res.append((t, j))
        for i in range(t + 1, b + 1):
            res.append((i, r))
        for j in range(r - 1, l - 1, -1):
            res.append((b, j))
        for i in range(b - 1, t, -1):
            res.append((i, l))
        return res

    def t1(self):
        p = self.p()
        b = [row[:] for row in self.a]
        for k in range(p):
            c = self.coords(k)
            vals = [self.a[i][j] for i, j in c]
            s = (p - k) % len(c)
            nv = vals[-s:] + vals[:-s] if s else vals
            for x in range(len(c)):
                b[c[x][0]][c[x][1]] = nv[x]
        return b

    def t2(self):
        p = self.p()
        b = [row[:] for row in self.a]
        for k in range(p):
            for i, j in self.coords(k):
                b[i][j] = k + 1
        return b

    def t3(self):
        return [sum(self.a[i][j] for i, j in self.coords(k)) for k in range(self.p())]

    def t4(self):
        res = []
        for k in range(self.p()):
            v = [self.a[i][j] for i, j in self.coords(k)]
            res.append(max(v) - min(v))
        return res


def show(a, t):
    print(t)
    for r in a:
        print("  ", r)
    print()


n, m = map(int, input("N M: ").split())
print("Введите", n, "строк:")
mat = [list(map(float, input().split())) for _ in range(n)]

o = MatrixLayers(mat)
show(mat, "Исходная:")
print("Слоёв:", o.p())
print("12.3 Суммы:", o.t3())
print("12.4 Размахи:", o.t4())
show(o.t2(), "12.2 Заполнение:")
show(o.t1(), "12.1 Поворот:")