import requests

while True:
    report = input("أدخل البلاغ: ")

    # قم بتعديل الرابط إلى مستضيف بلاغ الخاص بك
    url = 'https://example.com/submit_report'

    # إرسال البلاغ إلى المستضيف
    response = requests.post(url, data={'report': report})

    # التحقق من نجاح الإرسال
    if response.status_code == 200:
        print("تم إرسال البلاغ بنجاح.")
    else:
        print("حدث خطأ أثناء إرسال البلاغ. يرجى المحاولة مرة أخرى.")
