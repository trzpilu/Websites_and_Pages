import flask
from flask import render_template, request, flash, redirect, url_for, session
from blog import app
from blog.models import Entry, db
from blog.forms import EntryForm, LoginForm
import functools

@app.route("/")
def index():
    all_posts = Entry.query.filter_by(is_published=True).order_by(Entry.pub_date.desc())
    errors = flask.request.args.get('errors') #error message

    return render_template("homepage.html", all_posts=all_posts, errors=errors)

def login_required(view_func):
   @functools.wraps(view_func)
   def check_permissions(*args, **kwargs):
       if session.get('logged_in'):
           return view_func(*args, **kwargs)
       return redirect(url_for('login', next=request.path))
   return check_permissions

def new_or_edit(form, entry_id=None, entry=None, errors=None):
    if form.validate_on_submit():
        if entry_id == None:
            entry = Entry(
                title = form.title.data,
                body = form.body.data,
                is_published = form.is_published.data,
            )
            db.session.add(entry)
            flash('New post added. Abrakadabra!')
        else:
            form.populate_obj(entry)
            flash('Post updated. Shazzam!')
        db.session.commit()
        return None
    else:
        return flask.redirect(flask.url_for('index', errors=errors))

@app.route("/new-post/", methods=["GET", "POST"])
@login_required
def create_entry():
    form = EntryForm()
    errors = None
    
    if request.method == 'POST':
        errors = new_or_edit(form) 
        return redirect(url_for('index', errors=errors)) #error message

    return render_template("entry_form.html", form=form, errors=errors)


@app.route("/edit-post/<int:entry_id>/", methods=["GET", "POST"])
@login_required
def edit_entry(entry_id):
    entry = Entry.query.filter_by(id=entry_id).first_or_404()
    form = EntryForm(obj=entry)
    errors = None

    if request.method == 'POST':
        errors = new_or_edit(form, entry_id=entry_id, entry=entry)
        return redirect(url_for('index'))

    return render_template("entry_form.html", form=form, errors=errors)

#Old functions listed below, before being recombined into the three above
"""
@app.route("/new-post/", methods=["GET", "POST"])
def create_entry():
   form = EntryForm()
   errors = None
   if request.method == 'POST':
       if form.validate_on_submit():
           entry = Entry(
               title=form.title.data,
               body=form.body.data,
               is_published=form.is_published.data
           )
           db.session.add(entry)
           db.session.commit()
       else:
           errors = form.errors
   return render_template("entry_form.html", form=form, errors=errors)

@app.route("/edit-post/<int:entry_id>", methods=["GET", "POST"])
def edit_entry(entry_id):
   entry = Entry.query.filter_by(id=entry_id).first_or_404()
   form = EntryForm(obj=entry)
   errors = None
   if request.method == 'POST':
       if form.validate_on_submit():
            form.populate_obj(entry)
            db.session.commit()
       else:
           errors = form.errors
   return render_template("entry_form.html", form=form, errors=errors)

"""
@app.route("/login/", methods=['GET', 'POST'])
def login():
   form = LoginForm()
   errors = None
   next_url = request.args.get('next')
   if request.method == 'POST':
       if form.validate_on_submit():
           session['logged_in'] = True
           session.permanent = True  # Use cookie to store session.
           flash('You are now logged in.', 'success')
           return redirect(next_url or url_for('index'))
       else:
           errors = form.errors
   return render_template("login_form.html", form=form, errors=errors)


@app.route('/logout/', methods=['GET', 'POST'])
def logout():
   if request.method == 'POST':
       session.clear()
       flash('You are now logged out.', 'success')
   return redirect(url_for('index'))

   
@app.route("/drafts/", methods=['GET'])
@login_required
def list_drafts():
   drafts = Entry.query.filter_by(is_published=False).order_by(Entry.pub_date.desc())
   return render_template("drafts.html", drafts=drafts)

@app.route("/delete-post/<int:entry_id>/", methods=["POST"])
@login_required
def delete_entry(entry_id):
    entry = Entry.query.filter_by(id=entry_id).first_or_404()
    db.session.delete(entry)
    db.session.commit()
    flash('By the power of Ethernia! Post has been deleted')
    return redirect(url_for('index'))
