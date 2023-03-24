# -*- coding: utf-8 -*-
from project import app
from flask import render_template, request, url_for, redirect, session
from ..models.Category import *


@app.route('/home')
def home():
    print('/home')
    try:
        categorys = Category.read(session['user']['user_id'],name = None)
        return render_template('home/home.html', categorys=categorys)
    except:
        return redirect(url_for('.login'))


@app.route("/category/manage_category", methods=['POST'])
def create_category():
    if request.method == 'POST':
        print(request.form)
        action = request.form["action"]
        if action == "create":
            category_user = session['user']['user_id']
            category_name = request.form["category_name"]
            category = Category(category_user,category_name)
            category.create()    
            return redirect(url_for('.home'))
        if action == "delete":
            category_user = session['user']['user_id']
            category_name = request.form["category_name"]
            category = Category.read(category_user,category_name)
            category.delete()
            return redirect(url_for('.home'))
            

