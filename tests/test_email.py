#-*- coding: utf-8 -*-
from src.email import check_email
import pytest
@pytest.mark.parametrize('email, expected_email',
                         (('Helloworld@.ru', False ),
                          ('Helloworld@mi.ru', True ),
                          ('мояпочта@нетология.ру', True ),
                          ('python@email@net.ru', False ),
                          (' em@il.ru', False)  ) )
def test_check_email(email, expected_email):
    assert check_email(email) == expected_email, \
    f'Email введён неправильно {email}'

