#!/usr/bin/env python
class Person:
  """
  Write some documentation explaining the purpose of the class
  """
  def __init__(self,name,email,phone):
    ##constructor
    self.Name = name
    self.Email = email
    self.Phone = phone
  def getname(self):
    return self.Name
  def getphone(self):
    return self.Phone
  def getemail(self):
    return self.Email
  def changenumber(self,number):
    self.Phone = number

def main():
  """
  create instance
  """
  p = Person("sameer","samy@yahoo.com","111-222-3345")
  print p.getname()
  p.changenumber('555-666-7777')
  print p.getphone()

if __name__ == "__main__":
  main()
