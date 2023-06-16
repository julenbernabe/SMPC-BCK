import random

def takeSecond(l):
    return l[1]

def grouping(M: list, C: int):
    # Result initialization
    R = []
    # For bins that do not reach bin capacity C
    nC = []

    # STEP 1

    # Compute v_i = w_i/C
    for elem in M:
        elem[1] = elem[1] / C
    # Sort in decreasing order
    M.sort(key = takeSecond, reverse=True)

    # STEP 2

    # The v_i >= 1 are placed in separate bins
    while len(M) > 1 and M[0][1] >= 1:
        r = [M.pop(0), M.pop(-1)]
        R.append(r)
        
    # STEP 3

    # Split the remaining v_i in X, Y and Z sublists
    X = []
    Y = []
    Z = []
    while len(M) > 0 and M[0][1] >= 0.5:
        X.append(M.pop(0))
    # Order X so that players with same data length but greater reputation go first
    if len(X) > 0:
        X.sort(key = lambda x: (-x[1], -x[2]))
    while len(M) > 0 and M[0][1] >= (1/3):
        Y.append(M.pop(0))
    # Order Y so that players with same data length but greater reputation go first
    if len(Y) > 0:
        Y.sort(key = lambda x: (-x[1], -x[2]))
    if len(M) > 0:
        for elem in M:
            Z.append(elem)
    # Order Z so that players with same data length but greater reputation go last
    if len(Z) > 0:
        Z.sort(key = lambda x: (-x[1], x[2]))


    # STEP 4

    # New bins from X, Y, Z while XUY or Z are non-empty lists
    R, r, c, len_XUY = step4(R, C, X, Y, Z)
    # STEP 5

    # Three cases: len(XUY) = 1, len(XUY) = 0 and len(Z) = 0
    # Case 1: len(XUY) = 1
    if len_XUY == 1:
        # Case 1.1: X is non-empty (or Y is empty) and last bin is unfilled --> Fill r from X
        if len(X) > 0 and c < 1:
            c += X[0][1]
            r.append(X.pop(0))
            len_XUY -= 1
            while c < 1:
                if len(Z) > 0:
                    c += Z[-1][1]
                    r.append(Z.pop(-1))
                else:
                    # In nC store capacity of r (does not reach C) and position in R
                    nC.append([c, len(R)])
                    break
            R.append(r)
            while len(Z) > 0:
                c = Z[-1][1]
                r = [Z.pop(-1)]
                while c < 1:
                    if len(Z) > 0:
                        c += Z[-1][1]
                        r.append(Z.pop(-1))
                    else:
                        nC.append([c, len(R)])
                        break
                R.append(r)
        # Case 1.2: X is non-empty (or Y is empty) and last bin is filled --> New bin from X
        elif len(X) > 0 and c >= C:
            c = X[0][1]
            r = [X.pop(0)]
            len_XUY -= 1
            while c < 1:
                if len(Z) > 0:
                    c += Z[-1][1]
                    r.append(Z.pop(-1))
                else:
                    nC.append([c, len(R)])
                    break
            R.append(r)
            while len(Z) > 0:
                c = Z[-1][1]
                r = [Z.pop(-1)]
                while c < 1:
                    if len(Z) > 0:
                        c += Z[-1][1]
                        r.append(Z.pop(-1))
                    else:
                        nC.append([c, len(R)])
                        break
                R.append(r)
        # Case 1.3: X is empty (or len(Y) = 1) and last bin is unfilled --> Fill r from Y
        elif len(Y) == 1 and c < 1:
            c += Y[0][1]
            r.append(Y.pop(0))
            len_XUY -= 1
            while c < 1:
                if len(Z) > 0:
                    c += Z[-1][1]
                    r.append(Z.pop(-1))
                else:
                    nC.append([c, len(R)])
                    break
            R.append(r)
            while len(Z) > 0:
                c = Z[-1][1]
                r = [Z.pop(-1)]
                while c < 1:
                    if len(Z) > 0:
                        c += Z[-1][1]
                        r.append(Z.pop(-1))
                    else:
                        nC.append([c, len(R)])
                        break
                R.append(r)
        # Case 1.4: X is empty (or len(Y) = 1) and last bin is filled --> New bin from Y
        elif len(Y) == 1 and c >= C:
            c = Y[0][1]
            r = [Y.pop(0)]
            len_XUY -= 1
            while c < 1:
                if len(Z) > 0:
                    r.append(Z.pop(-1))
                else:
                    nC.append([c, len(R)])
                    break
            R.append(r)
            while len(Z) > 0:
                c = Z[-1][1]
                r = [Z.pop(-1)]
                while c < 1:
                    if len(Z) > 0:
                        c += Z[-1][1]
                        r.append(Z.pop(-1))
                    else:
                        nC.append([c, len(R)])
                        break
                R.append(r)

    # Case 2: len(XUY) = 0 (both X and Y are empty)
    elif len_XUY == 0:
        # Case 2.1: Last bin is unfilled --> Fill bin from Z
        if c < 1:
            while c < 1:
                if len(Z) > 0:
                    r.append(Z.pop(-1))
                else:
                    nC.append([c, len(R)])
                    break
            R.append(r)
            while len(Z) > 0:
                c = Z[-1][1]
                r = [Z.pop(-1)]
                while c < 1:
                    if len(Z) > 0:
                        c += Z[-1][1]
                        r.append(Z.pop(-1))
                    else:
                        nC.append([c, len(R)])
                        break
                R.append(r)
        # Case 2.2: Last bin is filled --> Fill bin from Z
        elif c > 1:
            while len(Z) > 0:
                c = Z[-1][1]
                r = [Z.pop(-1)]
                while c < 1:
                    if len(Z) > 0:
                        c += Z[-1][1]
                        r.append(Z.pop(-1))
                    else:
                        nC.append([c, len(R)])
                        break
                R.append(r)

    # Case 3: len(Z) = 0 (Z is empty)
    if len(Z) == 0:
        # Case 3.1: Last bin is unfilled and len(X) > 2 --> Fill bin from X
        if c < 1 and len(X) >= 2:
            for i in range (2):
                c += X[0][1]
                r.append(X.pop(0))
            R.append(r)
            while len(X) >= 2:
                c = 0
                r = []
                for i in range (2):
                    c += X[0][1]
                    r.append(X.pop(0))
                R.append(r)
            while len(Y) >= 3:
                c = 0
                r = []
                for i in range (3):
                    c += Y[0][1]
                    r.append(Y.pop(0))
                R.append(r)
            c = 0
            r = []
            if len(X) > 0:
                c += X[0][1]
                r.append(X.pop(0))
            while len(Y) > 0:
                c += Y[0][1]
                r.append(Y.pop(0))
            if c < 1:
                nC.append([c, len(R)])
            R.append(r)
        # Case 3.2: Last bin is unfilled and len(Y) > 3 --> Fill bin from Y
        elif c < 1 and len(Y) >= 3:
            for i in range (3):
                c += Y[0][1]
                r.append(Y.pop(0))
            R.append(r)
            while len(X) >= 2:
                c = 0
                r = []
                for i in range (2):
                    c += X[0][1]
                    r.append(X.pop(0))
                R.append(r)
            while len(Y) >= 3:
                c = 0
                r = []
                for i in range (3):
                    c += Y[0][1]
                    r.append(Y.pop(0))
                R.append(r)
            c = 0
            r = []
            if len(X) > 0:
                c += X[0][1]
                r.append(X.pop(0))
            while len(Y) > 0:
                c += Y[0][1]
                r.append(Y.pop(0))
            if c < 1:
                nC.append([c, len(R)])
            R.append(r)
        # Case 3.3: Last bin is filled --> Fille new bins from X and Y
        elif c > 1:
            while len(X) >= 2:
                c = 0
                r = []
                for i in range (2):
                    c += X[0][1]
                    r.append(X.pop(0))
                R.append(r)
            while len(Y) >= 3:
                c = 0
                r = []
                for i in range (3):
                    c += Y[0][1]
                    r.append(Y.pop(0))
                R.append(r)
            c = 0
            r = []
            if len(X) > 0:
                c += X[0][1]
                r.append(X.pop(0))
            while len(Y) > 0:
                c += Y[0][1]
                r.append(Y.pop(0))
            if c < 1:
                nC.append([c, len(R)])
            R.append(r)
    return R, nC


