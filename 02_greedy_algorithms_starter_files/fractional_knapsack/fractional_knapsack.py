# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    price = []
    value = 0.
    for i in range(n):
        price.append([values[i], weights[i]])

    price.sort(key=lambda x: -1.0*(x[0]/x[1]))


    for k in range(n):
        if capacity == 0:
            return value

        else:
            a = min(price[k][1], capacity)

            value += a * (1.0 * price[k][0] / price[k][1])

            capacity -= a

            price[k][1] -= a

    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.3f}".format(opt_value))

