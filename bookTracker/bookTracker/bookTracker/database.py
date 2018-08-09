from flask import Flask
from flask_sqlalchemy import *
from flask_sqlalchemy import SQLAlchemy
from bookTracker import app
#initializes the database and allows for the creation of tables within mysql

#make sure you change the username(admin) and password(Group2017) before you run db.createall() as this will not connect to your database
#When running in python interactive make sure you do from battersbox.Database import db before you run db.create_all() or it will not know whats going on
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:0000@localhost/bookTracker'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db = SQLAlchemy(app)

class Book(db.Model):
    __tablename__ = 'book'
    id = db.Column(db.Integer,primary_key = True,autoincrement = True)
    title = db.Column(db.String(80))
    author_id = db.Column(db.String(80))
    genre = db.Column(db.String(80))
    publisher_id = db.Column(db.String(80))
    year = db.Column(db.Integer)
    printing = db.Column(db.Integer)
    first_edition = db.Column(db.Boolean)
    description = db.Column(db.String(500))
    condition = db.String(db.String(80))
    notes = db.String(db.String(80))
    #relationships
    #function definitions
    def __repr__(self):
        return '<book %r>' % self.name
    def __init__(self,title,author_id,publisher,year,printing,first_edition,description,condition,notes):
        self.title = title
        self.author_id = author_id
        self.plublisher = publisher
        self.year = year
        self.printing = printing
        self.first_edition = first_edition
        self.description = description
        self.condition = condition
        self.notes = notes

class Author(db.Model):
    __tablename__='author'
    id = db.Column(db.Integer,primary_key = True,autoincrement=True)
    name = db.Column(db.String(80))
    birth = db.Column(db.Integer)
    death = db.Column(db.Integer)
    #relationships
        #db.relationship('Coaches',backref='salaries') --previous relationship example
        #db.relationship('Player',backref='salaries')
    #function definitions
    def __repr__(self):
        return '<author %r>' % self.salary_amount
    def __init__(self,name,birth,death):
        self.name = name
        self.birth = birth
        self.death = death

class Publisher(db.Model):
    __tablename__ = 'publisher'
    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    name = db.Column(db.String(80), unique=True)
    #relationships
    #function definitions
    def __repr__(self):
        return '<Publisher %r>' % self.name
    def __init__(self,name):
        self.name = name