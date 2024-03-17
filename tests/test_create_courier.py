import allure
import pytest

from http import HTTPStatus

from sources.client.data import TestData
from sources.client.courier_support import register_new_courier_and_return_login_password as exist_courier_data
from sources.client.courier_support import get_data_without_one_required_field
from sources.client.courier_support import get_response_post_courier as post_courier
                                            
                                            
                                            


@pytest.mark.get_url('create_courier')
class TestCreateCourier:

    @allure.title('курьера можно создать/ Тест успешного создания курьера при передаче всех обязательных полей') #покрывает 4 проверки задания: Создание курьера, создание курьера при передаче всех обязательных полей, проверка успешного запроса, возврат {'ok': 'true'}
    def test_create_courier_available_success(self, get_url, get_new_data):
        payload = get_new_data
        response = post_courier(get_url, payload)
        assert response.status_code == HTTPStatus.CREATED
        assert response.json() == TestData.RESPONSE_SUCCESS

    @allure.title('Тест невозможности создать 2 одинаковых курьера/ если создать пользователя с логином, который уже есть, возвращается ошибка.') #покрывает 2 проверки задания: Невозоможно создать 2 одинаковых курьера, возврат ошибки при создании если логин существует
    def test_create_courier_as_prev_courier_unavailable_success(self, get_url, get_new_data):
        payload = exist_courier_data(get_new_data)
        response = post_courier(get_url, payload)
        message = response.json()['message']
        assert response.status_code == HTTPStatus.CONFLICT
        assert message == TestData.ERROR_TEXT_FOR_LOGIN_EXIST_YET


    @allure.title('Проверка ответа при отсутствии в запросе обязательного поля')
    @pytest.mark.parametrize('field', ['login', 'password'])
    def test_create_courier_without_one_required_field_unavailable_success(self, get_url, field, get_new_data):
        payload = dict.fromkeys([field,])
        payload = get_data_without_one_required_field(payload, get_new_data)
        response = post_courier(get_url, payload)
        message = response.json()['message']
        assert response.status_code == HTTPStatus.BAD_REQUEST
        assert message == TestData.ERROR_TEXT_FOR_CREATE_WITHOUT_REQUIRED_FIELD

  