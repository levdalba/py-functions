# 1
def calculate_area(length, width):
    return length * width


# print(calculate_area(4, 5))


# 2
def format_greeting(name, greeting="Hello"):
    return f"{greeting}, {name}"


# print(format_greeting("John"))


# 3
def calculate_volume(length, width, height):
    return length * width * height


# print(calculate_volume(1, 2, 3))


# 4
def generate_url(domain, protocol="http", path="/"):
    return f"{protocol}://www.{domain}.{path}"


# print(generate_url("google", "https", "com"))


# 5
def calculate_total_cost(base_price, num, discount=0):
    return (base_price * num) * (1 - discount)


# print(calculate_total_cost(5, 5, 0.1))


# 6
def join_strings(separator=",", *args):
    return separator.join(args)


# print(join_strings(":", "a", "b", "c"))


# 7
def create_dict(key, value):
    return {key: value}


# print(create_dict("a", 1))


# 8
def calculate_bmi(weight, height):
    return weight / (height**2)


# print(calculate_bmi(71, 1.8))


# 9
def calculate_interest(principal, rate, time):
    return principal * (1 + rate) ** time


# print(calculate_interest(1000, 0.1, 5))


# 10
def join_strings(separator=",", *args, uppercase=False):
    joined = separator.join(args)
    if uppercase:
        return joined.upper()
    return joined


# print(join_strings(":", "a", "b", "c", uppercase=True))


# Custom mapping functions


# 1
def custom_map(f, lst):
    return [f(x) for x in lst]


# print(custom_map(lambda x: x**2, [1, 2, 3, 4, 5]))


# 2
def custom_filter(predicate, lst):
    if predicate:
        return [x for x in lst if predicate(x)]


# print(custom_filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5]))


# 3
def custom_reduce(func, initial, lst):
    result = initial
    for x in lst:
        result = func(result, x)
    return result


# print(custom_reduce(lambda x, y: x + y, 0, [1, 2, 3, 4, 5]))


# 4
def func(f, g):
    return lambda x: f(g(x))


# print(list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5]))))


# 5
def map_and_filter(map_func, filter_func, lst):
    return list(map(map_func, filter(filter_func, lst)))


# print(map_and_filter(lambda x: x**2, lambda x: x % 2 == 0, [1, 2, 3, 4, 5]))


# 6
def custom_sort(list, comparison):
    for i in range(len(list)):
        for j in range(i + 1, len(list)):
            if comparison(list[i], list[j]):
                list[i], list[j] = list[j], list[i]
    return list


# print(custom_sort([1, 2, 3, 4, 5], lambda x, y: x > y))


# 7


def custom_group_by(list, key_func):
    result = {}
    for x in list:
        key = key_func(x)
        if key not in result:
            result[key] = []
        result[key].append(x)
    return result


# print(custom_group_by([1, 2, 3, 4, 5], lambda x: x % 2 == 0))


# 8
def custom_transform(list, transform_func):
    return [transform_func(x) for x in list]


# print(custom_transform([1, 2, 3, 4, 5], lambda x: x**2))


# 9
def custom_filter_with_index(lst, predicate_func):
    return [x for i, x in enumerate(lst) if predicate_func(i, x)]


# print(custom_filter_with_index([1, 2, 3, 4, 5], lambda i, x: i % 2 == 0 and x % 2 == 0))


# 10
def custom_accumulate(lst, acc_func):
    result = []
    for i, x in enumerate(lst):
        result.append(acc_func(i, x))
    return result


# print(custom_accumulate([1, 2, 3, 4, 5], lambda i, x: i + x))
