from flatten_json import flatten

nested_json = {
    "a": 1,
    "b": {"c": 2, "d": [3, 4]},
    "e": [{"f": 5}, {"g": 6}]
}
flat = flatten(nested_json)
def my_flatten(data, parent_key='', separator='.') -> list:
    items = []
    for key, value in data.items() if isinstance(data,dict) else enumerate(data):
        new_key = f"{parent_key}{separator}{key}" if parent_key else str(key)
        if isinstance(value,(dict,list)):
            items.extend(my_flatten(value, new_key, separator))
        else:
            items.append((new_key,value))
    return dict(items)

def dd(data, parent_key='', sep='.'):
    items = []
    for key, value in data.items() if isinstance(data, dict) else enumerate(data):
        new_key = f"{parent_key}{sep}{key}" if parent_key else str(key)
        if isinstance(value, (dict, list)):
            items.extend(dd(value, new_key, sep))
        else:
            items.append((new_key, value))
    return dict(items)

my_flat = dd(nested_json)
assert flat == my_flat, f"{flat} \n does not match \n {my_flat}"

