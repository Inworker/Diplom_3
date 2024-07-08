from faker import Faker


class Urls:
    HOME_PAGE = "https://stellarburgers.nomoreparties.site"
    LOGIN_END_POINT = "/login"
    FORGOT_PASSWORD_END_POINT = "/forgot-password"
    RESET_PASSWORD_END_POINT = "/reset-password"
    ACCOUNT_END_POINT = "/account"
    ACCOUNT_PROFILE_END_POINT = "/account/profile"
    LIST_OF_ORDERS_END_POINT = "/feed"
    GET_DATA_INGREDIENT_URL = "/api/ingredients"
    CREATE_ORDER_URL = "/api/orders"
    RESET_PASSWORD_URL = "/api/password-reset"
    RECOVERY_PASSWORD_URL = RESET_PASSWORD_URL + "/reset-password"
    AUTH_REGISTER_USER_URL = "/api/auth/register"
    AUTH_LOGIN_URL = "/api/auth/login"
    AUTH_USER_URL = "/api/auth/user"
    AUTH_LOGOUT_USER_URL = "/api/auth/logout"
    AUTH_TOKEN_URL = "/api/auth/token"
    HISTORY_ACCOUNT_PAGE = "https://stellarburgers.nomoreparties.site/account/order-history"


class FakeData:
    fake = Faker()
    fake_email = fake.email()


class TimeWaitElement:
    TIME_OUT = 10
