#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import signal
import random

from PyQt4 import QtGui, QtCore, uic

import models


#.##........#######...######...####.##....##
#.##.......##.....##.##....##...##..###...##
#.##.......##.....##.##.........##..####..##
#.##.......##.....##.##...####..##..##.##.##
#.##.......##.....##.##....##...##..##..####
#.##.......##.....##.##....##...##..##...###
#.########..#######...######...####.##....##
class LoginForm(QtGui.QWidget):
	def __init__(self):
		super(LoginForm, self).__init__()
		self.initUI()

		#events:
		self.loginButton.clicked.connect(self.login)
		self.addButton.clicked.connect(self.add)

	def initUI(self):
		uic.loadUi("ui/login.ui", self)
		centerOnScreen(self)
		self.setFixedSize(self.size())
		self.passwordTextbox.setEchoMode(QtGui.QLineEdit.Password)

	def login(self):
		login = self.loginTextbox.text()
		password = self.passwordTextbox.text()

		if login and password:
			user = models.User.get((models.User.login == login) & (models.User.password == password))

			if user.role == "disp":
				self.f = DispForm(user)
			else:
				self.f = UserForm(user)

			self.f.show()
			self.close()
		
	def add(self):
		self.f = AddForm()
		self.f.show()
		self.close()


#....###....########..########.
#...##.##...##.....##.##.....##
#..##...##..##.....##.##.....##
#.##.....##.##.....##.##.....##
#.#########.##.....##.##.....##
#.##.....##.##.....##.##.....##
#.##.....##.########..########.
class AddForm(QtGui.QWidget):
	def __init__(self):
		super(AddForm, self).__init__()
		self.initUI()

		#events:
		self.sendButton.clicked.connect(self.addRecord)

	def initUI(self):
		uic.loadUi("ui/addform.ui", self)
		centerOnScreen(self)
		self.setFixedSize(self.size())
		self.passTextbox.setEchoMode(QtGui.QLineEdit.PasswordEchoOnEdit)

	def addRecord(self):
		name = self.nameTextbox.text()
		sername = self.sernameTextbox.text()
		adress = self.adressTextbox.text()
		firm = self.firmTextbox.text()
		model = self.modelTextbox.text()
		met_id = self.idTextbox.text()
		message = self.messageTextbox.toPlainText()
		login = self.loginTextbox.text()
		password = self.passTextbox.text()

		if name and sername and adress and firm and model and met_id and message and login and password:
			try:
				models.Add.create(name=name, sername=sername, adress=adress, firm=firm, model=model, met_id=met_id, message=message, login=login, password=int(password))
				self.close()
			except ValueError:
				print u'Пароль должен состоять только из цифр!'
		else:
			print u'Заполнены не все поля'


