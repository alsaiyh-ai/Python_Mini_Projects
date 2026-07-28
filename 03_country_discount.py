uName=input("Enter your Name :- ").replace(" ","").capitalize()
uCountry=input("Enter your Country :- ").replace(" ","").capitalize()
cName=input("Enter your Course :- ").replace(" ","")
cPrice=250
if uCountry in ["USA","Canada","Germany","France","Italy"]:
    print(f"Hello {uName} Because You Are From {uCountry}")
    print(f"The Course \"{cName}\" Price Is :\'${cPrice - 100}\' ")
else :
     print(f"Hello {uName} Because You Are From {uCountry}")
     print(f"The Course \"{cName}\" Price Is :$\'{cPrice - 80}\' ")









