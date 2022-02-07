import subprocess
import re
import termcolor as color
import random

class Changemac:

    def __init__(self):
        self.current_mac=""
        self.user_input_mac=""
        self.random_mac_address=""

    def getmac(self,interface:"example eth0"):
        output=subprocess.run(["ifconfig",interface], shell=False, capture_output=True)
        result=output.stdout.decode()

        regex_pattern=r'ether\s[\da-z]{2}:[\da-z]{2}:[\da-z]{2}:[\da-z]{2}:[\da-z]{2}:[\da-z]{2}'
        regex=re.compile(regex_pattern)
        search_result=regex.search(result)

        if search_result:
            self.current_mac=search_result.group().split(" ")[1]
        else:
            print(color.colored("[xxx] REGEX Patter Error! \n Please check your pattern...",'red'))
        return self.current_mac

    def default_mac(self):
        defaultmac=["3e:54:91:88:c9:e3","2f:54:91:88:c9:e3","9d:54:91:88:c9:e3","1k:54:91:88:c9:e3","4z:54:91:88:c9:e3"]
        count=0
        for i in defaultmac:
            count=count+1
            print(color.colored("{0} [+++] {1}".format(count , i),'green'))

        choice=int(input(color.colored("Press 1 to use our random mac address. \n Press 2 to use your own mac address::",'blue')))
        if choice==2:
            self.user_input_mac=input("Type your own mac address: ")
        else:
            list_index=len(defaultmac)-1
            mac_list=random.randint(0,list_index)
            random_mac=defaultmac[mac_list]

            original_mac=self.getmac("eth0")
            if original_mac==random_mac:
                mac_list=mac_list+1
                if mac_list==len(defaultmac)-1:
                    mac_list=0
                    random_mac=defaultmac[mac_list]
                    self.random_mac_address=random_mac
            else:
                random_mac=defaultmac[mac_list]
                self.random_mac_address=random_mac
        return self.random_mac_address

    def change_mac(self,interface,newmac):

        output = subprocess.run(["ifconfig", interface , "down"], shell=False, capture_output=True)
        print(output.stdout.decode())

        output = subprocess.run(["ifconfig", interface ,"hw" , "ether" , newmac ], shell=False, capture_output=True)
        print(output.stdout.decode())

        output = subprocess.run(["ifconfig", interface , "up"], shell=False, capture_output=True)
        print(output.stdout.decode())

        return self.getmac(interface)
