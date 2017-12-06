from gmail import GMail, Message
from random import choice
import datetime

now = datetime.datetime.now()
hour = int(now.hour)

html_content = ['''<p style="text-align: center;">Cộng ho&agrave; X&atilde; hội Chủ nghĩa Việt Nam</p>
<p style="text-align: center;">Độc lập - Tự do - Hạnh ph&uacute;c</p>
<h1 style="text-align: center;"><strong>ĐƠN XIN NGHỈ HỌC</strong></h1>
<p>K&iacute;nh gửi: Thầy Nguyễn Quang Huy</p>
<p>Em t&ecirc;n l&agrave;: Chu Cao Qu&yacute;, học vi&ecirc;n lớp C4E14</p>
<p>{{REASON}} V&igrave; vậy, em xin ph&eacute;p thầy cho em nghỉ 1 h&ocirc;m. Em hứa sẽ xem lại video giảng của thầy v&agrave; l&agrave;m b&agrave;i tập đầy đủ</p>
<p style="text-align: right;">K&iacute; t&ecirc;n</p>
<p style="text-align: right;"><strong>Cao Qu&yacute;</strong></p>
<p style="text-align: right;">&nbsp;</p>
<p>&nbsp;</p>
''']

reason = ['''<p style="text-align: left;">H&ocirc;m nay em bị ốm.&nbsp;</p>
<p>&nbsp;</p>''', '''<p style="text-align: left;">H&ocirc;m qua em bị ninja l&agrave;ng lead chặn đầu n&ecirc;n đ&atilde; bị tai nạn v&agrave; bị gẫy ch&acirc;n.</p>
<p>&nbsp;</p>''', '''<p style="text-align: left;">H&ocirc;m qua em đi bar s&agrave;n, quẩy qu&aacute; nhiệt n&ecirc;n h&ocirc;m nay em đ&atilde; bị sập nguồn.</p>
<p>&nbsp;</p>''', '''<p style="text-align: left;">H&ocirc;m qua em đi ăn với bạn, lỡ ăn nhiều qu&aacute; n&ecirc;n s&aacute;ng nay em bị ti&ecirc;u chảy cấp, giờ em đang trong bệnh viện chuẩn bị mổ.</p>
<p>&nbsp;</p>
''']

send = False

while not send:
    if hour = 7:

        gmail = GMail('hohohohochiminh@gmail.com', 'quypr2000')
        msg = Message('XIN NGHI', to ='hohohohochiminh@gmail.com', html = html_content.replace("{{REASON}}", choice(reason)))
        gmail.send(msg)

        send = True
