from app import app
from app.forms import JoinMailingListForm
from flask import render_template, url_for

@app.route('/', methods=['GET','POST'])
def landingpage():
    form = JoinMailingListForm()
    if form.validate_on_submit():
        return render_template('success.html')
    return render_template('index.html', form=form)