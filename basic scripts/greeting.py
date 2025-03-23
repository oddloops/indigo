#!/usr/bin/python3

def basic_greeting(fname, lname, state):
  print("Hello dearest %s %s. How is the weather in %s?" % (fname, lname, state))

first_name = 'Malory'
last_name = 'Archer'
state = 'New York'

basic_greeting(first_name, last_name, state)