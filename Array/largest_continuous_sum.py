""" 
def large_cont_sum(arr): 
    largest_sum = 0
    start = 0 
    end = 0
    for i in range(len(arr)+1):
        for j in range(i, len(arr)+1):
            temp = sum(arr[i:j])
            if temp > largest_sum:
                largest_sum = temp
                start = i
                end = j
    # print(start, end)
    return largest_sum """

def large_cont_sum(arr):
    if len(arr) == 0:
        return 0
    
    max_sum = current_sum = arr[0]

    for num in arr[1:]:
        current_sum = max(current_sum+num, num)

        max_sum = max(current_sum, max_sum)

    return max_sum

print(large_cont_sum([1,2,-1,3,4,10,10,-10,-1]))

from nose.tools import assert_equal

class LargeContTest(object):
    def test(self,sol):
        assert_equal(sol([1,2,-1,3,4,-1]),9)
        assert_equal(sol([1,2,-1,3,4,10,10,-10,-1]),29)
        assert_equal(sol([-1,1]),1)
        print('ALL TEST CASES PASSED')
        
#Run Test
t = LargeContTest()
t.test(large_cont_sum)