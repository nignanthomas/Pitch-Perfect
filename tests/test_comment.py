import unittest
from app.models import Comment,User
from flask_login import current_user
from app import db

class TestComment(unittest.TestCase):

    def setUp(self):
        self.new_user = User(username = 'Thomas', password = 'totopitch', email = 'nstcephas@gmail.com')
        self.new_comment = Comment(id=1, post_comment="this is a nice pitch post", category_id='funny', pitches="what a nice pitch", user_id = self.new_user)

    def tearDown(self):
        Comment.query.delete()
        User.query.delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_comment,Comment))


    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.id,1)
        self.assertEquals(self.new_comment.post_comment,"this is a nice pitch post")
        self.assertEquals(self.new_comment.category_id,'funny')
        self.assertEquals(self.new_comment.pitch, 'what a nice pitch')
        self.assertEquals(self.new_comment.user,self.new_user)


    def test_save_comment(self):
        self.new_comment.save_comment()
        self.assertTrue(len(Comment.query.all())>0)


    def test_get_comment_by_id(self):

        self.new_comment.save_comment()
        got_comments = Comment.get_comments(12345)
        self.assertTrue(len(got_comments) == 1)
