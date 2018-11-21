import unittest
from app.models import Pitch,User
from flask_login import current_user
from app import db

class TestPitch(unittest.TestCase):

    def setUp(self):
        self.user_user = User(username = 'Thomas',
                                 password = 'totopitch',
                                 email = 'nstcephas@gmail.com')
        self.new_pitch = Pitch(id=1,
                                     title='Pitch itself',
                                     content="this is a nice pitch post",
                                     category_id='funny',
                                     comments="what a nice comment",
                                     user_id = self.user_user)

    def tearDown(self):
        Pitch.query.delete()
        User.query.delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_pitch,Pitch))


    def test_check_instance_variables(self):
        self.assertEquals(self.new_pitch.id,1)
        self.assertEquals(self.new_pitch.title,'Pitch itself')
        self.assertEquals(self.new_pitch.content,"this is a nice pitch post")
        self.assertEquals(self.new_pitch.category,'funny')
        self.assertEquals(self.new_pitch.comments, 'what a nice comment')
        self.assertEquals(self.new_pitch.user,self.user_user)


    def test_save_pitch(self):
        self.new_pitch.save_pitch()
        self.assertTrue(len(Pitch.query.all())>0)


    def test_get_pitch_by_id(self):

        self.new_pitch.save_pitch()
        got_pitches = Pitch.get_pitch(1)
        self.assertTrue(len(got_pitches) == 1)
