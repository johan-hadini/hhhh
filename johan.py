# johan.py
import subprocess
from core import HackingTool

class ddos(HackingTool):
    TITLE = "ddos"
    DESCRIPTION = "Best DDoS Attack Script With 36 Plus Methods." \
                   "DDoS attacks\n\b " \
                   "for SECURITY TESTING PURPOSES ONLY! "
   
    INSTALL_COMMANDS = [
        "git clone https://github.com/the-deepnet/ddos.git",
        "cd ddos; sudo pip3 install -r requirements.txt"
    ]
    PROJECT_URL = "https://github.com/the-deepnet/ddos.git"

    def run(self):
        method = input("Enter Method >> ")
        url = input("Enter URL >> ")
        threads = input("Enter Threads >> ")
        proxylist = input(" Enter ProxyList >> ")
        multiple = input(" Enter Multiple >> ")
        timer = input(" Enter Timer >> ")

        # تعريف المتغير socks_type541 بقيمة مناسبة
        socks_type541 = "some_value"

        subprocess.run(["sudo", "python3", "ddos", method, url, socks_type541, threads, proxylist, multiple, timer])

# يمكنك أيضًا إضافة التشغيل الرئيسي هنا
if __name__ == "__main__":
    tool = ddos()
    tool.run()
