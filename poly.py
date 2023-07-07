class india:
    def capital(self):
        print ("Delhi is the capital")
    def language(self):
        print("Hind is spoken widely")

class USA:
    def capital(self):
        print("Washinton DC is the Capital")
    def language(self):
        print("Ebglish is widely spoken")
obj1 = india()
obj2 = USA()
for i in (obj1, obj2):
    i.capital()
    i.language()