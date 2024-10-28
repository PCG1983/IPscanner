import os

def GetIPv4():
    reTry = True
    while reTry:
        reTry = False
        try:
            os.system("ipconfig > IPv4.txt")
            IPv4 = ''
            content = ''
            index = 0
            with open("IPv4.txt") as file:
                content = file.read()
                index = int(content.find("LAN adapter Wi-Fi"))
            content = content[index:]
            index = content.find("IPv4 Address. . . . . . . . . . . :")
            IPv4 = content[index+35:index+50].replace(' ', '').replace('\n', '')
            os.system("del IPv4.txt")
            return IPv4
        except Exception:
            reTry = True
if __name__=="__main__":
    print("IP: "+GetIPv4())