import allure
import pytest
from requests.exceptions import JSONDecodeError


from http import HTTPStatus

from sources.client.data import TestData
from sources.client.courier_support import (get_data_for_check_response_error as response_error,
                                            get_data_without_one_required_field as without_one_required_field,
                                            register_new_courier_and_return_login_password as courier_data_is_exist,
                                            get_response_get_courier as get_courier)


@pytest.mark.get_url('login_courier')
class TestLoginCourier:

    @allure.title('Курьер может авторизоваться/Для авторизации нужно передать все обязательные поля/Успешный запрос возвращает id') # покрывает 3 проверки в задании : Курьер может авторизоваться, Для авторизации нужно передать все обязательные поля, Успешный запрос возвращает id
    def test_login_courier_available_is_success(self, get_url, get_new_data):
        payload = courier_data_is_exist(get_new_data)
        response = get_courier(get_url, payload)
        assert response.status_code == HTTPStatus.OK
        assert 'id' in response.json()

    @allure.title(';')
    def test_login_courier_with_required_fields_available_is_success(self, get_url, get_new_data):
        payload = courier_data_is_exist(get_new_data)
        response = get_courier(get_url, payload)
        assert response.status_code == HTTPStatus.OK
        assert 'id' in response.json()

    @allure.title('Ошибка авторизации при неправильном login или password')
    @pytest.mark.parametrize('condition', ('incorrect_login', 'incorrect_password'))
    def test_login_courier_with_incorrect_login_password_return_error_success(
            self, get_url, condition, get_new_data):
        current_data = courier_data_is_exist(get_new_data)
        payload = response_error(condition, current_data)
        response = get_courier(get_url, payload)
        assert response.json()['message'] == TestData.ERROR_TEXT_FOR_INCORRECT_LOGIN_OR_PASSWORD

    @allure.title('Проверка ошибки авторизации курьера при отсутствии в запросе обязательного поля login')
    def test_login_courier_without_one_field_return_error_login_success(self, get_url, get_new_data):
        current_data = courier_data_is_exist(get_new_data)
        payload = current_data.copy()  
        del payload['login']  
        response = get_courier(get_url, payload)
        assert response.status_code == HTTPStatus.BAD_REQUEST
        expected_error_message = TestData.ERROR_TEXT_LOGIN_WITHOUT_PASSWORD
        assert response.json()['message'] == expected_error_message
    
    @allure.title('Проверка ошибки авторизации курьера при отсутствии в запросе обязательного поля password')
    def test_login_courier_without_one_field_return_error_success(self, get_url, get_new_data):
        current_data = courier_data_is_exist(get_new_data)
        payload = dict.fromkeys(['password', ])
        payload = without_one_required_field(payload, current_data)
        response = get_courier(get_url, payload)
        message = response.json()['message']
        assert response.status_code == HTTPStatus.BAD_REQUEST
        assert message == TestData.ERROR_TEXT_LOGIN_WITHOUT_PASSWORD

    @allure.title('Ошибка авторизация несуществующим пользователем')
    def test_login_courier_with_required_fields_available_success(self, get_url, get_new_data):
        payload = courier_data_is_exist(get_new_data)
        password = get_new_data['login']
        payload['login'] = f"new{get_new_data['login']}"
        response = get_courier(get_url, payload)
        payload['login'] = password
        message = response.json()['message']
        assert response.status_code == HTTPStatus.NOT_FOUND
        assert message == TestData.ERROR_TEXT_FOR_INCORRECT_LOGIN_OR_PASSWORD

