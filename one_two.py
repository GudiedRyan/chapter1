def check_if_permutation(string_a, string_b):
    list_a = []
    list_b = []
    list_a[:0] = string_a
    list_b[:0] = string_b
    list_a.sort()
    list_b.sort()
    if list_a == list_b:
        return True
    return False