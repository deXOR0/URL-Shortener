from flask import url_for, redirect, flash, jsonify, request, render_template
from url_shortener import app, db, bcrypt
# Uncomment the two lines below to implement Model and Form
from url_shortener.models import URL
from url_shortener.forms import URL as url_form, URL_Verification as url_verification_form
import shortuuid
import re

def validate_short_url(short_url):
    if re.match('^[A-Za-z0-9_-]+$', short_url):
        return True
    return False

def short_url_exists(short_url):
    url = URL.query.filter_by(short_url=short_url).first()
    url_exists = True if url is not None else False
    return url_exists

def generate_short_url():

    short_url = ''
    
    while True: # Mimmicks do while behavior
        short_url = shortuuid.ShortUUID().random(length=5)

        if not short_url_exists(short_url):
            break;

    return short_url

@app.route('/', methods=['GET', 'POST'])
def idx():
    form = url_form()

    if form.validate_on_submit():
        short_url = form.short_url.data
        if (len(short_url := short_url.strip()) > 0):
            if not validate_short_url(short_url):
                return jsonify({ 'message' : f'{short_url} can only contain alphanumeric character, - and _' })
            if short_url_exists(short_url):
                return jsonify({ 'message' : f'{short_url} is already in use' })
        else:
            short_url = generate_short_url()
        
        redirect_url = form.url.data
        if redirect_url.startswith('http://'):
            redirect_url = redirect_url.replace('http://', '')
        elif redirect_url.startswith('https://'):
            redirect_url = redirect_url.replace('https://', '')
        if len(redirect_url := redirect_url.strip()) > 0:
            if form_password := form.password.data:
                password = bcrypt.generate_password_hash(
                form_password).decode('utf-8')
                url = URL(short_url=short_url, redirect_url=redirect_url, password=password)
            else :
                url = URL(short_url=short_url, redirect_url=redirect_url)
            db.session.add(url)
            db.session.commit()

            return render_template('post-creation.html', url=f'{request.base_url}{short_url}')
        else:
            return jsonify({ 'message' : 'url cannot be empty!' })

    return render_template('index.html', form=form)
    
@app.route('/<short_url>', methods=['GET', 'POST'])
def redirect_to(short_url):
    url = URL.query.filter_by(short_url=short_url).first()

    if url:
        if url.password:
            form = url_verification_form()
            if form.validate_on_submit():
                if bcrypt.check_password_hash(url.password, form.password.data):
                    return redirect(f'http://{url.redirect_url}')
                else :
                    flash('Password mismatch!')
            return render_template('verification.html', form=form)

        return redirect(f'http://{url.redirect_url}')
    else:
        return jsonify({ 'message' : 'url not found' })
