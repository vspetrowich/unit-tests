
def check_email(email: str) -> bool:
    if email.find('@') != -1:
        if len(email.split('@')) < 3:
            result = True
        else:
            return False
    if email.find(' ') == -1:
        result = True
    else:
        return False
    if email.find('.') != -1:
        if email[email.find('@') +1 ] != ".":
            result = True
        else:
            return False

    return result
    ...


if __name__ == '__main__':
    assert check_email('Helloworld@.ru') is False
    assert check_email('Helloworld@mi.ru') is True
    assert check_email('мояпочта@нетология.ру') is True
    assert check_email('python@email@net.ru') is False
    assert check_email(' em@il.ru') is False
    print("\nОтличная работа, отправляйте на проверку!")