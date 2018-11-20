from flask import render_template,request,redirect,url_for,abort,flash
from . import main
from .forms import PitchForm,CommentForm,UpdateProfile
from ..models import User,Pitch,Comment
from .. import db,photos
import markdown2
from flask_login import login_required, current_user




# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    pitches = Pitch.query.all()
    title = "Pitch-Perfect \\ Home"
    return render_template('index.html', title = title, pitches = pitches)



@main.route('/pitches/<category>')
def pitches_category(category):

    '''
    View function that returns pitches by category
    '''
    title = f'Pitch-Perfect \\ {category.upper}'
    if category = "all":
        pitches = Pitch.query.order_by(Pitch.time.desc())
    else:
        pitches = Pitch.query.filter_by(category=category).order_by(Pitch.time.desc()).all()

    return render_template('pitches.html',title = title,pitches = pitches)



@main.route('/<uname>/new/pitch', methods=['GET','POST'])
@login_required
def new_pitch():
    form = PitchForm()

    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    title_page = "Pitch-Perfect \\ Add New Pitch"

    if form.validate_on_submit():

        title=form.title.data
        content=form.content.data
        category=form.category.data
        date = datetime.datetime.now()
        time = str(date.time())
        time = time[0:5]
        date = str(date)
        date = date[0:10]
        pitch = Pitch(title=title,
                      content=content,
                      category=category,
                      user=current_user,
                      date = date,
                      time = time)

        db.session.add(pitch)
        db.session.commit()

        # pitch.save_pitch(pitch)
        flash('Your pitch has been created!', 'success')
        return redirect(url_for('main.pitch_categories',category = category))

    return render_template('new_pitch.html', title=title_page, form=form)






################################################################################

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)



@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)




@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))
