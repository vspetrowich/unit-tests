from src.yandex_folder import create_yandex_folder
import pytest

#id_yandex = input('укажите Ваш OAuth-токен: ')
itog = {
    201 : 'Папка успешно создана',
    409 : 'Папка уже существует',
    401 : 'Ошибка доступа неверный ID'
}
id_yandex = 'Укажите тут Ваш Яндекс-ID' #Для автоматического теста необходимо указать ID


@pytest.mark.parametrize('id_yandex, status_code',
                         ((id_yandex, 201 ),
                         (id_yandex, 409 ),
                         ('y0__37585jujhjehfhfhjhjrhfjrjjji23ujk5948610i85o18j41', 401 )
                           ) )
def test_create_yandex_folder(id_yandex, status_code):
    assert create_yandex_folder(id_yandex) == status_code, \
    f'Результат: {create_yandex_folder(id_yandex)} {itog[create_yandex_folder(id_yandex)]}'