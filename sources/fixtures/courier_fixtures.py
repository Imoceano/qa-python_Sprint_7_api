import pytest

from sources.client.courier_support import get_data_for_create_courier

@pytest.fixture
def get_new_data():
    payload = get_data_for_create_courier()
    yield payload
    get_data_for_create_courier()