def step4(R: list, C: int, X: list, Y: list, Z: list):
    len_XUY = len(X) + len(Y)
    while len_XUY > 1  and len(Z) > 0:
        if len(X) > 1 and len(Y) > 2:
            if X[0][1] >= Y[0][1] + Y[1][1]:
                c = X[0][1]
                r = [X.pop(0)]
                len_XUY -= 1
                while c < 1:
                    if len(Z) > 0:
                        c += Z[-1][1]
                        r.append(Z.pop(-1))
                    elif len(Y) > 0:
                        c += Y[-1][1]
                        r.append(Y.pop(-1))
                    else:
                        return R, r, c, len_XUY
                R.append(r)
            else:
                c = Y[0][1] + Y[1][1]
                r = [Y.pop(0), Y.pop(0)]
                len_XUY -= 2
                while c < 1:
                    if len(Z) > 0:
                        c += Z[-1][1]
                        r.append(Z.pop(-1))
                    elif len(Y) > 0:
                        c += Y[-1][1]
                        r.append(Y.pop(-1))
                    else:
                        return R, r, c, len_XUY
                R.append(r)
        elif len(X) >= 1:
            c = X[0][1]
            r = [X.pop(0)]
            len_XUY -= 1
            while c < 1:
                if len(Z) > 0:
                    c += Z[-1][1]
                    r.append(Z.pop(-1))
                elif len(Y) > 0:
                    c += Y[-1][1]
                    r.append(Y.pop(-1))
                else:
                    return R, r, c, len_XUY
            R.append(r)
        elif len(Y) >= 2:
            c = Y[0][1] + Y[1][1]
            r = [Y.pop(0), Y.pop(0)]
            len_XUY -= 2
            while c < 1:
                if len(Z) > 0:
                    c += Z[-1][1]
                    r.append(Z.pop(-1))
                elif len(Y) > 0:
                    c += Y[-1][1]
                    r.append(Y.pop(-1))
                else:
                    return R, r, c, len_XUY
            R.append(r)
            
    return R, [], 0, len_XUY

# Functions below are for testing that the grouping function works properly
def generate(n = 25):
    M = []
    for i in range (n):
        r = []
        for j in range (3):
            r.append(random.randint(1, 10))
        M.append(r)
    return M

def capacity(r: list):
    c = 0
    for elem in r:
        c += elem[1]
    return c

# M = generate(2)
# # Add scientist to the list
# M.append(['c', 0, 0])
# R, nC = grouping(M, 11)
# print('R:', R)
# print('nC:', nC)