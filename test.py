import pytest
from maxsubarray import Solution


@pytest.fixture
def s():
    yield Solution()


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([-1, 1, 2, -2], 3),
        ([-2, -1, 1, 2, -2], 3),
        ([-2, 1, 1, 2, -2], 4),
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
    ],
)
def test_brute_force(s, nums, expected):
    actual = s.brute_force(nums)
    assert expected == actual


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([-1, 1, 2, -2], 3),
        ([-2, -1, 1, 2, -2], 3),
        ([-2, 1, 1, 2, -2], 4),
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
    ],
)
def test_brute_force_cache(s, nums, expected):
    actual = s.brute_force_cache(nums)
    assert expected == actual


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([-1, 1, 2, -2], 3),
        ([-2, -1, 1, 2, -2], 3),
        ([-2, 1, 1, 2, -2], 4),
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
        ([1, 2, -1, 4], 6),
        ([-1], -1)
    ],
)
def test_slim(s, nums, expected):
    actual = s.slim(nums)
    assert expected == actual


@pytest.mark.parametrize(
    "nums, expected_sum, expected_start, expected_end",
    [
        ([-1, 1, 2, -2], 3, 1, 2),
        ([-2, -1, 1, 2, -2], 3, 2, 3),
        ([-2, 1, 1, 2, -2], 4, 1, 3),
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6, 3, 6),
        ([1, 2, -1, 4], 6, 0, 3),
        ([-1], -1, 0, 0)
    ],
)
def test_slim_with_indexes(s, nums, expected_sum, expected_start, expected_end):
    actual = s.slim_with_indexes(nums)
    assert expected_sum == actual[0]
    assert expected_start == actual[1]
    assert expected_end == actual[2]

@pytest.mark.parametrize(
    "nums, expected_sum",
    [
        ([-1, 1, 2, -2], 3),
        ([-2, -1, 1, 2, -2], 3),
        ([-2, 1, 1, 2, -2], 4),
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
        ([-1], -1),
        ([-2,-3,-1], -1),
        ([-1,-2,-3,0], 0),
        ([-1,0,-2,2], 2)
    ],
)
def test_split(s, nums, expected_sum):
    actual = s.divide(nums)
    assert expected_sum == actual
    # assert expected_start == actual[1]
    # assert expected_end == actual[2]

