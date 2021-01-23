from flask import url_for, redirect, flash, jsonify, request
from url_shortener import app, db
# Uncomment the two lines below to implement Model and Form
from url_shortener.models import URL
import shortuuid
import re

def validate_short_url(short_url):
    if re.match('(\w)+$', short_url):
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

@app.route('/', methods=['POST'])
def home():
    data = request.get_json()

    if 'short_url' in data:
        if (len(short_url := data['short_url'].strip()) > 0):
            if not validate_short_url(short_url):
                return jsonify({ 'message' : f'{short_url} can only contain alphanumeric character and _' })
            if short_url_exists(short_url):
                return jsonify({ 'message' : f'{short_url} is already in use' })
        else:
            short_url = generate_short_url()
    else:
        short_url = generate_short_url()

    if len(redirect_url := data['redirect_url'].strip()) > 0:
        url = URL(short_url=short_url, redirect_url=redirect_url)
        db.session.add(url)
        db.session.commit()

        return jsonify({ 'message' : f'succesfully added {short_url}' })
    else:
        return jsonify({ 'message' : 'url cannot be empty!' })


@app.route('/<short_url>', methods=['GET'])
def redirect_to(short_url):
    url = URL.query.filter_by(short_url=short_url).first()

    if url:
        return redirect(f'http://{url.redirect_url}')
    else:
        return jsonify({ 'message' : 'url not found' })