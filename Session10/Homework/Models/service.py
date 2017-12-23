from mongoengine import *
class river(Document):
    name = StringField()
    continent = StringField()
    length = IntField()
    def __str__(self):
        return "{0} - {1} - {2}".format(self.name, self.continent, self.length)