#.########..####..######..########.
#.##.....##..##..##....##.##.....##
#.##.....##..##..##.......##.....##
#.##.....##..##...######..########.
#.##.....##..##........##.##.......
#.##.....##..##..##....##.##.......
#.########..####..######..##.......
class DispForm(QtGui.QWidget):
	def __init__(self, user):
		super(DispForm, self).__init__()
		self.user = user
		self.initUI()
		
		#events:
		self.openreqestButton.clicked.connect(self.openRequestForm)
		self.openchatButton.clicked.connect(self.openChatForm)
		self.openmapButton.clicked.connect(self.openMapForm)
		self.showmeterButton.clicked.connect(self.showMeter)
		
	def initUI(self):
		uic.loadUi("ui/dispform.ui", self)
		self.setWindowTitle(u'Диспетчер %s %s' % (self.user.name, self.user.sername))
		centerOnScreen(self)
		self.setFixedSize(self.size())
		self.dataErrorHint.hide()
		self.adressLabel.hide()
		self.loginLabel.hide()
		self.dataLabel.hide()
		self.adressHint.hide()
		self.loginHint.hide()
		self.dataHint.hide()
		self.dateLabel.hide()
		self.nameLabel.hide()
		self.nameHint.hide()

	def openRequestForm(self):
		requests = models.Add.select().where(models.Add.status == 0)
		if requests.count():
			self.f = SelectIt(requests, flag="request")
		else:
			self.f = EmptyRequestForm()
		self.f.show()

	def openChatForm(self):
		argues = models.Chat.select().where(models.Chat.answer == '')
		if argues.count():
			self.f = SelectIt(argues, flag="argue")
		else:
			self.f = EmptyRequestForm()
		self.f.show()

	def openMapForm(self):
		self.o = MapForm()
		self.o.show()

	def showMeter(self):
		data = self.dataBox.text()

		if self.dataTypeBox.currentIndex() == 0 and data:
			self.dataErrorHint.hide()
			self.adressLabel.hide()
			self.loginLabel.hide()
			self.dataLabel.hide()
			self.adressHint.hide()
			self.loginHint.hide()
			self.dataHint.hide()
			self.dateLabel.hide()
			self.nameLabel.hide()
			self.nameHint.hide()
			try:
				meter = models.Meter.get(models.Meter.adress == data)
			except:
				self.dataErrorHint.show()
				self.dataErrorHint.setText(u'Нет данных, удовлетворяющих запрос')

		elif self.dataTypeBox.currentIndex() == 1 and data:
			self.dataErrorHint.hide()
			self.adressLabel.hide()
			self.loginLabel.hide()
			self.dataLabel.hide()
			self.adressHint.hide()
			self.loginHint.hide()
			self.dataHint.hide()
			self.dateLabel.hide()
			self.nameLabel.hide()
			self.nameHint.hide()

			try:
				meter = models.Meter.get(models.Meter.user == int(data))
			except ValueError:
				self.dataErrorHint.show()
				self.dataErrorHint.setText(u'Номер договора должен быть целым числом!')
			except models.Meter.DoesNotExist:
				self.dataErrorHint.show()
				self.dataErrorHint.setText(u'Нет данных, удовлетворяющих запрос')

		try:
			self.adressLabel.setText(meter.adress)
			self.loginLabel.setText(meter.user.login)
			self.dataLabel.setText(str(meter.record.data))
			self.nameLabel.setText(meter.user.name + ' ' + meter.user.sername)
			self.dateLabel.setText(str(meter.record.date.__format__("%H:%M %d.%m.%Y")))
			self.adressLabel.show()
			self.loginLabel.show()
			self.dataLabel.show()
			self.adressHint.show()
			self.loginHint.show()
			self.dataHint.show()
			self.dateLabel.show()
			self.nameLabel.show()
			self.nameHint.show()
		except:
			pass


#.########.##.....##.########..########.##....##.....########..########..#######..##.....##.########..######..########
#.##.......###...###.##.....##....##.....##..##......##.....##.##.......##.....##.##.....##.##.......##....##....##...
#.##.......####.####.##.....##....##......####.......##.....##.##.......##.....##.##.....##.##.......##..........##...
#.######...##.###.##.########.....##.......##........########..######...##.....##.##.....##.######....######.....##...
#.##.......##.....##.##...........##.......##........##...##...##.......##..##.##.##.....##.##.............##....##...
#.##.......##.....##.##...........##.......##........##....##..##.......##....##..##.....##.##.......##....##....##...
#.########.##.....##.##...........##.......##........##.....##.########..#####.##..#######..########..######.....##...
class EmptyRequestForm(QtGui.QWidget):
	def __init__(self):
		super(EmptyRequestForm, self).__init__()
		self.initUI()

	def initUI(self):
		uic.loadUi("ui/emptyrequestform.ui", self)
		self.setFixedSize(self.size())
		centerOnScreen(self)
		self.setWindowTitle(u'Нет записей')


