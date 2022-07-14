from flask_wtf import FlaskForm
from wtforms import (StringField, TextAreaField, IntegerField, BooleanField,
                     RadioField, EmailField, IntegerRangeField)
from wtforms.validators import InputRequired, Length


class PersonalityForm(FlaskForm):
    name = StringField('Name *', validators=[InputRequired(),
                                             Length(min=10, max=100)])
    email = EmailField('EMail *', validators=[InputRequired()])

    friends = IntegerRangeField('You regularly make new friends.')
    random_topics = IntegerRangeField('You spend a lot of your free time exploring various random topics that pique your interest.')
    cry = IntegerRangeField('Seeing other people cry can easily make you feel like you want to cry too.')
    backup_plan = IntegerRangeField('You often make a backup plan for a backup plan.')
    stay_calm = IntegerRangeField('You usually stay calm, even under a lot of pressure.')
    social_events = IntegerRangeField('At social events, you rarely try to introduce yourself to new people and mostly talk to the ones you already know.')
    start_projects = IntegerRangeField('You prefer to completely finish one project before starting another.')
    sentimental = IntegerRangeField('You are very sentimental')
    organization = IntegerRangeField('You like to use organizing tools like schedules and lists.')
    self_steem = IntegerRangeField('Even a small mistake can cause you to doubt your overall abilities and knowledge.')
    conversation = IntegerRangeField('You feel comfortable just walking up to someone you find interesting and striking up a conversation.')
    creative = IntegerRangeField('You are not too interested in discussing various interpretations and analyses of creative works.')
    head_heart = IntegerRangeField('You are more inclined to follow your head than your heart.')
    planning = IntegerRangeField('You usually prefer just doing what you feel like at any given moment instead of planning a particular daily routine.')
    impression = IntegerRangeField('You rarely worry about whether you make a good impression on people you meet.')
    group_activities = IntegerRangeField('You enjoy participating in group activities.')
    interpretation = IntegerRangeField('You like books and movies that make you come up with your own interpretation of the ending.')
    accomplish = IntegerRangeField('Your happiness comes more from helping others accomplish things than your own accomplishments.')
