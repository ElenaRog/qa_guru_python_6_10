from dataclasses import dataclass
from enum import Enum
from datetime import datetime

from selene import browser, have

from classes.registration_page import RegistrationPage


class Gender(Enum):
    male = 'Male'
    female = 'Female'
    other = 'Other'


class Birthday:
    def __init__(self, value):
        self.day = datetime.strptime(value, '%d %B,%Y').day
        self.month = datetime.strptime(value, '%d %B,%Y').strftime('%B')
        self.year = datetime.strptime(value, '%d %B,%Y').year
        self.bday = value


class Hobbies(Enum):
    sports = 'Sports'
    reading = 'Reading'
    music = 'Music'

@dataclass
class Student:
    first_name: str
    last_name: str
    email: str
    gender: Gender
    number: str
    date_of_birth: Birthday
    subject: str
    hobbies: Hobbies
    picture: str
    address: str
    state: str
    city: str

    @staticmethod
    def open():
        browser.open('/automation-practice-form')
        # browser.all('[id^=google_ads][id$=container__]').with_(timeout=10).wait_until(
        #     have.size_greater_than_or_equal(3)
        # )
        # browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)

    def register(self):
        registration_page = RegistrationPage()
        registration_page.fill_name(self.first_name)
        registration_page.fill_last_name(self.last_name)
        registration_page.fill_email(self.email)
        registration_page.fill_gender(self.gender.value)
        registration_page.fill_number(self.number)
        registration_page.fill_date_of_birth(self.date_of_birth.year, self.date_of_birth.month, self.date_of_birth.day)
        registration_page.fill_subject(self.subject)
        registration_page.fill_hobbies(self.hobbies.value)
        registration_page.download_picture(self.picture)
        registration_page.fill_address(self.address)
        registration_page.fill_state(self.state)
        registration_page.fill_city(self.city)
        registration_page.submit()

    def should_have_registered(self):
        browser.element('.table').all('td').even.should(
            have.exact_texts(
                f'{self.first_name} {self.last_name}',
                self.email,
                self.gender.female.value,
                self.number,
                self.date_of_birth.bday,
                self.subject,
                self.hobbies.sports.value,
                self.picture,
                self.address,
                f'{self.state} {self.city}'
            )
        )