#.########..########..#######..##.....##.########..######..########
#.##.....##.##.......##.....##.##.....##.##.......##....##....##...
#.##.....##.##.......##.....##.##.....##.##.......##..........##...
#.########..######...##.....##.##.....##.######....######.....##...
#.##...##...##.......##..##.##.##.....##.##.............##....##...
#.##....##..##.......##....##..##.....##.##.......##....##....##...
#.##.....##.########..#####.##..#######..########..######.....##...	
class RequestForm(QtGui.QWidget):
	action = QtCore.pyqtSignal()
	def __init__(self, id):
		super(RequestForm, self).__init__()
		self.id = id
		self.initUI()
		self.showInfo()

		#events:
		self.acceptButton.clicked.connect(self.accept)
		self.rejectButton.clicked.connect(self.reject)

	def initUI(self):
		uic.loadUi("ui/reqestForm.ui", self)
		self.setFixedSize(self.size())
		centerOnScreen(self)
		self.setWindowTitle(u'Заявка #%s' % str(self.id))

	def showInfo(self):
		self.rec = models.Add.get(models.Add.id == self.id)
		self.name = self.rec.name
		self.sername = self.rec.sername
		self.login = self.rec.login
		self.password = self.rec.password
		self.adress = self.rec.adress
		self.firm = self.rec.firm
		self.model = self.rec.model
		self.met_id = self.rec.met_id

		self.nameLabel.setText(self.rec.name)
		self.sernameLabel.setText(self.rec.sername)
		self.adressLabel.setText(self.rec.adress)
		self.firmLabel.setText(self.rec.firm)
		self.modelLabel.setText(self.rec.model)
		self.messageLabel.setText(self.rec.message)
	
	def accept(self):
		createUser = models.User.create(name=self.name, sername=self.sername, login=self.login, password=self.password, role='user')
		record = models.Record.create(data=random.randint(0,99999))
		models.Meter.create(adress=self.adress, firm=self.firm, model=self.model, met_id=self.met_id, user=createUser, record=record)
		models.Add.update(status=True).where(models.Add.id==self.rec.id).execute()
		self.action.emit()
		self.close()

	def reject(self):
		models.Add.update(status=True).where(models.Add.id==self.rec.id).execute()
		self.action.emit()
		self.close()


#.##.....##....###....########.
#.###...###...##.##...##.....##
#.####.####..##...##..##.....##
#.##.###.##.##.....##.########.
#.##.....##.#########.##.......
#.##.....##.##.....##.##.......
#.##.....##.##.....##.##.......
class MapForm(QtGui.QWidget):
	def __init__(self):
		super(MapForm, self).__init__()
		self.initUI()

	def initUI(self):
		uic.loadUi("ui/mapform.ui", self)
		self.setFixedSize(self.size())
		centerOnScreen(self)
		mapLabel = QtGui.QPixmap('q.jpg')


#..######..##.....##....###....########......########..####..######..########.
#.##....##.##.....##...##.##......##.........##.....##..##..##....##.##.....##
#.##.......##.....##..##...##.....##.........##.....##..##..##.......##.....##
#.##.......#########.##.....##....##.........##.....##..##...######..########.
#.##.......##.....##.#########....##.........##.....##..##........##.##.......
#.##....##.##.....##.##.....##....##.........##.....##..##..##....##.##.......
#..######..##.....##.##.....##....##.........########..####..######..##.......
class ChatDispForm(QtGui.QWidget):
	action = QtCore.pyqtSignal()
	def __init__(self, id):
		super(ChatDispForm, self).__init__()
		self.id = id
		self.initUI()
		self.showInfo()

		#events:
		self.sendButton.clicked.connect(self.send)

	def initUI(self):
		uic.loadUi("ui/chatdispform.ui", self)
		self.setFixedSize(self.size());
		centerOnScreen(self)
		self.setWindowTitle(u"Жалоба #%d" % self.id)

	def showInfo(self):
		self.rec = models.Chat.get(models.Chat.id == self.id)
		self.nameLabel.setText(self.rec.user.name)
		self.sernameLabel.setText(self.rec.user.sername)
		self.messageLabel.setText(self.rec.message)

	def send(self):
		textAnswer = self.answerTextbox.toPlainText()
		models.Chat.update(answer=textAnswer).where(models.Chat.id==self.rec.id).execute()
		self.action.emit()
		self.close()


