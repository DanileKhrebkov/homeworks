import requests

def get_geolocation_info():
    try:
        # Отправляем GET-запрос к API
        response = requests.get('https://ipinfo.io/161.185.160.93/geo')
        
        # Проверяем статус ответа
        response.raise_for_status()
        
        # Получаем данные в формате JSON
        data = response.json()
        
        # Выводим информацию
        print("Информация о геолокации:")
        print(f"Страна: {data.get('country', 'недоступно')}")
        print(f"Город: {data.get('city', 'недоступно')}")
        print(f"Местоположение: {data.get('loc', 'недоступно')}")
        print(f"Организация: {data.get('org', 'недоступно')}")
        
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при соединении с API: {e}")
    except ValueError:
        print("Ошибка при обработке JSON-ответа")
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")

# Вызываем функцию
get_geolocation_info()