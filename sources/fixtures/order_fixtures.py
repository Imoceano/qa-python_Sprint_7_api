import pytest

from sources.client.order_support import cancel_order


@pytest.fixture
def cancel_order():
    payload = {}
    yield payload
    cancel_order(payload)