#..######..########.##.......########..######..########......####.########
#.##....##.##.......##.......##.......##....##....##..........##.....##...
#.##.......##.......##.......##.......##..........##..........##.....##...
#..######..######...##.......######...##..........##..........##.....##...
#.......##.##.......##.......##.......##..........##..........##.....##...
#.##....##.##.......##.......##.......##....##....##..........##.....##...
#..######..########.########.########..######.....##.........####....##...
class SelectIt(QtGui.QWidget):
	def __init__(self, data, flag):
		super(SelectIt, self).__init__()
		self.flag = flag
		self.data = data
		self.initUI()
		
		#костыль:
		if self.flag == 'request':
			self.setListRequest(data)
			self.setWindowTitle(u"Заявки")
		elif self.flag == 'argue':
			self.setListArgue(data)
			self.setWindowTitle(u"Жалобы")
		else :
			self.setListAnswer(data)
			self.setWindowTitle(u"Ответы")

		#events:
		self.list.itemDoubleClicked.connect(self.showFullItem)
	
	def initUI(self):
		uic.loadUi("ui/selectit.ui", self)
		self.setFixedSize(self.size());
		centerOnScreen(self)

	def setListRequest(self, data):
		for item in data:
			self.list.addItem(u"Заявка #%d, от пользователя %s %s (%s)" %(item.id, item.name, item.sername, item.date.__format__("%d.%m.%Y")))

	def setListArgue(self, data):
		for item in data:
			self.list.addItem(u"Жалоба #%d, от пользователя %s %s (%s)" %(item.id, item.user.name, item.user.sername, item.date.__format__('%d.%m.%Y')))
	def setListAnswer(self, data):
		for item in data:
			self.list.addItem(u"Ответ #%d, от диспетчера (%s)" %(item.id, item.date.__format__("%d.%m.%Y")))

	def showFullItem(self):
		text = str(self.list.currentItem().text().toUtf8())
		s = text.index('#')
		f = text.index(',')
		text = text[s+1:f] #жутко смотреть
		id = int(text)
		if self.flag == 'request':
			self.request = RequestForm(id)
			self.f = self.request
			self.request.action.connect(self.requestTrigger)
		elif self.flag == 'argue':
			self.argue = ChatDispForm(id)
			self.f = self.argue
			self.argue.action.connect(self.argueTrigger)
		else:
			self.f = AnswerUserForm(id)
		self.f.show()

	def requestTrigger(self):
		self.list.clear()
		requests = models.Add.select().where(models.Add.status == 0)
		if requests.count():
			self.setListRequest(requests)
		else:
			self.close()

	def argueTrigger(self):
		self.list.clear()
		argues = models.Chat.select().where(models.Chat.answer == '')
		if argues.count():
			self.setListArgue(argues)
		else:
			self.close()


#.##.....##..######..########.########.
#.##.....##.##....##.##.......##.....##
#.##.....##.##.......##.......##.....##
#.##.....##..######..######...########.
#.##.....##.......##.##.......##...##..
#.##.....##.##....##.##.......##....##.
#..#######...######..########.##.....##
class UserForm(QtGui.QWidget):
	def __init__(self, user):
		super(UserForm, self).__init__()
		self.user = user
		self.initUI()
		self.met()

		#events:
		self.chatButton.clicked.connect(self.openChatUser)
		self.answerButton.clicked.connect(self.openAnswer)

	def initUI(self):
		uic.loadUi("ui/userform.ui", self)
		self.setFixedSize(self.size())
		centerOnScreen(self)
		self.setWindowTitle(u'Пользователь ' + self.user.name + ' ' + self.user.sername)

	def openAnswer(self):
		answer = models.Chat.select().where((models.Chat.answer != 0) & (models.Chat.user == self.user.id))
		if answer.count():
			self.f = SelectIt(answer, flag='answer')
		else:
			self.f = EmptyRequestForm()
		self.f.show()

	def openChatUser(self):
		self.f = ChatUserForm(self.user)
		self.f.show()

	def met(self):
		try:
			mets = list(models.Meter.select().where(models.Meter.user == self.user.id))
			self.dataLCD.display(mets[-1].record.data)
			self.timeLabel.setText(str(mets[-1].record.date.__format__("%H:%M %d.%m.%Y")))
		except:
			print u'Показаний нет'


