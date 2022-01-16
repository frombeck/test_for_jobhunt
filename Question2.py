#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 20:48:52 2022

@author: Ulugbeck
"""

def encodeString(Str):
  
    map = {}
    res = ""
    i = 0

    for ch in Str:

        if ch not in map:
            map[ch] = i
            i += 1
            

        res += str(map[ch])
    return res

def get_matches(words, pattern):

    Len = len(pattern)

    hash = encodeString(pattern)

    for word in words:


        if(len(word) == Len and
           encodeString(word) == hash):
            print(word, end = " ")
 
words = ["a", "wwffw", "xxccx", "xxhhi", "aaaaa", "aaaa", "wwccw", "qqffqq"]
pattern = "aabba"
get_matches(words, pattern)