from selene import have

from pages.student_registration import RegistrationPage


def test_student_registration_form():
    registration_page = RegistrationPage()
    registration_page.open()

    registration_page.fill_name('Elena')
    registration_page.fill_last_name('Rogozina')
    registration_page.fill_email('elenarog@mail.ru')
    registration_page.fill_gender('Female')
    registration_page.fill_number('5554678578')
    registration_page.fill_date_of_birth('1997', 'June', '27')
    registration_page.fill_subject('Biology')
    registration_page.fill_hobbies('Sports')
    registration_page.download_picture('image.png')
    registration_page.fill_address('Baker st. 221B')
    registration_page.fill_state('Uttar Pradesh')
    registration_page.fill_city('Agra')
    registration_page.submit()

    registration_page.registered_user_data().should(
        have.exact_texts(
            'Elena Rogozina',
            'elenarog@mail.ru',
            'Female',
            '5554678578',
            '27 June,1997',
            'Biology',
            'Sports',
            'image.png',
            'Baker st. 221B',
            'Uttar Pradesh Agra'
        )
    )


