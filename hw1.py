# Name: Choya Vann 
# Evergreen Login: vancho06 
# Computer Science Foundations 
# Programming as a Way of Life 
# Homework 1 
# You may do your work by editing this file, or by typing code at the # command line and copying it into the appropriate part of this file when # you are done. 
#When you are done, running this file should compute and # print the answers to all the problems. 
import math # makes the math.sqrt function available ### 
### Problem 1 ###
print "Problem 1 solution follows:"
print "x-5.86 x+8.5408" 
bit = math.sqrt((0-5.86)**2-4*8.5408)
plus = (5.86 + bit)/2
minus = (5.86- bit)/2
print "value 1"
print plus
print "value 2"
print minus
### Problem 2 ### 
print "Problem 2 solution follows:"
import hw1_test
print hw1_test.a
print hw1_test.b
print hw1_test.c
print hw1_test.d
print hw1_test.e
print hw1_test.f
### Problem 3 ### 
print "Problem 3 solution follows:" 
import hw1_test
print ((hw1_test.a and hw1_test.b) or (not hw1_test.c) and not (hw1_test.d or hw1_test.e or hw1_test.f))
# ... write your code and comments here (and remove this line) ### 
### Collaboration  witha lot of help from Cody Swearingen and University of Washington.###  
#List your collaborators here, as a comment (on a line starting with "#").# 
# a lot of help from Cody Swearingen and University of Washington website suggesting use of a double or single loop.#