from flask import after_this_request
from sqlalchemy.sql import func
from . import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    userId = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    usernname = db.Column(db.String(100))

class ArtworkOrder(db.Model):
    customer_id
    customer_name
    customer_phone
    order_date
    order_price
    apparel
    base_color
    max_color
    art_location
    description
    cost
    employee
    date_complete


class PrintOrder(db.Model):
    customer_id
    customer_name
    customer_phone

    order_date
    due_date
    print_date
    date_delivered

    setup_charge
    deposit 
    discount
    total_cost

    s_number
    s_charge
    l_number
    l_charge

   


class CostAnalysis(db.Model):
    


class EmployeeManagement(db.Model):
    employee_id = db.Column(db.Integer, primary_key=True)
    employee_name = db.Column(db.Integer, primary_key=True)
    employee_phone = db.Column(db.Integer, primary_key=True)
    employee_jobtype = db.Column(db.Integer, primary_key=True)
    project = db.Column(db.String(100), null = True)
    task = db.Column(db.String(100), null = True)
    start_time = db.Column(db.Integer(100), null = True)
    end_time = db.Column(db.Integer(100), null = True)



