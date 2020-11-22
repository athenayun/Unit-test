
def reverse_dict(input_value):
    out = {}
    for k1, subdict_1 in input_value.items():
        for k2, subdict_2 in subdict_1.items():
            for k3, subdict_3 in subdict_2.items():
                for k4, k5 in subdict_3.items():
                    out = {k5:{k4:{k3:{k2:k1}}}}
    return out
