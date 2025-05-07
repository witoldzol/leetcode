from typing import Any
from flatten_dict import flatten

def my_flatten(input:dict, separator = '/', parent = '') -> list[tuple[str,Any]]:
    result = []
    for k,v in input.items():
        key = f"{parent}{separator}{k}" if parent else str(k)
        if isinstance(v, dict):
            result.extend(my_flatten(v,separator = '/', parent = key))
        else:
            result.append((key,v))
    return result 

def test_simple():
    expected = {"a":1}
    input = {"a":1}
    result = my_flatten(input)
    expected = flatten(input, reducer='path')
    assert expected == dict(result)

def test_one_nested():
    input = {"a":1, "b":{"c":3} }
    expected = flatten(input, reducer='path')
    actual = my_flatten(input)
    assert expected == dict(actual)

def test_nested_dict_in_list():
    input = {"a":1, "b":[{"c":3}] }
    expected = flatten(input, reducer='path')
    actual = my_flatten(input)
    assert expected == dict(actual)

def test_nested_dict_in_list_two():
    input = {"a":1, "b":[[{"c":3}]] }
    expected = flatten(input, reducer='path')
    actual = my_flatten(input)
    assert expected == dict(actual)

def test_nested_list():
    input = {"a":1, "b":{"c":3, "d": [1]} }
    expected = flatten(input, reducer='path')
    actual = my_flatten(input)
    assert expected == dict(actual)

def test_nested_list_2():
    input = {"a":1, "b":{"c":3, "d": [1, 2, 3]} }
    expected = flatten(input, reducer='path')
    print(expected)
    actual = my_flatten(input)
    assert expected == dict(actual)

def test_nested_list_3():
    input = {"a":1, "b":{"c":3, "d": [1, 2, {"e":3}]} }
    expected = flatten(input, reducer='path')
    print(expected)
    actual = my_flatten(input)
    assert expected == dict(actual)
