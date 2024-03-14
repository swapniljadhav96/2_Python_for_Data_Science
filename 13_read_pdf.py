# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 12:24:55 2024

@author: suraj
"""

####**************read the PDF file***************
#install PyPDF2 :'pip install PyPDF2'
from PyPDF2 import PdfFileReader
#importing the required modules
from PyPDF2 import PdfReader

#creating the a pdf reader object
reader = PdfReader('C:/Data Science/1-python/OSA_report.pdf')

#printing the number of pages in the pdf
print(len(reader.pages))


####
#getting the a sepicfic pages from the pdf file
page = reader.pages[11]

####
#extracting text from pages
text = page.extract_text()
print(text)

####Quick reference take website use the "regex101.com/'
#in this websie we get the all ready refence which is uesd in the pdf extraction process
#1.comman token 2.all tokens
##########
#checking the pattern with the special command
#
import re
chat2='Hi I have a problem with my order number 412889912'
pattern ='order[^\d]*(\d*)'
matches=re.findall(pattern,chat2)
matches


