# -*- coding: utf-8 -*-
#!/usr/bin/env python
#https://github.com/globalaplication/gnome.background/blob/master/config.py
#https://github.com/globalaplication/manager.file
#V2.1
import os
class Load (object):
	def __init__(self, file="/var/tmp/data"):
		""" eğer tanımlama yapılmazsa tmp klasörüne anahtarlar için 
		data isminde dosya oluşturulur"""
		self.file, self.keys = file, list()
		if os.path.exists(file) is False:
			os.system("{} {}".format("touch", 
			file))
		for test in open(file):
			self.keys.append(test.strip(
			"\n").split(":")[0])
	def get (self, key=""):
		"anahtar değerini öğrenmek için kullan"
		if len(key) is 0: 
			return None
		if key not in self.keys:
			return "None"
		for test in open(self.file):
			if test.split(":")[0] == key:
				value = test.split(":")[1].strip("\n")
		return value
	def set (self, dic, overwrite=True, string = ""):
		"""yeni bir anahtar oluşturmak için kullan 
		key:anahtar value:değer"""
		for beta in self.keys:	
			if beta in self.keys and overwrite is True:
				if dic.get(beta) is None:
					string = string + "{}:{}\n".format(beta, 
					self.get(beta))
				else:
					string = string + "{}:{}\n".format(beta, 
					dic.get(beta))
		if overwrite is True:
			for beta in dic:
				if beta not in self.keys:
					string = string + "{}:{}\n".format(beta, 
					dic.get(beta))
		for beta in self.keys:	
			if beta in self.keys and overwrite is False:
				if dic.get(beta) is None:
					string = string + "{}:{}\n".format(beta, 
					self.get(beta)) 
				else:
					string = string + "{}:{}\n".format(beta, 
					self.get(beta))
		if overwrite is False:
			for beta in dic:
				if beta not in self.keys:
					string = string + "{}:{}\n".format(beta, 
					dic.get(beta))
		with open(self.file, "w") as data:
			data.write(string)
		return string
	def keyList(self):
		keys_list = list()
		for test in open(self.file):
			keys_list.append(test.split(
			":")[0])
		return keys_list
	def info (self):
		return 
data = Load("./data.op")
data.set({"a":"a1", "b":"b1", "e":"e1"}, overwrite=True)

