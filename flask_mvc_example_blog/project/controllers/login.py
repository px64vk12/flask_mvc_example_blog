# -*- coding: utf-8 -*-

from project import app
from datetime import timedelta
from flask import render_template, request, url_for, redirect, session
from ..models.User import *

# todo session timeout
@app.route("/")
@app.route("/main")
def main():
    return redirect(url_for('.login'))


@app.route("/login", methods=['POST','GET'])
def login():
    # 로그인 페이지 진입
    if request.method == 'GET':
        session.clear()
        return render_template('login/login.html')
    # 로그인 행위
    if request.method == 'POST':
        user_id = request.form["user_id"]
        user_pw = request.form["user_pw"]
        print(user_id, user_pw)
        user = User.read(user_id, user_pw)
        if user != None:
            session['user'] = user.toJson()
            return redirect(url_for('.home'))
        return render_template('login/login.html')
    




    