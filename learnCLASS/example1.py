#!/usr/bin/env python
"""
example of a class
define a class, define firstname,lastname,account-no,initial-deposit and print out.
"""
class Account:
  
  def __init__(self, firstname,lastname,account,deposit):
    self.__fname=firstname
    self.__lname=lastname
    self.__acctno=account
    self.__dep=deposit

  def get_balance(self):
    print "first name ",self.__fname
    print "last name ",self.__lname
    print "account number",self.__acctno
    print "deposit amount",self.__dep
  
def main():
  samy=Account("sameer","gawande","1234",12000)
  print samy.get_balance()

if __name__=="__main__":
  main()
