class USA():
    def capital(self):
        print("Washington D.C")
    def language(self):
        print("English")
    def type(self):
        print("USA is a developed country")

class India():
    def capital(self):
        print("New Delhi")
    def language(self):
        print("Hindi")
    def type(self):
        print("India is a developing country")

I = India()
U = USA()

for i in (I,U):
    i.capital()
    i.language()
    i.type()
    