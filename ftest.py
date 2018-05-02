from singledispatchann import singledispatchann

class C:
  @singledispatchann
  def xx(self, a):
    print('C.fff')
    return 0

  @xx.register()
  def f(self, a: int) -> int:
    print('C.f')
    return a + 1

  @xx.register()
  def ff(self, a: dict) -> int:
    print('C.ff')
    return 0


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

c = C()
c.xx(1)
c.xx({})
