# https://stackoverflow.com/questions/6760685/creating-a-singleton-in-python
# http://python-3-patterns-idioms-test.readthedocs.io/en/latest/Singleton.html


class OnlyOne:
    class __OnlyOne:
        def __init__(self, arg):
            self.val = arg

    instance = None

    def __init__(self, arg):
        if not OnlyOne.instance:
            OnlyOne.instance = OnlyOne.__OnlyOne(arg)
        else:
            OnlyOne.instance.val = arg

    def __getattr__(self, name):
        return getattr(self.instance, name)


x = OnlyOne('sausage')
print(x)
y = OnlyOne('eggs')
print(y)
z = OnlyOne('spam')
print(z)
print(x)
print(y)
