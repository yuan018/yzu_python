
from datetime import date
from lesson09.orm.PeeweeCreateTable import Person, Pet

bob = Person(name='Bob', birthday=date(1985, 1, 15))
bob.save()
mary = Person.create(name='Mary', birthday=date(1995, 3, 1))
herb = Person.create(name='Herb', birthday=date(1970, 5, 5))

kitty = Pet.create(owner=bob, name='Kitty', animal_type='cat')
fido = Pet.create(owner=herb, name='Fido', animal_type='dog')
lucky = Pet.create(owner=herb, name='Lucky', animal_type='cat')
happy = Pet.create(owner=herb, name='Happy', animal_type='cat')