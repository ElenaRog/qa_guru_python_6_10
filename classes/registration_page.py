import os
from selene.support.shared import browser
from selene import have, be

from tests.conftest import RES_DIR


class RegistrationPage:

    @staticmethod
    def open():
        browser.open('/automation-practice-form')
        # browser.all('[id^=google_ads][id$=container__]').with_(timeout=10).wait_until(
        #     have.size_greater_than_or_equal(3)
        # )
        # browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)

    def fill_name(self, value):
        browser.element('#firstName').type(value)

    def fill_last_name(self, value):
        browser.element('#lastName').type(value)

    def fill_email(self, value):
        browser.element('#userEmail').type(value)

    def fill_gender(self, value):
        browser.all('[name=gender]').element_by(have.value(value)).element('..').click()

    def fill_number(self, value):
        browser.element('#userNumber').type(value)

    def fill_date_of_birth(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').send_keys(month)
        browser.element('.react-datepicker__year-select').send_keys(year)
        browser.element(f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)').click()

    def fill_subject(self, value):
        browser.element('#subjectsInput').type(value).press_enter()

    def fill_hobbies(self, value):
        browser.all('.custom-checkbox').element_by(have.exact_text(value)).click()

    def download_picture(self, file):
        browser.element('#uploadPicture').locate().send_keys(
            os.path.join(RES_DIR, file)
        )

    def fill_address(self, value):
        browser.element('#currentAddress').type(value)

    def fill_state(self, value):
        browser.element('#state').click()
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(value)
        ).click()

    def fill_city(self, value):
        browser.element('#city').click()
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(value)
        ).click()

    @staticmethod
    def submit():
        browser.element('#submit').should(be.visible).click()

    def registered_user_data(self):
        return browser.element('.table').all('td').even

