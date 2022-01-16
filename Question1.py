#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 15:58:23 2022

@author: Ulugbeck
"""

import datetime
import random

date = datetime.datetime.now()
lucky_number = (random.randrange(1, 101))
  
     
date = (date.strftime("%d %b %y"))

first_name = "Mike"
	
  
       

class LuckyNumber():
  

  
  def generate_data(date,lucky_number):
     print(date,lucky_number)
     
     
  def display_data(generate_data):
     txt = (f"Hello {first_name}, your lucky number for {date} is: {lucky_number:.2f}")
     print(txt)
        
        
x = LuckyNumber

print(x.display_data(1))