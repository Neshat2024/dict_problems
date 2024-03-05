# Input : {'a': {'b': {'c': {}}}, 'd': {'e': {}}, 'f': {'g': {'h': {'i': {}}}}}
# Output : {'c': {'b': {'a': {}}}, 'e': {'d': {}}, 'i': {'h': {'g': {'f': {}}}}}

test_dict = {'a': {'b': {'c': {}}}, 'd': {'e': {}}, 'f': {'g': {'h': {'i': {}}}}}
list_of_dicts = [{key: value} for key, value in test_dict.items()]


def vars_of_dicts(dictionary):
    for key, value in dictionary.items():
        list_of_keys.append(key)
    if type(value) == dict:
        check_key = [i for i in value.keys()]
        if check_key == []:
            return list_of_keys
        return vars_of_dicts(value)
    return list_of_keys


main_dict = {}
for i in list_of_dicts:
    list_of_keys = []
    vars_of_dicts(i)
    count = len(list_of_keys)
    new_dict = {}
    for j in range(count):
        check_key = [i for i in new_dict.keys()]
        if check_key == []:
            new_dict[list_of_keys[j]] = {}
        else:
            other_keys = [i for i in new_dict.keys()]
            new_dict[list_of_keys[j]] = dict(new_dict)
            new_dict.pop(other_keys[0])
    main_dict.update(new_dict)

print(main_dict)