#..######..##.....##....###....########.....##.....##..######..########.########.
#.##....##.##.....##...##.##......##........##.....##.##....##.##.......##.....##
#.##.......##.....##..##...##.....##........##.....##.##.......##.......##.....##
#.##.......#########.##.....##....##........##.....##..######..######...########.
#.##.......##.....##.#########....##........##.....##.......##.##.......##...##..
#.##....##.##.....##.##.....##....##........##.....##.##....##.##.......##....##.
#..######..##.....##.##.....##....##.........#######...######..########.##.....##
class ChatUserForm(QtGui.QWidget):
	def __init__(self, id):
		super(ChatUserForm, self).__init__()
		self.id = id
		self.initUI()

		#events:
		self.choiceBox.currentIndexChanged.connect(self.variety)
		self.sendButton.clicked.connect(self.sendmessage)
	
	def initUI(self):
		uic.loadUi("ui/chatuserform.ui", self)
		centerOnScreen(self)
		self.commentHint.hide()
		self.metTextbox.hide()
		self.progTextbox.hide()
		self.messageTextbox.hide()
		self.sendButton.hide()
		self.size = self.geometry()
		self.resize(self.width(), self.height()-350)

	def variety(self):
		if self.choiceBox.currentIndex() == 0:
			self.commentHint.hide()
			self.metTextbox.hide()
			self.progTextbox.hide()
			self.messageTextbox.hide()
			self.sendButton.hide()
			self.resize(self.width(), self.height()-350)
	
		elif self.choiceBox.currentIndex() == 1:
			self.setGeometry(self.size)
			self.commentHint.hide()
			self.metTextbox.hide()
			self.progTextbox.hide()
			self.messageTextbox.show()
			self.sendButton.show()
			self.messageTextbox.setGeometry(40, 120, 271, 251)
			self.messageTextbox.move(self.messageTextbox.x(), self.messageTextbox.y()-50)
			self.messageTextbox.resize(self.messageTextbox.width(), self.messageTextbox.height()+50)

		elif self.choiceBox.currentIndex() == 2:
			self.setGeometry(self.size)	
			self.commentHint.show()
			self.metTextbox.show()
			self.progTextbox.show()
			self.messageTextbox.setGeometry(40, 120, 271, 251)
			self.messageTextbox.show()
			self.sendButton.show()

	def sendmessage(self):
		if self.choiceBox.currentIndex() == 1:
			message = self.messageTextbox.toPlainText()

		elif self.choiceBox.currentIndex() == 2:	
			message = u"Показания в программе " + self.progTextbox.text() + u" Показания на счетчике " + self.metTextbox.text() + u" Проблема: " + self.messageTextbox.toPlainText()

		if  message:
			models.Chat.create(message=message, user=self.id)
			self.close()


#....###....##....##..######..##......##.########.########......##.....##..######..########.########.
#...##.##...###...##.##....##.##..##..##.##.......##.....##.....##.....##.##....##.##.......##.....##
#..##...##..####..##.##.......##..##..##.##.......##.....##.....##.....##.##.......##.......##.....##
#.##.....##.##.##.##..######..##..##..##.######...########......##.....##..######..######...########.
#.#########.##..####.......##.##..##..##.##.......##...##.......##.....##.......##.##.......##...##..
#.##.....##.##...###.##....##.##..##..##.##.......##....##......##.....##.##....##.##.......##....##.
#.##.....##.##....##..######...###..###..########.##.....##......#######...######..########.##.....##
class AnswerUserForm(QtGui.QWidget):
	def __init__(self, id):
		super(AnswerUserForm, self).__init__()
		self.answer = models.Chat.get(models.Chat.id == id)
		self.initUI()
		self.showInfo()

	def initUI(self):
		uic.loadUi("ui/answeruserform.ui", self)
		self.setFixedSize(self.size())
		centerOnScreen(self)
		self.setWindowTitle(u"Ответ #%d" % self.answer.id)

	def showInfo(self):
		self.nameLabel.setText(self.answer.user.name)
		self.sernameLabel.setText(self.answer.user.sername)
		self.messageLabel.setText(self.answer.message)
		self.answerLabel.setText(self.answer.answer)


#..######...##........#######..########.....###....##......
#.##....##..##.......##.....##.##.....##...##.##...##......
#.##........##.......##.....##.##.....##..##...##..##......
#.##...####.##.......##.....##.########..##.....##.##......
#.##....##..##.......##.....##.##.....##.#########.##......
#.##....##..##.......##.....##.##.....##.##.....##.##......
#..######...########..#######..########..##.....##.########
def centerOnScreen(self):
	resolution = QtGui.QDesktopWidget().screenGeometry()
	self.move(resolution.width()/2 - self.frameSize().width()/2, resolution.height()/2 - self.frameSize().height()/2 )


def main():
	signal.signal(signal.SIGINT, signal.SIG_DFL)
	app = QtGui.QApplication(sys.argv)
	w = LoginForm()
	w.show()
	sys.exit(app.exec_())


if __name__ == '__main__':
	main()