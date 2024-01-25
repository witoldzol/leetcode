import pytest
from maxsubarray import Solution


@pytest.fixture
def s():
    yield Solution()

@pytest.mark.parametrize("nums, expected",[
    ([-1, 1, 2, -2], 3),
    ([-2, -1, 1, 2, -2], 3),
    ([-2, 1, 1, 2, -2], 4),
    ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
])
def test_brute_force(s, nums, expected):
    actual = s.brute_force(nums)
    assert expected == actual

@pytest.mark.parametrize("nums, expected",[
    ([-1, 1, 2, -2], 3),
    ([-2, -1, 1, 2, -2], 3),
    ([-2, 1, 1, 2, -2], 4),
    ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
])
def test_brute_force_cache(s, nums, expected):
    actual = s.brute_force_cache(nums)
    assert expected == actual

@pytest.mark.parametrize("nums, expected",[
    ([-1, 1, 2, -2], 3),
    ([-2, -1, 1, 2, -2], 3),
    ([-2, 1, 1, 2, -2], 4),
    ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
])
def test_brute_force_with_pointers(s, nums, expected):
    actual = s.brute_force_with_pointers(nums)
    assert expected == actual
# def test_divide_and_conquer(s):
#
#     nums = [-1, 1, 2, -2]
#     actual = s.maxSubArray(nums)
#     assert 3 == actual
#
#     nums = [-2, -1, 1, 2, -2]
#     actual = s.maxSubArray(nums)
#     assert 3 == actual
#
#     nums = [-2, 1, 1, 2, -2]
#     actual = s.maxSubArray(nums)
#     assert 4 == actual
#
#     nums = [-2, 1, 1, 2, -2]
#     actual = s.maxSubArray(nums)
#     assert 4 == actual
#
#     nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
#     actual = s.maxSubArray(nums)
#     assert 6 == actual
#
#     # nums = [1,-1,2,1]
#     # actual = s.maxSubArray(nums)
#     # assert 3 == actual
#     #
#     # nums = [-1,3,2,-1]
#     # actual = s.maxSubArray(nums)
#     # assert 5 == actual
