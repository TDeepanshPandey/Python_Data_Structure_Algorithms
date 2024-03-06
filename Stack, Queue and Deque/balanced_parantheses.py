def balance_check(s):
    parentheses_opening = '[({'
    parentheses_closing = '})]'
    stack = []
    for i in list(s):
        if i in parentheses_opening:
            stack.append(i)
        if i in parentheses_closing:
            try:
                if i == ')':
                    stack.remove('(')
                if i == ']':
                    stack.remove('[')
                if i == '}':
                    stack.remove('{')        
            except:
                return False
    return len(stack) == 0


print(balance_check('[]'))

print(balance_check('[](){([[[]]])}'))

print(balance_check('()(){]}'))

"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""
from nose.tools import assert_equal

class TestBalanceCheck(object):
    
    def test(self,sol):
        assert_equal(sol('[](){([[[]]])}('),False)
        assert_equal(sol('[{{{(())}}}]((()))'),True)
        assert_equal(sol('[[[]])]'),False)
        print('ALL TEST CASES PASSED')
        
# Run Tests

t = TestBalanceCheck()
t.test(balance_check)