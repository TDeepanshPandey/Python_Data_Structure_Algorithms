""" 
def anagram(s1,s2):
    tmp1 =list(s1)
    tmp1.sort()
    tmp1 = [char for char in tmp1 if char != ' ']
    tmp2 = list(s2)
    tmp2.sort()
    tmp2 = [char for char in tmp2 if char != ' ']
    if tmp1 == tmp2:
        return True
    else:
        return False """
    
def anagram(s1, s2):
    s1 = s1.replace(' ','').lower()
    s2 = s2.replace(' ','').lower()
    return sorted(s1) == sorted(s2)

print(anagram('dog','god'))
print(anagram('clint eastwood','old west action'))
print(anagram('aa','bb'))

"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""
from nose.tools import assert_equal

class AnagramTest(object):
    
    def test(self,sol):
        assert_equal(sol('go go go','gggooo'),True)
        assert_equal(sol('abc','cba'),True)
        assert_equal(sol('hi man','hi     man'),True)
        assert_equal(sol('aabbcc','aabbc'),False)
        assert_equal(sol('123','1 2'),False)
        print("ALL TEST CASES PASSED")

# Run Tests
t = AnagramTest()
t.test(anagram)