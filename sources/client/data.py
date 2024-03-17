class TestData:
    MAIN_URL = 'https://qa-scooter.praktikum-services.ru'

    
    ERROR_TEXT_FOR_CREATE_WITHOUT_REQUIRED_FIELD = 'Недостаточно данных для создания учетной записи'
    ERROR_TEXT_FOR_LOGIN_EXIST_YET = 'Этот логин уже используется. Попробуйте другой.'
    ERROR_TEXT_FOR_INCORRECT_LOGIN_OR_PASSWORD = 'Учетная запись не найдена'
    ERROR_TEXT_LOGIN_WITHOUT_PASSWORD = 'Недостаточно данных для входа'
    RESPONSE_SUCCESS = {'ok': True}


    FIRSTNAME_CLIENT= 'Иван'
    LASTNAME_CLIENT = 'НеИван'
    ADDRESS_CLIENT = 'Бикини Боттом, Дом Ананас'
    METRO_STATION = 5
    PHONE_CLIENT = '89999990000'
    TIME_OF_RENT = 4
    DELIVERY_TIME = '2024-03-04'
    COMMENT = 'Домофона нет. Позвоните плз'

    SCOOTER_COLOR_BLACK = ['BLACK']
    SCOOTER_COLOR_GRAY = ['GRAY']
    SCOOTER_COLOR_BLACK_AND_GRAY = ['BLACK', 'GRAY']
    SCOOTER_WITTHOUT_COLOR = []

    client_data = [
        FIRSTNAME_CLIENT,
        LASTNAME_CLIENT,
        ADDRESS_CLIENT,
        METRO_STATION,
        PHONE_CLIENT,
        TIME_OF_RENT,
        DELIVERY_TIME,
        COMMENT
    ]

    data_color = [
        SCOOTER_COLOR_BLACK,
        SCOOTER_COLOR_GRAY,
        SCOOTER_COLOR_BLACK_AND_GRAY,
        SCOOTER_WITTHOUT_COLOR
    ]
