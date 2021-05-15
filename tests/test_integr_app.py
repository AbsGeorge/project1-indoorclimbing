from flask_testing import LiveServerTestCase
from selenium import webdriver

from urllib.request import urlopen
from flask import url_for

from application.models import ClimbingCentre
from application import app, db


class TestBase(LiveServerTestCase):
    TEST_PORT = 5050 # test port, doesn't need to be open

    def create_app(self):

        app.config.update(
            SQLALCHEMY_DATABASE_URI="sqlite:///test.db",
            LIVESERVER_PORT=self.TEST_PORT,
            
            DEBUG=True,
            TESTING=True
        )

        return app

    def setUp(self):

        chrome_options = webdriver.chrome.options.Options()
        chrome_options.add_argument('--headless')

        self.driver = webdriver.Chrome(options=chrome_options)

        db.create_all() 

        self.driver.get(f'http://localhost:{self.TEST_PORT}')

    def tearDown(self):
        self.driver.quit()

        db.drop_all()

    def test_server_is_up_and_running(self):
        response = urlopen(f'http://localhost:{self.TEST_PORT}')
        self.assertEqual(response.code, 200)

class TestAdd(TestBase):
    TEST_CASES = 'testing'

    def submit_input(self, case): # custom method
        self.driver.find_element_by_xpath('/html/body/a[2]')
        self.driver.find_element_by_xpath('//*[@id="name"]').send_keys(case)
        self.driver.find_element_by_xpath('//*[@id="address"]').send_keys(case)
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()

    def test_create(self):
        self.driver.get(f'http://localhost:5000/create') # go to /create route

        input_box = self.driver.find_element_by_xpath('//*[@id="name"]')
        input_box.send_keys('centre')
        input_box = self.driver.find_element_by_xpath('//*[@id="address"]')
        input_box.send_keys('address')

        self.driver.find_element_by_xpath('//*[@id="submit"]').click() # submit field

        assert self.driver.current_url == 'http://localhost:5000/home'

