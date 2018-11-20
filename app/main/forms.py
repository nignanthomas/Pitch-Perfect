from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class PitchForm(FlaskForm):

    title = StringField('Pitch title')
    category = SelectField('Pitch Category', choices=[('pickup-lines', 'pickup-lines'),
                                                      ('motivational', 'motivational'),
                                                      ('promotion', 'promotion'),
                                                      ('funny', 'funny'),
                                                      ('random', 'random')])
    content = TextAreaField('Type Here',validators=[Required()])
    submit = SubmitField('Create Pitch')


class CommentForm(FlaskForm):

    title = StringField('Comment Title')
    comment = TextAreaField('Post Of The Comment')
    submit = SubmitField('Submit')

#########################################


########################################

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')
