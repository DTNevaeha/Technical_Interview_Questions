## Given 2 values, find the path to the first value in the second value.
## If the value occurs more than once, print each value, else None.

# Value1 = what am I looking for, Value2 = the path on how to find it
def find_path(value1, value2) -> list:
    if value1 == value2:
        return []
    elif type(value2) is dict:
        for key, val in value2.items():
            if val == value1:
                return [key]
            else:
                path = find_path(value1, val)
                if path is not None:
                    return [key] + path
        return None
    elif type(value2) is list:
        for index, item in enumerate(value2):
            if item == value1:
                return [index]
            else:
                path = find_path(value1, item)
                if path is not None:
                    return [index] + path
        return None
    else:
        return None


# Do some simple tests.
print(f'{find_path(["Hello world"], [23,["Hello world"],45])=}')  # [1]
print(f'{find_path("Hello world", ["Hello world"])=}')  # [0]
print(f'{find_path(56, [1,2,3,{"sd": [56]},"Hello world"])=}')  # [3, 'sd', 0]
print(f'{find_path(56, [1,2,3,{"sd": [56]}, 56])=}')  # [3, 'sd', 0]
print(f'{find_path("Hello world", [1,2,3,["John", "Hello world"], 492])=}')  # [3, 1]
print(f"find_path(56, 56)")  # []
print(f"find_path(56, 57)")  # None
