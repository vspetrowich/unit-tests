
from src.discrim import solution
import pytest

@pytest.mark.parametrize('a, b, c, list1',
                         ((1, 8, 15, [-3.0, -5.0]),
                          (5, -8, 3, [1.0, 0.6]),
                          (1, -13, 12, [12.0, 1.0]),
                          (-4, 28, -49, [3.5]),
                          (2, -5, 2, [2.0, 0.5]),
                          (1, 1, 1, [] ) ) )
def test_solution(a, b, c, list1):
    assert solution(a, b, c) == list1, \
    f'Корни уравнения: {list1}'

