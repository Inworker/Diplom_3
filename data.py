from faker import Faker

class Urls:
    HOME_PAGE = "https://stellarburgers.nomoreparties.site"
    LOGIN_END_POINT = "/login"
    FORGOT_PASSWORD_END_POINT ="/forgot-password"
    RESET_PASSWORD_END_POINT = "/reset-password"

class FakeData:
    fake = Faker()
    fake_email = fake.email()