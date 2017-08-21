#!/usr/bin/env python
#coding:utf-8
from selenium import webdriver

class Qiubai:
	def __init__(self):
		self.dr = webdriver.Chrome(executable_path='C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
		self.dr.get('https://www.qiushibaike.com/')

	def print_content(self):
		main_content = self.dr.find_element_by_id('content-left')
		contents = main_content.find_elements_by_class_name('content')

		i = 1
		for content in contents:
			print(str(i)+'.'+content.text+'\n')
			i += 1

		self.quit()

	def quit(self):
		self.dr.quit()

Qiubai().print_content()
#Qiubai()