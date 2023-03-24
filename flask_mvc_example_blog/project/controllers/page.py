# -*- coding: utf-8 -*-
from project import app
from flask import render_template, request, url_for, redirect, session
from ..models.Page import *


@app.route('/page/<select_page>')
def page(select_page):
    print('/page')
    user = session['user']['user_id']
    select_category = session['select_category']
    page = Page.read(user, select_category, select_page)
    page = page.toJson()
    return render_template('page/page.html', page=page)
