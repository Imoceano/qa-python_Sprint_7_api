from sources.client.data import TestData


class APICourier:

    ENDPOINT_COURIER_CREATE = '/api/v1/courier'
    ENDPOINT_COURIER_LOGIN = '/api/v1/courier/login'

    def post_api_courier_route(self):
        url = f'{TestData.MAIN_URL}{self.ENDPOINT_COURIER_CREATE}'
        return url

    def get_api_courier_route(self):
        url = f'{TestData.MAIN_URL}{self.ENDPOINT_COURIER_LOGIN}'
        return url


class APIOrder:

    ENDPOINT_ORDERS_CREATE_GET_LIST = '/api/v1/orders'
    ENDPOINT_ORDER_CANCEL = '/api/v1/orders/cancel'

    def get_post_api_order_route(self):
        url = f'{TestData.MAIN_URL}{self.ENDPOINT_ORDERS_CREATE_GET_LIST}'
        return url
