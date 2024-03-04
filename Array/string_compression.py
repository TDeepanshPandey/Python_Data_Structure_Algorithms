def compress(s):
    if len(s) == 0:
        return '' 
    res = []
    for i in sorted(set(s)):
        res.append(i)
        res.append(str(tuple(s).count(i)))
    return ''.join(res)

print(compress('AAAAABBBBCCCC'))

"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""
from nose.tools import assert_equal

class TestCompress(object):

    def test(self, sol):
        assert_equal(sol(''), '')
        assert_equal(sol('AABBCC'), 'A2B2C2')
        assert_equal(sol('AAABCCDDDDD'), 'A3B1C2D5')
        print('ALL TEST CASES PASSED')

# Run Tests
t = TestCompress()
t.test(compress)