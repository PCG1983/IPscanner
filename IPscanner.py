import os
from rich import print
from IPcatcher import GetIPv4
import time
from sys import exit
from datetime import date

os.system('cls')
p = print
def print(s: str, end=''):
    if __name__ == '__main__': p(s,end=end)
def sleep(s: float | int):
    if __name__ == '__main__': time.sleep(s)
print("[bold red]   _____    ___                                             ")
print("[bold red]   \\_   \\  / _ \\ [bold green]___   ___   __ _  _ __   _ __    ___  _ __ ")
print("[bold red]    / /\\/ / /_)/[bold green]/ __| / __| / _` || '_ \\ | '_ \\  / _ \\| '__|")
print("[bold red] /\\/ /_  / ___/[bold green] \\__ \\| (__ | (_| || | | || | | ||  __/| |   ")
print("[bold red] \\____/  \/[bold green]     |___/ \\___| \\__,_||_| |_||_| |_| \\___||_|   \n")

res = GetIPv4()
global force
force = False
if (res == "127.0.0.1") or not ('192' in res):
    print("[yellow bold][[red bold]![/]] You're not connected to an external network !")
    sleep(3)
    exit()
else:
    def InternalScan():
        Ups = []
        print("[bold blue][[green bold]*[/]] Scanning for the up-hosts[/][yellow](This won't include the hosts which don't reply pings)[/]\n[green] - Press Ctrl+C to cancel the scan.[/]")
        try:
            for i in range(0,256):
                for j in range(0,256):
            
                    IPv4 = "192.168.{0}.{1}".format(str(i),str(j))
                    os.system("ping {} -n 1 -w 1.5 > temp.txt".format(IPv4))
                    pong = False
            
                    with open("temp.txt") as temp:
                        content = temp.read()
                        if "Lost = 0" in content:
                            pong = True
                    os.system("del temp.txt")
                    if pong:
                        Ups.append(IPv4)
                        print("\rPinging [green bold]"+IPv4+"[/] [yellow]|[/] Host is [green bold]UP![/]", end="   \r")
                    else:
                        print("\rPinging [red bold]"+IPv4+"[/] [yellow]|[/] Host is [red bold]DOWN![/]", end="   \r")
                    if j == 255:
                        break
                if i == 255:
                    break
        except KeyboardInterrupt:
            force = True
            os.remove("temp.txt")
        os.system("cls")
        if not force:
            for i in range(0,3):
                print("[green bold]Scan has been finished![/]")
                sleep(.5)
                print(' '*23)
                sleep(.5)
        else:
            print("[yellow bold]Scan interrupted![/]")
            sleep(2.5)
        os.system("cls")
        if len(Ups) == 0:
            print("[[red bold]![/]] No host is up!\nYou're alone in the network.")
        else:
            print("[cyan bold]These {} hosts were up:\n----------".format("[green bold]"+str(len(Ups))+"[/]"))
            num = 0
            file = open("up-Hosts on {}.txt".format(date.today()), '+x')
            if __name__=="__main__":
                for host in Ups:
                    num += 1
                    print(str(num)+'. '+host)
                    file.write(str(num)+'. '+host+'\n')
                file.close()
            else:
                return Ups

    InternalScan()
    os.system("PAUSE")