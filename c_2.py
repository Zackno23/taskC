import csv
class Customer:
    def __init__(self, first_name, family_name, age):
        self.first_name = first_name
        self.family_name = family_name
        self.age = age

    def full_name(self):
        return f"{self.first_name} {self.family_name}"

    def age(self):
        return self.age

    def entry_fee(self):
        if self.age <= 3:
            return 0
        elif self.age < 20:
            return 1000
        elif self.age >= 75:
            return 500
        elif self.age >= 65:
            return 1200
        else:
            return 1500
    def info_csv(self):
        name = f"{self.first_name} {self.family_name}"
        return '|'.join([name, str(self.age), str(self.entry_fee())])




ken = Customer(first_name="Ken", family_name="Tanaka", age=75)
print(ken.info_csv() ) # 1000 という値を返す

tom = Customer(first_name="Tom", family_name="Ford", age= 57)
print(tom.info_csv()) # 1500 という値を返す

ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
print(ieyasu.info_csv()) # 1200 という値を返す