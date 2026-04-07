def stvorec(_vel, _farba):
    t.setpc(_farba)
    for repc in range(1, 5):
        t.fd(_vel)
        t.rt(90)