from singledispatchann import singledispatchann

  
@singledispatchann
def x(x):
  return x

@x.register()
def f(a: int) -> int:
  print('f')
  return a + 1

@x.register()
def ff(a: dict) -> int:
  print('ff')
  return 0

x(1)
x({})
