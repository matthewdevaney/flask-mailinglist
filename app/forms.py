from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email, Length  


class JoinMailingListForm(FlaskForm):
    email = StringField('Sign Up',
                        validators=[Length(min=1, max=128, message='Error: email address must be between 1-128 characters'),
                                    Email("Error: must be a valid email address")],
                        render_kw={
                            'class': 'form-control mr-2',
                            'placeholder': 'Your Email Here...',
                            'size': 30 
                        })
                        
    submit = SubmitField('Submit',
                         render_kw={
                             'class': 'btn btn-success'
                         })
                          
