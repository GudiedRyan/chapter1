import one_two as one_two

def test_permutation_1():
    assert one_two.check_if_permutation("listen", "silent") == True
def test_permutation_2():
    assert one_two.check_if_permutation("apples", "apple") == False