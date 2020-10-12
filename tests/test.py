import anon_func as af


def nested_function_test():
    value = 5

    new_func = af.func("", "return 'value'", collect_locals=True)
    value = 6
    print(new_func())
    return new_func


out = nested_function_test()

