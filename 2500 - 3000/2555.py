while True:
    string = input()
    v = str(float(string))
    it = list(str(int(float(string))))
    qwq = ['', 'S', 'B', 'Q', 'W', 'Y']
    QwQ = ['', 'W', 'Y']
    q = len(it) % 4
    if '-' in string:
        print('F', end='')
        if '-' in it:
            it.remove('-')
    if '+' in it:
        it.remove('+')

    any = []
    va = []
    it = list(reversed(it))
    q = len(it)//4
    cout0 = 0
    v123 = 1
    if int(float(string)) != 0:
        #  整数部分
        for i in range(q):
            for w in range(4):
                v0 = it[0]
                va.append(qwq[w])
                va.append(it[0])
                it.remove(v0)
                cout0 += 1
            any.append(va)
            va = []

            z = cout0 // 4
            any.append(list(QwQ[z]))

        for w in range(len(it)):

            v0 = it[0]
            va.append(qwq[w])
            va.append(it[0])
            it.remove(v0)

        any.append(va)
        va = []

        ans = []
        for i in any:
            for q in i:
                ans.append(q)
        ans = list(reversed(ans))

        while '' in ans:
            ans.remove('')

        qw = ans

        for i in range(len(ans)):
            if 0 < i < len(ans)-1 and ans[i] not in QwQ:
                v1, v2 = ans[i-1], ans[i+1]
                if v1 == '0':
                    qw[i] = ''
        while '' in qw:
            qw.remove('')

        ans = qw

        for i in range(len(qw)):
            if 0 < i < len(qw):
                v3 = qw[i-1]
                if v3 == qw[i] == '0':
                    ans[i-1] = ''
        if qw[-1] == '0':
            qw[-1] = ''

        while '' in ans:
            ans.remove('')

        if ans[0] in QwQ:
            ans.remove(ans[0])

        for i in range(len(ans)):
            if ans[i] in QwQ and ans[i-1] == '0':
                ans[i-1] = ''
        while '' in ans:
            ans.remove('')

        for i in range(len(ans)):
            if ans[i] in QwQ and ans[i-1] in QwQ:
                ans[i] = ''
        while '' in ans:
            ans.remove('')

        for i in ans:
            print(i, end='')


        #  整数部分
    else:
        v123 = -1

    if '.' in string and string[len(string) - 1] != '.':
        fl = string
        v4 = []
        for i in fl:
            v4.append(i)
        v4 = list(reversed(v4))
        v5 = []
        for i in v4:
            if i != '.':
                v5.append(i)
            else:
                v5.append('.')
                break
        v5 = list(reversed(v5))

        for i in v5:
            if i == '.' and v123 == -1:
                print('0D', end='')
            elif i == '.':
                print('D', end='')
            else:
                print(i, end='')
