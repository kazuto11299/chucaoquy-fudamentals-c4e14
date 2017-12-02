# tuananh = ["Tuan Anh", 22, "Moc Chau", 2, True, 4, 20]
# tuananh = {
#
# }
# tuananh ={
#     "name": "Tuan Anh"
# }
tuananh = {
    "name": "Tuan Anh",
    "age": 22,
    "home": "Moc Chau",
    "in relationship": True,
    "projects": 4
}
# print(tuananh["in relationship"])
tuananh["in relationship"] = False
print(tuananh)
tuananh["projects"] += 1
print(tuananh)
tuananh['extra hours'] = 20
print(tuananh)
#dictionary
del tuananh["in relationship"]
print(tuananh)
