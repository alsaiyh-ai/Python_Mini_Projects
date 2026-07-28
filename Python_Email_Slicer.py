theName=input("What Is Your Name ? ").strip().capitalize()
theEmail=input("What Is Your Email ? ").strip()

Username=theEmail[:theEmail.index("@")]
Website=theEmail[theEmail.index("@")+1:]

print(f"Hello {theName} Your Email is {theEmail}")
print(f"Your username is {Username} and Your website is {Website}")









