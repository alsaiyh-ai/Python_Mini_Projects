admins=["Alsaiyh", "Ali", "Osama", "Raghad","Fatima", "Sameh", "Samera" ]
name=input("Please Type Your Name:-").capitalize().replace(" ","")
if name in admins:
    print(f"Hello {name}")
    option=input("Delete Or Update Your name ? ").capitalize().replace(" ","")
    if option=="Update":
        thenewname=input("Your Name Please:- ").capitalize().replace(" ","")
        admins[admins.index(name)]=thenewname
        print("Name Updated")
        print(admins)
    elif option=="Delete":
        admins.remove(name)
        print("Name Deleted")
        print(admins)
    else:
        print("Wrong option")
else:
    status=input("Not Admin, Add You Yes Or No? ").capitalize().replace(" ","")
    if status == "Yes":
        admins.append(name)
        print(admins)
    else:
        print("You Are Not Added.")




 








