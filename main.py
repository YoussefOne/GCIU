s=0
t=1
def clear():
    import os
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
try:
    import requests
except:
    import os
    if os.name == "nt":
        os.system("pip install requests")
        clear()
    else:
        os.system("pip3 install requests")
        clear()
clear()
try:
    length_letters=int(input("how much is username letters you want (3,4,5 only ) :"))
except:
    clear()
    print("this is not a number")
    quit()
try:
    length_of_usernames=int(input("How much usernames you want :"))
except:
    clear()
    print("this is not a number")
    quit()
clear()
def logo():
    print("\033[31;1;40m"+"INSTAGRAM USERNAME "+str(length_letters)+" LETTERS GENERATOR & CHECKER :)"+"\033[37;1;40m")
logo()
choice = 1
import string
import random
letters_can_be_used = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' , '_' ,"1","2","3","4","5","6","7","8","9","0"]
x = True
used_usernames = []
usernames = []
while x:
    if s == length_of_usernames:
        x=False
        clear()
        g=0
        for i in usernames:
            g=g+1
            print("\033[31;1;40m"+str(g)+": "+"\033[32;1;40m"+i+"\033[37;1;40m")
        print(usernames)
        print(" \n")
        quit()
    else:
        None
    request_headers = {
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding":"gzip, deflate, br",
    "Accept-Language":"en-US,en;q=0.5",
    "Connection":"keep-alive",
    "Host":"www.instagram.com",
    "Upgrade-Insecure-Requests":"1",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0"
    }
    if choice == 1:
        used = False
        random_letter1 = random.choice(letters_can_be_used)
        random_letter2 = random.choice(letters_can_be_used)
        random_letter3 = random.choice(letters_can_be_used)
        random_letter4 = random.choice(letters_can_be_used)
        final_username = random_letter1 + random_letter2 + random_letter3 + random_letter4
        url = "https://www.instagram.com/"+final_username+"/"
        if final_username[:-1] == ".":
            used = True
        else:
            if final_username[0] == ".":
                used = True
            else:
                for i in used_usernames:
                    if i == final_username:
                        used = True
                        break
                    else:
                        used = False
        if length_letters == 4:
            random_letter1 = random.choice(letters_can_be_used)
            random_letter2 = random.choice(letters_can_be_used)
            random_letter3 = random.choice(letters_can_be_used)
            random_letter4 = random.choice(letters_can_be_used)
            final_username = random_letter1 + random_letter2 + random_letter3 + random_letter4
        elif length_letters == 5:
            random_letter1 = random.choice(letters_can_be_used)
            random_letter2 = random.choice(letters_can_be_used)
            random_letter3 = random.choice(letters_can_be_used)
            random_letter4 = random.choice(letters_can_be_used)
            random_letter5 = random.choice(letters_can_be_used)
            final_username = random_letter1 + random_letter2 + random_letter3 + random_letter4 + random_letter5
        elif length_letters == 3:
            random_letter1 = random.choice(letters_can_be_used)
            random_letter2 = random.choice(letters_can_be_used)
            random_letter3 = random.choice(letters_can_be_used)
            final_username = random_letter1 + random_letter2 + random_letter3
        else:
            clear()
            print("(3,4,5) letters only you can choose .")
            quit()
        if used :
            None
        else:
            used_usernames.append(final_username)
            response_status_code = requests.get( url , headers=request_headers ).status_code
            if response_status_code == 200:
                print("'"+final_username+"':\033[31;1;40m False \033[34;1;40m"+str(response_status_code)+"\033[37;1;40m \""+url+"\"\033[35;1;40m 2 "+"\033[37;1;40m ( "+str(t)+" )")
                t=t+1
            else:
                if s==0:
                    s=1
                else:
                    s=s+1
                x="'"+final_username+"':\033[32;1;40m True \033[34;1;40m"+str(response_status_code)+"\033[37;1;40m \""+url+"\"\033[35;1;40m 1 "+"\033[37;1;40m ( "+str(t)+" s:"+str(s)+" )"
                t=t+1
                print(x)
                usernames.append(final_username)
                from selenium import webdriver
        choice = 2
    elif choice == 2:
        request_headers = {
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Encoding":"gzip, deflate, br",
        "Accept-Language":"en-US,en;q=0.5",
        "Connection":"keep-alive",
        "Host":"www.instagram.com",
        "Upgrade-Insecure-Requests":"1",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
        }
        used = False
        if length_letters == 4:
            random_letter1 = random.choice(letters_can_be_used)
            random_letter2 = random.choice(letters_can_be_used)
            random_letter3 = random.choice(letters_can_be_used)
            random_letter4 = random.choice(letters_can_be_used)
            final_username = random_letter1 + random_letter2 + random_letter3 + random_letter4
        elif length_letters == 5:
            random_letter1 = random.choice(letters_can_be_used)
            random_letter2 = random.choice(letters_can_be_used)
            random_letter3 = random.choice(letters_can_be_used)
            random_letter4 = random.choice(letters_can_be_used)
            random_letter5 = random.choice(letters_can_be_used)
            final_username = random_letter1 + random_letter2 + random_letter3 + random_letter4 + random_letter5
        elif length_letters == 3:
            random_letter1 = random.choice(letters_can_be_used)
            random_letter2 = random.choice(letters_can_be_used)
            random_letter3 = random.choice(letters_can_be_used)
            final_username = random_letter1 + random_letter2 + random_letter3
        else:
            clear()
            print("(3,4,5) letters only you can choose .")
            quit()
        url = "https://www.instagram.com/"+final_username+"/"
        for i in used_usernames:
            if i == final_username:
                used = True
                break
            else:
                used = False
        if used :
            None
        else:
            used_usernames.append(final_username)
            response_status_code = requests.get( url , headers=request_headers ).status_code
            if response_status_code == 200:
                print("'"+final_username+"':\033[31;1;40m False \033[34;1;40m"+str(response_status_code)+"\033[37;1;40m \""+url+"\"\033[35;1;40m 2 "+"\033[37;1;40m ( "+str(t)+" )")
                t=t+1
            else:
                if s==0:
                    s=1
                else:
                    s=s+1
                x="'"+final_username+"':\033[32;1;40m True \033[34;1;40m"+str(response_status_code)+"\033[37;1;40m \""+url+"\"\033[35;1;40m 1 "+"\033[37;1;40m ( "+str(t)+" s:"+str(s)+" )"
                t=t+1
                print(x)
                usernames.append(final_username)
        choice = 1
ignore = input()