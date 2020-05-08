"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

q = set(range(1, 10))
# q = set(range(1, 200))
# q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6


def sum_diff(num_set):
    alt_list = [f(x) for x in num_set]
    sum_dict = {}
    diff_dict = {}

    for num in alt_list:
        for num2 in alt_list:
            key = num + num2
            if key in sum_dict:
                sum_dict[key].append((num, num2))
            else:
                sum_dict[key] = [(num, num2)]

    for num in alt_list:
        for num2 in alt_list:
            key = num - num2
            if key < 0:
                pass
            elif key in diff_dict:
                diff_dict[key].append((num, num2))
            else:
                diff_dict[key] = [(num, num2)]

    print_list = []

    for key in sum_dict.keys():
        if key in diff_dict:
            for pair in sum_dict[key]:
                for pair2 in diff_dict[key]:
                    print_list.append(
                        f'{pair[0]} + {pair[1]} = {pair2[0]} - {pair2[1]}\n')

    print_string = ''.join(print_list)

    return print_string


print(sum_diff(q))
