Данный проект тестирует приложение https://qa-scooter.praktikum-services.ru/


Тесты содержаться в директории Tests
Общее количество тестов 24



Дирректория allure_results - содержит отчеты о тестировании 

В тестах используются методы:
 @pytest.fixture
 @pytest.mark.parametirze 


Информация о запуске:

Запуск всех тестов. pytest -v tests

Запус с подробной оценкой покрытия pytest --cov=main --cov-report=html
(смотреть файл main_py.html после запуска)

Запуск тестов с формированием отчета Allure - pytest tests  --alluredir=allure_results 
Запуск тестов с формирование отчета Allure в формате веб страницы - allure serve allure_results




Данные тесты проверяют эгдпоинты перечисленные ниже:



 1. Создание курьера

 `test_create_courier.py` - 

 Эндпоинт: POST /api/v1/courier




 2. Логин курьера

 `test_login_courier.py` - 

 Эндпоинт: GET /api/v1/courier/login



3. Создание заказа

`test_create_order.py` - 


POST /api/v1/orders


4. Список заказов

`test_get_list_orders.py` - 

GET /api/v1/orders

