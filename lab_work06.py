try:        #предотвращение ошибки, если пользователь введет не цифру
    n = int(input('Введите количество критериев: '))
    set_k = []
    for i in range(1, n + 1):  # создание матрицы
        k = 'k'
        c = k + str(i)
        set_k.append(c)
    # print(set_k)

    for i in range(n):  # создание единичных списков
        set_k[i] = []
        for j in range(n):
            set_k[i].append(1.0)
    # print(set_k)

    for i in range(2, n + 1):  # добавление данных пользователя
        for j in range(1, i):
            x = float(input('Введите отношение важности для ' + str(j) + ' критерия к ' + str(i) + ' критерию: '))
            set_k[i - 1][j - 1] = x
    # print(set_k)

    for i in range(n - 2, -1, -1):  # отзеркаливание введенных данных пользователя
        for j in range(i, -1, -1):
            set_k[j][i + 1] = float("{0:.2f}".format(1.0 / set_k[i + 1][j]))
            # set_k[j][i + 1] = 1.0 / set_k[i + 1][j]
            # print(j, i + 1)
    # print(set_k)

    pr = []
    sum = 0
    for i in range(n):  # вычисление сумм строк
        m = 0
        for j in range(n):
            m += set_k[i][j]
            sum += set_k[i][j]
        pr.append(m)
    # print(pr)
    # print(sum)

    for i in range(n):
        otv = pr[i] / sum
        print('Весовой коэффициент для ' + str(i + 1) + ' критерия: ' + str(float("{0:.2f}".format(otv))))
except ValueError:
    a = 1
    print('Ошибка, Вы ввели не цифру')

while a == 1:
    try:
        n = int(input('Введите количество критериев: '))
        set_k = []
        for i in range(1, n + 1):  # создание матрицы
            k = 'k'
            c = k + str(i)
            set_k.append(c)
        # print(set_k)

        for i in range(n):  # создание единичных списков
            set_k[i] = []
            for j in range(n):
                set_k[i].append(1.0)
        # print(set_k)

        for i in range(2, n + 1):  # добавление данных пользователя
            for j in range(1, i):
                x = float(input('Введите отношение важности для ' + str(j) + ' критерия к ' + str(i) + ' критерию: '))
                set_k[i - 1][j - 1] = x
        # print(set_k)

        for i in range(n - 2, -1, -1):  # отзеркаливание введенных данных пользователя
            for j in range(i, -1, -1):
                set_k[j][i + 1] = float("{0:.2f}".format(1.0 / set_k[i + 1][j]))
                # set_k[j][i + 1] = 1.0 / set_k[i + 1][j]
                # print(j, i + 1)
        # print(set_k)

        pr = []
        sum = 0
        for i in range(n):  # вычисление сумм строк
            m = 0
            for j in range(n):
                m += set_k[i][j]
                sum += set_k[i][j]
            pr.append(m)
        # print(pr)
        # print(sum)

        for i in range(n):
            otv = pr[i] / sum
            print('Весовой коэффициент для ' + str(i + 1) + ' критерия: ' + str(float("{0:.2f}".format(otv))))
    except ValueError:
        a = 1
        print('Ошибка, Вы ввели не цифру')
