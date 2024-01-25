from maxsubarray import Solution

def test_divide_and_conquer():
    s = Solution()
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    actual = s.maxSubArray(nums)
    assert 6 == actual

    nums = [1,-1,2,1]
    actual = s.maxSubArray(nums)
    assert 3 == actual

    nums = [-1,3,2,-1]
    actual = s.maxSubArray(nums)
    assert 5 == actual

