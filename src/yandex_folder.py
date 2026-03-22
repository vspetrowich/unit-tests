import requests

def create_yandex_folder(id_yandex: str) -> int:
    # создаём папку на яндекс диске
    params = {'path': 'test'}
    headers ={'Authorization': f'OAuth {id_yandex}'}
    response = requests.put('https://cloud-api.yandex.net/v1/disk/resources', headers=headers, params=params)
    #print(response.status_code)
    result = response.status_code
    return result

if __name__ == '__main__':
    # словарь ошибок
    itog = {
        201: 'Папка успешно создана',
        409: 'Папка уже существует',
        401: 'Ошибка доступа неверный ID'
    }
    # Авторизация яндекс
    id_yandex = input('укажите Ваш OAuth-токен: ')
    # Создаём папку
    assert create_yandex_folder(id_yandex) == 201, \
    f'Результат: {create_yandex_folder(id_yandex)} {itog[create_yandex_folder(id_yandex)]}'
    # Папка уже существует
    assert create_yandex_folder(id_yandex) == 409
    # Ошибка доступа
    assert create_yandex_folder('y0__37585juj7890f3gg906jrj78i23ujk5948610i85o18j41') == 401