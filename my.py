class Wallet:
    def __init__(self, owner, balance = 0, valuta = "GRN"):
        self.owner = owner
        self.balance = balance
        self.valuta = valuta

    def add_money(self, amount):
        self.balance += amount
        print(self.balance)


    def spend_money(self, amount):
        if self.balance >= amount:
           self.balance -= amount
        print(self.balance)

    def convert(self, newValuta, kurs):
        self.valuta == newValuta
        self.balance = self.balance * kurs
        print(f"owner = {self.owner}\n balance = {self.balance}\n valuta {self.valuta}")

b = Wallet("Ivan",100, "GRN")
b.add_money(100)
print(b.add_money)
b.spend_money(50)
print(b.spend_money)
b.convert("grn", 50)