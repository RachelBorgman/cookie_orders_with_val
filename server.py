from flask import render_template, session, redirect, request
from flask_app.controllers import cookie_orders
from flask_app import app

if __name__=="__main__":
    app.run(debug=True, host="localhost", port=5005)