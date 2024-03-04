""" def rev_word(s):
    temp = s.split(' ')
    temp = [char for char in temp if char != ' ' if char != '']
    temp.reverse()
    return ' '.join(temp) """

def rev_word(s):
    return " ".join(reversed(s.split()))

print(rev_word('Hi John,   are you ready to go?'))

print(rev_word('    space before'))

"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""

from nose.tools import assert_equal

class ReversalTest(object):
    
    def test(self,sol):
        assert_equal(sol('    space before'),'before space')
        assert_equal(sol('space after     '),'after space')
        assert_equal(sol('   Hello John    how are you   '),'you are how John Hello')
        assert_equal(sol('1'),'1')
        print("ALL TEST CASES PASSED")
        
# Run and test
t = ReversalTest()
t.test(rev_word)