def test(m1, m2):
    for i in m1:
        for j in m2:
            print(i, j, i + j)

test({'a', 'b'}, {'x', 'y', 'z'})