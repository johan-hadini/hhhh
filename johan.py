import requests
import logging
from pyfiglet import Figlet

# تكوين تسجيل
logging.basicConfig(filename='report_tool.log', level=logging.INFO)

# إعداد شعار باستخدام pyfiglet
f = Figlet(font='slant')
logo = f.renderText('البلاغ')
print(logo)

while True:
    report = input("أدخل البلاغ: ")

    url = 'https://www.whatsapp.com/contact/?subject=messenger'

    response = requests.post(url, data={'report': report})

    if response.status_code == 200:
        print("تم إرسال البلاغ بنجاح.")
        # سجل النجاح
        logging.info(f'تم إرسال البلاغ: {report}')
    else:
        print("حدث خطأ أثناء إرسال البلاغ. يرجى المحاولة مرة أخرى.")
        # سجل الخطأ
        logging.error(f'حدث خطأ أثناء إرسال البلاغ: {report}')
