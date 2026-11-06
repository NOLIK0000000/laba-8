class MatrixLayers:
    def __init__(self, a):
        self.a = a
        self.n = len(a)
        self.m = len(a[0])

    def count_layers(self):
        x = self.n // 2
        y = self.m // 2
        if x < y:
            return x
        return y

    def layer_coords(self, num):
        top = num
        left = num
        bot = self.n - 1 - num
        right = self.m - 1 - num
        res = []
        j = left
        while j <= right:
            res.append((top, j))
            j += 1
        i = top + 1
        while i <= bot:
            res.append((i, right))
            i += 1
        j = right - 1
        while j >= left:
            res.append((bot, j))
            j -= 1
        i = bot - 1
        while i > top:
            res.append((i, left))
            i -= 1
        return res

    def task_12_1(self):
        p = self.count_layers()
        new_a = []
        for row in self.a:
            new_row = []
            for x in row:
                new_row.append(x)
            new_a.append(new_row)
        for num in range(p):
            coords = self.layer_coords(num)
            cnt = len(coords)
            step = p - num
            step = step % cnt
            vals = []
            for c in coords:
                vals.append(self.a[c[0]][c[1]])
            if step != 0:
                new_vals = []
                for i in range(cnt - step, cnt):
                    new_vals.append(vals[i])
                for i in range(0, cnt - step):
                    new_vals.append(vals[i])
            else:
                new_vals = vals
            for k in range(cnt):
                ii = coords[k][0]
                jj = coords[k][1]
                new_a[ii][jj] = new_vals[k]
        return new_a

    def task_12_2(self):
        p = self.count_layers()
        new_a = []
        for row in self.a:
            new_row = []
            for x in row:
                new_row.append(x)
            new_a.append(new_row)
        for num in range(p):
            coords = self.layer_coords(num)
            for c in coords:
                new_a[c[0]][c[1]] = num + 1
        return new_a

    def task_12_3(self):
        p = self.count_layers()
        res = []
        for num in range(p):
            coords = self.layer_coords(num)
            s = 0
            for c in coords:
                s = s + self.a[c[0]][c[1]]
            res.append(s)
        return res

    def task_12_4(self):
        p = self.count_layers()
        res = []
        for num in range(p):
            coords = self.layer_coords(num)
            mn = None
            mx = None
            for c in coords:
                v = self.a[c[0]][c[1]]
                if mn is None:
                    mn = v
                    mx = v
                else:
                    if v < mn:
                        mn = v
                    if v > mx:
                        mx = v
            res.append(mx - mn)
        return res

def print_mat(a, text):
    print(text)
    for i in range(len(a)):
        s = "  "
        for j in range(len(a[i])):
            s = s + str(a[i][j]) + " "
        print(s)
    print()

print("Введите N и M:")
stroka = input()
chasti = stroka.split()
n = int(chasti[0])
m = int(chasti[1])
print("Введите", n, "строк по", m, "чисел:")
mat = []
for i in range(n):
    s = input()
    ch = s.split()
    row = []
    for x in ch:
        row.append(float(x))
    mat.append(row)
obj = MatrixLayers(mat)
print_mat(mat, "Исходная матрица:")
print("Слоёв:", obj.count_layers())
print("12.3 Суммы:", obj.task_12_3())
print("12.4 Размахи:", obj.task_12_4())
print_mat(obj.task_12_2(), "12.2 Заполнение:")
print_mat(obj.task_12_1(), "12.1 Поворот:")