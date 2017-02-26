def a(x, y):
  print x, y
def b(other,function,*args,**kwargs):
  function(*args,**kwargs)
  print other
b('world',a,'hello','dude')
