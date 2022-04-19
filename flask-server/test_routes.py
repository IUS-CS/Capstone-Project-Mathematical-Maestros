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
                new_song = Song(midi_path=os.path.join(basedir, "test_library/1650378574.972328.mid"),\
                    wav_path=os.path.join(basedir, "test_library/1650378574.972328.wav"),\
                    genre="Rock",
                    rating=0.0)
                db.session.add(new_song)
                db.session.commit()
                response = client.get('/play/1')
                assert response.status_code == 200

    def test_single_song(self):
        with app.app_context():
            with app.test_client() as client:
                new_song = Song(midi_path=os.path.join(basedir, "test_library/1650378574.972328.mid"),\
                    wav_path=os.path.join(basedir, "test_library/1650378574.972328.wav"),\
                    genre="Rock",
                    rating=0.0)                
                db.session.add(new_song)
                db.session.commit()
                response = client.get('/song/1')
                assert response.status_code == 200

    def test_all_song(self):
        with app.app_context():
            with app.test_client() as client:
                new_song = Song(midi_path=os.path.join(basedir, "test_library/1650378574.972328.mid"),\
                    wav_path=os.path.join(basedir, "test_library/1650378574.972328.wav"),\
                    genre="Rock",
                    rating=0.0) 
                new_song2 = Song(midi_path=os.path.join(basedir, "test_library/1650379410.3046038.mid"),\
                    wav_path=os.path.join(basedir, "test_library/1650379410.3046038.wav"),\
                    genre="Rock",
                    rating=0.0) 
                db.session.add(new_song)
                db.session.add(new_song2)
                db.session.commit()
                response = client.get('/song')
                assert response.status_code == 200

    def test_delete_song(self):
        with app.app_context():
            with app.test_client() as client:
                new_song = Song(midi_path=os.path.join(basedir, "test_library/1650378574.972328.mid"),\
                    wav_path=os.path.join(basedir, "test_library/1650378574.972328.wav"),\
                    genre="Rock",
                    rating=0.0) 
                db.session.add(new_song)
                db.session.commit()
                wav_source = os.path.join(basedir, "test_library/1650378574.972328.wav")
                wav_destination = os.path.join(basedir, "test_library/1650378574.972328(1).wav")
                shutil.copy(wav_source, wav_destination)
                midi_source = os.path.join(basedir, "test_library/1650378574.972328.mid")
                midi_destination = os.path.join(basedir, "test_library/1650378574.972328(1).mid")
                shutil.copy(midi_source, midi_destination)
                response = client.delete('/song/1')
                os.rename(wav_destination, wav_source)
                os.rename(midi_destination, midi_source)
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
