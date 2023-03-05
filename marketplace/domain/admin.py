import uuid

import email_validator
import phonenumbers
from attr import field, Factory, frozen


def generate_id() -> str: return uuid.uuid4().hex


def validate_email(instance, attribute, value): return email_validator.validate_email(value)


def validate_phone_number(instance, attribute, value): return phonenumbers.parse(value)


# TODO integrate password
@frozen
class Admin:
    first_name: str
    last_name: str
    email: str = field(validator=validate_email)
    phone_number: str = field(validator=validate_phone_number)
    id: str = Factory(generate_id)


if __name__ == "__main__":
    admin = Admin(first_name="Momo", last_name="Lo", email="momo@lo.com", phone_number="+221775357510")

    print(admin)
