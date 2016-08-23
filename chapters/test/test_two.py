from chapters import two as c2
import os
import pytest

test_mat = ['11000',
            '01100',
            '00101',
            '10001',
            '01011']

@pytest.mark.parametrize('test_input,expected', [
    ([], True),
    ([0], True),
    ([0,1,2,3,4,5,6,7,8,9,10], True),
    ([0,1,2,3,4,5,6,7,8,10,9], False),
    ('abcdefghijklmnopqrstuvwxyz', True),
    ('abcdefghijklmnopqrstuvwzyx', False),
    ('', True),
    (' ', True),
    ('  ', True)
])
def test_p2_is_sorted_recursive(test_input, expected):
    assert c2.p2_is_sorted_recursive(test_input) == expected


@pytest.mark.parametrize('test_input,expected', [
    (0, ['']),
    (1, ['0', '1']),
    (2, ['00', '01', '10', '11']),
    (3, ['000', '001', '010', '011', '100', '101', '110', '111'])
])
def test_p3_all_binary_sequences(test_input, expected):
    assert sorted(c2.p3_all_binary_sequences(test_input)) == sorted(expected)


def test_p5_find_largest_region_fill():
    assert c2.p5_find_largest_region_fill(test_mat) == 5


def test_p5_find_largest_region_eval():
    assert c2.p5_find_largest_region_eval(test_mat) == 5


@pytest.mark.parametrize('test_input,expected', [
    (2, 1),
    (4, 2),
    (8, 10),
    (16, 30),
    (32, 98),
    (64, 218),
    (128, 316)
])
def test_p5_find_largest_region_analog(test_input, expected):

    f = open(os.path.join(os.path.dirname(__file__), 'can', 'test_p5_find_largest_region_analog%d.txt' % test_input))
    m = [line.strip() for line in f]
    assert c2.p5_find_largest_region_fill(m) == expected
    assert c2.p5_find_largest_region_eval(m) == expected


def test_p5_find_largest_region_nested():

    m = ['111111111',
         '100000001',
         '101111101',
         '101000101',
         '101010101',
         '101000101',
         '101111101',
         '100000001',
         '111111111']
    assert c2.p5_find_largest_region_fill(m) == 32
    assert c2.p5_find_largest_region_eval(m) == 32







