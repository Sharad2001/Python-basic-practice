class Dad:
    basketball = 1

class Son(Dad):
    dance = 1
    def isdance(self):
        return f"Yes i dance {self.dance}" \
               f"number of times."

class Grandson(Son):
    dance = 6
    def isdance(self):
        return f"Jackson yeah! Yes I dance" \
               f" {self.dance} no. of times"

darry = Dad()
larry = Son()
harry = Grandson()

print(harry.isdance())