class Node(object):
    
    def __init__(self,value):
        
        self.value = value
        self.nextnode = None

def cycle_check(node):
    cycle_check_flag = False
    while node.nextnode == None or node.nextnode == node:
        node = node.nextnode
        if node.nextnode == node:
            cycle_check_flag = True
        cycle_check(node)
    return cycle_check_flag

"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""
from nose.tools import assert_equal

# CREATE CYCLE LIST
a = Node(1)
b = Node(2)
c = Node(3)

a.nextnode = b
b.nextnode = c
c.nextnode = a # Cycle Here!


# CREATE NON CYCLE LIST
x = Node(1)
y = Node(2)
z = Node(3)

x.nextnode = y
y.nextnode = z


#############
class TestCycleCheck(object):
    
    def test(self,sol):
        assert_equal(sol(a),True)
        assert_equal(sol(x),False)
        
        print("ALL TEST CASES PASSED")
        
# Run Tests

t = TestCycleCheck()
t.test(cycle_check)
