from src.polindrom import solve
import pytest

@pytest.mark.parametrize('phrases, true_list',
                         ((["нажал кабан на баклажан", "дом как комод", "рвал дед лавр"],\
                           ["нажал кабан на баклажан", "рвал дед лавр"]),
                         (["нажал кабан на баклажан", "азот калий и лактоза", "пуст суп"],\
                          ["нажал кабан на баклажан", "азот калий и лактоза", "пуст суп"]),
                        (["дом как комод", "карман мрак"], []) )
                           )
def test_solve(phrases, true_list):
    assert solve(true_list) == true_list, \
    f'Ответ: {len(solve(true_list))} правильных ответа из {len(solve(true_list))}'

