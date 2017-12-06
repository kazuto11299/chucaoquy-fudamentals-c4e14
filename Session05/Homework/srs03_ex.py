# from pymongo import MongoClient
# client = MongoClient('mongodb://admin:admin@ds021182.mlab.com:21182/c4e')
# db_c4e = client.get_default_database()
# customers = db_c4e['customers'].find()
# count_ads = 0
# count_wom = 0
# count_event = 0
# for customer in customers:
#     if customer['ref'] == 'ads':
#         count_ads += 1
#     elif customer['ref'] == 'wom':
#         count_wom += 1
#     elif customer['ref'] == 'event':
#         count_event += 1
# print('''Reference:
#     {0}Advertisement
#     {1}Word of Mouth
#     {2}
# Event'''.format(count_ads, count_wom, count_event))
#
# import matplotlib
# matplotlib.use('TkAgg')
#
# from matplotlib import pyplot
# labels = ['Advertisement', 'Word of Mouth', 'Event']
# colors = ['#49aaff', '#fc626f', '#fcff84']
# data = [count_ads, count_wom, count_event]
# pyplot.pie(data, labels = labels, colors = colors, autopct = '%1.2f%%')
# pyplot.axis('equal')
# pyplot.show()
