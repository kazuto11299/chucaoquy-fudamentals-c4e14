from mongoengine import Document, StringField, IntField, BooleanField
class Service(Document):
    account = StringField()
    game = StringField()
    price = StringField()
    contact = IntField()
    occupied = BooleanField()
