import unittest
import shutil
from models import db
from routes import *

basedir = os.path.abspath(os.path.dirname(__file__))
db_uri = 'sqlite:///' + os.path.join(basedir, 'test_db.sqlite')


class TestRoutes(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        self.app = app.test_client()

        db.drop_all()
        db.create_all()

    def tearDown(self):
        pass

    def test_register(self):
        with app.app_context():
            with app.test_client() as client:
                sent = {"user_name": "matt", "email": "matt@iu.edu", "password": "password"}
                response = client.post('/users', json=sent)
                assert response.status_code == 200
                response = client.post('/users', json=sent)
                assert response.status_code == 401

    def test_sign_in(self):
        with app.app_context():
            with app.test_client() as client:
                sent = {"user_name": "jon", "email": "matt@iu.edu", "password": "password"}
                client.post('/users', json=sent)
                response = client.post('/users/session', json=sent)
                assert response.status_code == 200
                sent = {"user_name": "matt", "email": "matt@iu.edu", "password": "password"}
                response = client.post('/users/session', json=sent)
                assert response.status_code == 401

    def test_play(self):
        with app.app_context():
            with app.test_client() as client:
                new_song = Song(os.path.join(basedir, "test_library/0b02d34c3dc14a099e26b360f733f3a8.wav"), steps="128")
                db.session.add(new_song)
                db.session.commit()
                response = client.get('/play/1')
                assert response.status_code == 200

    def test_single_song(self):
        with app.app_context():
            with app.test_client() as client:
                new_song = Song(os.path.join(basedir, "test_library/0b02d34c3dc14a099e26b360f733f3a8.wav"), steps="128")
                db.session.add(new_song)
                db.session.commit()
                response = client.get('/song/1')
                assert response.status_code == 200

    def test_all_song(self):
        with app.app_context():
            with app.test_client() as client:
                new_song2 = Song(os.path.join(basedir, "test_library/0b02d34c3dc14a099e26b360f733f3a8.wav"),
                                 steps="128")
                new_song3 = Song(os.path.join(basedir, "test_library/0b6241f5a82e406d8b9e4a464ca3b312.wav"),
                                 steps="128")
                db.session.add(new_song2)
                db.session.add(new_song3)
                db.session.commit()
                response = client.get('/song')
                assert response.status_code == 200

    def test_delete_song(self):
        with app.app_context():
            with app.test_client() as client:
                new_song = Song(os.path.join(basedir, "test_library/0b02d34c3dc14a099e26b360f733f3a8.wav"), steps="128")
                db.session.add(new_song)
                db.session.commit()
                source = os.path.join(basedir, "test_library/0b02d34c3dc14a099e26b360f733f3a8.wav")
                destination = os.path.join(basedir, "test_library/0b02d34c3dc14a099e26b360f733f3a8(1).wav")
                shutil.copy(source, destination)
                response = client.delete('/song/1')
                os.rename(destination, source)
                assert response.status_code == 200


def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestRoutes('test_register'))
    suite.addTest(TestRoutes('test_sign_in'))
    suite.addTest(TestRoutes('test_play'))
    suite.addTest(TestRoutes('test_single_song'))
    suite.addTest(TestRoutes('test_all_song'))
    suite.addTest(TestRoutes('test_delete_song'))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())
