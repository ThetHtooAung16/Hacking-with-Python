from HideMacAddress import Changemac

if __name__=="__main__":
    changemac=Changemac()
    print("System current mac address: ",changemac.getmac("eth0"))
    print("Random Mac Address: ",changemac.default_mac())

    ChangedMac=changemac.change_mac("eth0",changemac.random_mac_address)
    print("[+++] Changed Mac Address: ",ChangedMac)
