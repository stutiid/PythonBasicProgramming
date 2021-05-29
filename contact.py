import logging
import re
from contact_custom_exception import ContactException

logging.basicConfig(filename='contact_exception.log', encoding='utf-8', level=logging.INFO)
"""
Class represents a person contact with details like name with first name and last name, address details of person like
area address, its city, its state and zipcode of that city and other contact details like mobile number and email
address. Getters and setters are used to validate the fields
"""


class Contact:

    def __init__(self, contact_details):
        self.first_name = contact_details[0]
        self.last_name = contact_details[1]
        self.address = contact_details[2]
        self.city = contact_details[3]
        self.state = contact_details[4]
        self.zipcode = contact_details[5]
        self.mobile = contact_details[6]
        self.email = contact_details[7]

    @property
    def first_name(self):
        return self.first_name

    @first_name.setter
    def first_name(self, value):
        if value is None:
            raise ContactException(ContactException.exception_type[0], "please give some input")
        if len(value) == 0:
            raise ContactException(ContactException.exception_type[1], "entered empty first name")
        if re.fullmatch('^[A-Z][a-z]{2,20}$', value):
            self._first_name = value
        else:
            raise ContactException(ContactException.exception_type[2], "entered invalid first name")

    @property
    def last_name(self):
        return self.last_name

    @last_name.setter
    def last_name(self, value):
        if value is None:
            raise ContactException(ContactException.exception_type[0], "please give some input")
        if len(value) == 0:
            raise ContactException(ContactException.exception_type[1], "entered empty last name")
        if re.fullmatch('^[A-Z][a-z]{2,}$', value):
            self._last_name = value
        else:
            raise ContactException(ContactException.exception_type[2], "entered invalid last name")

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        if value is None:
            raise ContactException(ContactException.exception_type[0], "please give some input")
        if len(value) == 0:
            raise ContactException(ContactException.exception_type[1], "entered empty address")
        else:
            self._address = value

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        if value is None:
            raise ContactException(ContactException.exception_type[0], "please give some input")
        if len(value) == 0:
            raise ContactException(ContactException.exception_type[1], "entered empty city name")
        if re.fullmatch('^[A-Z][a-z]{2,}$', value):
            self._city = value
        else:
            raise ContactException(ContactException.exception_type[2], "entered invalid city name")

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        if value is None:
            raise ContactException(ContactException.exception_type[0], "please give some input")
        if len(value) == 0:
            raise ContactException(ContactException.exception_type[1], "entered empty state name")
        if re.fullmatch('^[A-Z][a-z]{2,}$', value):
            self._state = value
        else:
            raise ContactException(ContactException.exception_type[2], "entered invalid state name")

    @property
    def zipcode(self):
        return self._zipcode

    @zipcode.setter
    def zipcode(self, value):
        if value is None:
            raise ContactException(ContactException.exception_type[0], "please give some input")
        if re.fullmatch('^[1-9][0-9]{5}$|^[1-9][0-9]{2} [0-9]{3}$', str(value)):
            self._zipcode = value
        else:
            raise ContactException(ContactException.exception_type[2], "entered invalid zipcode")

    @property
    def mobile(self):
        return self._mobile

    @mobile.setter
    def mobile(self, value):
        if value is None:
            raise ContactException(ContactException.exception_type[0], "please give some input")
        if re.fullmatch('^[1-9][0-9]{9}$|^[0-9]{2}[1-9][0-9]{9}$|^\\+[0-9]{2}[1-9][0-9]{9}$', str(value)):
            self._mobile = value
        else:
            raise ContactException(ContactException.exception_type[2], "entered invalid mobile")

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if value is None:
            raise ContactException(ContactException.exception_type[0], "please give some input")
        if len(value) == 0:
            raise ContactException(ContactException.exception_type[1], "entered empty email address")
        if re.fullmatch('^(\\w|.|_|-)+[@](\\w|_|-|.)+[.]\\w{2,3}$', value):
            self._email = value
        else:
            raise ContactException(ContactException.exception_type[2], "entered invalid email address")

    def __str__(self):
        return f"contact( name=>{self._first_name} {self._last_name}, address=>{self._address}, city=>{self._city}" \
               + f",state=>{self._state}, zipcode=>{self._zipcode}, mobile=>{self._mobile}, email=>{self._email})"


if __name__ == '__main__':
    try:
        contact_details_list = ['Landon', 'Kirby', '7 Fox Hill', 'Margao', 'Goa', 403602, 9878654534, 'kirby@gmail.com']
        contacts = Contact(contact_details_list)
        logging.info(contacts.__str__())
    except ContactException as ex:
        logging.exception(ex.__str__())
