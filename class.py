class person:
    def _init  (self,name, age):
        self.age=age
        self.name=name
    
    def print_info(self):
        if self.name:
            print("name",self.name)
        if self.age:
            print("age",self.age)

person1= ("dayana")
person2= ("avin")

print(person1.name)
print(person2.name)