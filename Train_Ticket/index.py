import time      #pip install time
ST = "1.SuperFast Train"
PT = "2.Passenger Train"
UT = "3.Unit Train"
R = "Rupess"
Cgl = "Chegapattu to Chennai Beach"
pwu = ["chengalpattu","CGL","Paranur", "PWU", "Singaperumal Koil", "SKL", "Maraimalai Nagar", "MMNK", "Kattangulattur", "CTM", "Potheri Halt", "POTI", "Guduvancheri", "GI"]
upm = ["Urappakkam", "UPM", "Vandalur", "VDR", "Perungulattur", "PRGL", "Tambaram", "TBM", "Tambaram Sanatorium", "TBMS", "Chromepet", "CMP", "Pallavaram", "PV", "Trisulam", "TLM", "Minambakkam", "MN", "Palavanthangal", "PZA", "St Thomas Mount", "STM", "Guindy", "GDY", "Saidapet", "SP", "Mambalam", "MBM", "Kodambakam", "MKK", "Nungambakkam", "NBK", "Chennai Chetpet", "MSC", "Chennai Egmore", "MS", "Chennai Park", "MPK", "Chennai Fort", "MSF", "Chennai Beach", "MSB"]
print(Cgl)
while (True):
    sq = str(input("Enter Your Destination:")).strip().upper()
    if (sq in upm or sq in pwu):
        print("Use Only Number Not Letters")
        print(ST)
        print(PT)
        print(UT)
        s = str(input("Choose Your Train Type:"))
        print("Your Destination is", sq)
        if s == "1" or ST==sq:
            print("your Ticket Price is:",120,R)
            c = input("Confrim or No:").strip().upper()
            if c == "YES" or "Confrim" or"s" or"S":
                print("Your Payment is Under Processing")
                time.sleep(1.0)
            elif c == "NO" or "NAN" or "nan":
                print("Please give us feedback on why you don't want to book")
                input("Enter Here:")
                break
            else:
                print("Check Your Spelling")
                continue
            print("Your Booked,SuperFast Train Ticket is Confrimed")
            break
        elif s == "2" or PT==sq:
            print("your Ticket Price is:",35,R)
            c = input("Confrim or No:").strip().upper()
            if c == "YES" or "Confrim" or"s" or"S":
                print("Your Payment is Under Processing")
                time.sleep(1.0)
            elif c == "NO" or "NAN" or "nan":
                print("Please give us feedback on why you don't want to book")
                input("Enter Here:")
                break
            else:
                print("Check Your Spelling")
                continue
            print("Your Booked,Passenger Train Ticket is Confrimed")
            break
        elif s == "3" or UT==sq:
            print("your Ticket Price is:",10,R)
            c = input("Confrim or No:").strip().upper()
            if c == "YES" or "Confrim" or"s" or"S":
                print("Your Payment is Under Processing")
                time.sleep(1.0)
            elif c == "NO" or "NAN" or "nan":
                print("Please give us feedback on why you don't want to book")
                input("Enter Here: ")
                break
            else:
                print("Check Your Spelling")
                continue
            print("Your Booked,Unit Train Ticket is Confrimed")
            break
        else:
            print("I Think Your Entered detials is wrong Check it And Try Again")
            continue
    elif(sq != upm or sq != upm):
        print("I Think Your Entered detials is wrong Check it And Try Again")
        print("Here Only Avalabile chengalpattu To Chennai Beach")

    else:
        pass
        
