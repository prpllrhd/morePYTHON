# Function defined outside the class
class C:
    def g(self):
        return 'hello world'
aa = C()
print aa.g()
