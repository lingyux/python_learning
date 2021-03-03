class People(object):
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
        pass

    def talk(self, food):
        print('I am {},I am a {},I am {} years old,I like eating {}'.format(
            self.name, self.sex, self.age, food))
        pass


lingyux = People('lingyux', 20, 'man')
print(lingyux.name, lingyux.age, lingyux.sex)

lingyux.talk('fish')
