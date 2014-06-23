#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
from peewee import *
db = MySQLDatabase('ipu', user='amel', passwd='')

class MySQLModel(Model):
	class Meta:
		database = db

class User(MySQLModel):
	login = CharField()
	password = IntegerField()
	name = CharField()
	sername = CharField()
	role = CharField()

class Chat(MySQLModel):
	message = TextField()
	answer = TextField(default='')
	user = ForeignKeyField(User, related_name='chat')
	date = DateField(default=datetime.datetime.now())

class Record(MySQLModel):
	data = IntegerField()
	date = DateTimeField(default=datetime.datetime.now())

class Meter(MySQLModel):
	user = ForeignKeyField(User, related_name='meters')
	adress = CharField()
	firm = CharField()
	model = CharField()
	met_id = CharField()
	record = ForeignKeyField(Record, related_name='records', null=True)

class Add(MySQLModel):
	message = TextField()
	name = CharField()
	sername = CharField()
	login = CharField()
	password = IntegerField()
	adress = CharField()
	firm = CharField()
	model = CharField()
	met_id = CharField()
	status = BooleanField(default=False)
	date = DateField(default=datetime.datetime.now())





