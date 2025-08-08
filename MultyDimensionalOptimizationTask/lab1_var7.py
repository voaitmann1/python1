# variant 7

from scipy.optimize import fmin_powell

def whole_function(x1, x2):


    #return (8-x1)**2 - (7-x2)**2 + 3*(x2**2)
    return (8-x1)**2 - (7-x2)**2 + 3*(x2**4)


def calc_F1(x1):  # komponent 1 gradient

    return 2*x1 - 16


def calc_F2(x2):  # komponent 2 gradient

    #return - 2*x2 + 12*(x2**3) + 7
    return - 2*x2 + 12*(x2**3) + 14

def main():

    x1 = -3
    x2 = 5
    eps = 0.001
    gradF1 = calc_F1(x1)
    gradF2 = calc_F2(x2)
    alfa = fmin_powell(calc_F1, 0.5)
    M_iter = 100
    K_iter = 0

    for _ in range(M_iter): # golovnyi cycle
        K_iter += 1
        if abs(gradF1) <= eps and abs(gradF2) <= eps:  # perevirka
            break

        x1po = x1
        x2po = x2

        x1 = x1 - alfa*gradF1
        x2 = x2 - alfa*gradF2

        gradF1 = calc_F1(x1)
        gradF2 = calc_F2(x2)

        if x1po and x2po:
            if abs(x1-x1po)/abs(x1po) <= eps and abs(x2-x2po)/abs(x2po) <= eps:  #perevirka
                break

    print("Iterations:{}, x1 = {}, x2 = {}, alfa = {}, func = {}".format(
        K_iter, x1, x2, alfa, whole_function(x1, x2)))


if __name__ == '__main__':
    main()

# end of file
