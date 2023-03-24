def division(a, b):
    if b == 0 : return ZeroDivisionError
    elif type(a) != int or type(b) != int : return TypeError
    else: return a/b

def make_negative( number ):
    return -number if number > 0 else number


"""
Can you find the needle in the haystack?
Write a function findNeedle() that takes an array full of junk but containing one "needle"
After your function finds the needle it should return a message (as a string) that says:
"found the needle at position " plus the index it found the needle, so:
Example(Input --> Output)
["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"] --> "found the needle at position 5"
"""
def find_needle(haystack):
    position = 3#99999999
    print(f"found the needle at position {position}")
    return position




### tests: ####################################################################################
def test_division():
    for divisible, divisor, expected in ((42, 2, 21), (-9, 2, -4.5), (0, 0, ZeroDivisionError), (0, "2", TypeError) ):
        actual = division(divisible, divisor)
        assert actual == expected, f"For {divisible}/{divisor}, expected {expected} but got {actual}"

def test_make_negative():
    for n, expected in ((42,-42), (-9,-9), (0,0)):
        actual = make_negative(n)
        assert actual == expected, f"For n = {n}, expected {expected} but got {actual}"

def test_find_needle():
    for haystack, expected in (
            (['3', '123124234', None, 'needle', 'world', 'hay', 2, '3', True, False], 3), # found the needle at position 3
            (['283497238987234', 'a dog', 'a cat', 'some random junk', 'a piece of hay', 'needle',
             'something somebody lost a while ago'], 5), # found the needle at position 5
            ([1, 2, 3, 4, 5, 6, 7, 8, 8, 7, 5, 4, 3, 4, 5, 6, 67, 5, 5, 3, 3, 4, 2, 34, 234, 23, 4, 234, 324, 324,
             'needle', 1, 2, 3, 4, 5, 5, 6, 5, 4, 32, 3, 45, 54], 30)): # found the needle at position 30
        actual = find_needle(haystack)
        assert actual == expected, f"For n = {haystack}, expected {expected} but got {actual}"



### run module ################################
if __name__ == '__main__':
    test_division()
    print("test division() ........... OK")

    test_make_negative()
    print("test make_negative() ...... OK")

    test_find_needle()
    print("test find_needle() ........ OK")

    test_division()