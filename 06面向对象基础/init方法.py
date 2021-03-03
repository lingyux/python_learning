class Animal(object):
    def __init__(self):
        self.name = 'Jerry'
        self.color = 'blue'
        pass

    def eat(self):
        print('吃饭')
        pass


dog = Animal()
dog.color = 'white'
dog.name = 'Puppy'
print(dog.name)

cat = Animal()
cat.color = 'black'
cat.name = 'Tom'
print(cat.name)

mouse = Animal()
mouse.color = 'yellow'
print(mouse.name, mouse.color)
