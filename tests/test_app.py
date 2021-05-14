import unittest
from flask.wrappers import Response
from flask import url_for
from flask_testing import TestCase
from application.models import ClimbingCentre, ClimberInformation
from application import app, db

class TestBase(TestCase):
    def create_app(self):
        app.config.update(
                SQLALCHEMY_DATABASE_URI="sqlite:///data.db",
                SECRET_KEY="TEST_SECRET_KEY",
                DEBUG=True, 
                WTF_CSRF_ENABLED=False
            )
        return app

    def setUp(self):
        db.create_all()
        db.session.add(ClimbingCentre(centre_name="name", address="address"))
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestViews(TestBase):
    def test_home_get(self):
        response = self.client.get(url_for("home"))
        self.assertEqual(response.status_code, 200)

    def test_create_get(self):
        response = self.client.get(url_for("create"))
        self.assertEqual(response.status_code, 200)

    def test_update_get(self):
        response = self.client.get(url_for("update", id=1))
        self.assertEqual(response.status_code, 200)

    def test_signup_get(self):
        response = self.client.get(url_for("signup", id=1))
        self.assertEqual(response.status_code, 200)


    def test_delete_get(self):
        response = self.client.get(url_for("delete", id=1), follow_redirects=True)
        self.assertEqual(response.status_code, 200)

class TestRead(TestBase):
    def test_read(self):
        response = self.client.get(url_for("home"))
        self.assertIn(b"name", response.data)
            

class TestCreate(TestBase):
    def test_create_post(self):
        response = self.client.post(
            url_for("create"),
            data=dict(centre_name="name", address="address"),
            follow_redirects=True
        )
        self.assertIn(b"name", response.data)
        self.assertIn(b"address", response.data)

class TestSignup(TestBase):
    def test_signup_post(self):
        response = self.client.post(
            url_for("signup"),
            data=dict(centre_name="name", address="address"),
            follow_redirects=True
        )
        self.assertIn(b"name", response.data)
        self.assertIn(b"address", response.data)
    

class TestUpdate(TestBase):
    def test_update_post(self):
        response = self.client.post(
            url_for("update", id=1), 
            data=dict(centre_name=" ", address=" "),
            follow_redirects=True
        )
        self.assertIn(b' ', response.data)
        self.assertIn(b" ", response.data)


class TestDelete(TestBase):
    def test_delete_delete(self):
        response = self.client.delete(
            url_for("delete", id=1),
            follow_redirects=True
        )
        self.assertNotIn(b'name', response.data)