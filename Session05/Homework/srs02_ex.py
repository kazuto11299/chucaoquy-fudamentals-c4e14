from pymongo import MongoClient
client = MongoClient('mongodb://admin:admin@ds021182.mlab.com:21182/c4e')
db_c4e = client.get_default_database()
post = db_c4e['posts']
new_post = {
    'title': 'Đời Ngược Xuôi',
    'author': 'Tùng Trần',
    'content': '''Mệt mỏi rồi bao năm tháng ngược xuôi
Đã nếm đủ vị đời trong nước mắt
Dù cố gắng nâng niu và lượm nhặt
Từng nụ cười vẫn chẳng nắm chặt tay

Nhưng ông trời thì lại cứ mỉa mai
Luôn mang đến những đắng cay hờn tủi
Có nhiều khi âm thầm tôi tự hỏi
Mình đã sai và lầm lỗi chổ nào

Mà kéo dài theo năm tháng khổ đau
Bước chênh chao trên đường đời mấp mé
Kiếp nổi trôi bước chân trần cô lẻ
Chẳng biết mình rồi sẽ phải về đâu

Hay bẽ bàng giữa nơi chốn bể dâu
Là số phận không thể nào thoát được
Nên dẫu có bốn ba đời xuôi ngược
Mãi chỉ là dòng nước mắt tuôn rơi?'''
}
post.insert_one(new_post)
