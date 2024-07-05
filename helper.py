from faker import Faker

fake = Faker()


class CreateCurrierData:
    @staticmethod
    def generate_currier_data():
        CREATE_COURIER_BODY = {
            "email": fake.email(),
            "password": fake.password(),
            "name": fake.first_name()
        }
        return CREATE_COURIER_BODY

    @staticmethod
    def generate_fake_user_data():
        CREATE_COURIER_BODY = {
            "email": fake.email(),
            "password": fake.password(),
            "name": fake.first_name()
        }
        return CREATE_COURIER_BODY

    @staticmethod
    def generate_fake_email():
        FAKE_EMAIL = {"email": fake.email()}
        return FAKE_EMAIL
