# -*- coding: utf-8 -*-
from project import app
from flask import render_template, request, url_for, redirect,session
from ..models.Page import *
from ..models.Category import *


@app.route('/category/<select_category>')
def category(select_category):
    print('/category')
    print(select_category)
    category = Category.read(
        user_id = session['user']['user_id'],
        name = select_category 
        ) 
    # 카테고리 조회를 실패한다면 홈으로 
    if category == None:
        return redirect(url_for('.home'))
        
        
    session['select_category'] = select_category
    pages = Page.read(
        user_id  = session['user']['user_id'], 
        category = session['select_category'])
    
    return render_template('category/category.html',
                           category=category.toJson(), 
                           pages=pages)


@app.route("/page/manage_page", methods=['POST'])
def manage_page():
    if request.method == 'POST':
        action = request.form["action"]
        if action == "create":
            user_id         = session['user']['user_id']
            category        = session['select_category']
            page_name       = request.form["page_name"]
            page_content    = request.form["page_content"]
            page = Page(user_id, category, page_name, page_content)
            page.create()
            return redirect("/category/"+category)
        if action == "delete":
            user_id = session['user']['user_id']
            category = session['select_category']
            page_name = request.form["page_name"]
            page_content = request.form["page_content"]
            page = Page.read(user_id, category, page_name)
            page.delete()
            return redirect("/category/"+category)
