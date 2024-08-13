# Inheritance, super()
class A():
    def __init__(self, a):
        self.a = a

class B():
    def __init__(self, b):
        self.b = b

class C_A(A):
    # this init will overwrite parent's init
    def __init__(self, ca):
        self.ca = ca

ca_i = C_A("this is ca")
print(ca_i.ca)
try:
    print(ca_i.a)
except Exception as exception:
    print(exception)
print()

class C_A_Super(A):
    # this init will still overwrite parent's init
    def __init__(self, caSuper):
    # but you can add super() to access parent's init
        super().__init__(caSuper)
        self.caSuper = caSuper

caSuper_i = C_A_Super("this is caSuper_i")
print(f"caSuper.caSuper: {caSuper_i.caSuper}")
print(f"caSuper.a: {caSuper_i.a}")
print()

# MRO
# more details are at "2_Additional_Resources.md"
# cannot create D > A > C_A
try:
    class D_ACA(A, C_A):
        pass
    print(D_ACA.mro())
except Exception as exception:
    print(f"Cherry_Tomato(Fruit, Tomato) will raise:\n{exception}")
    print()
# but D > C_A > A is OK
finally:
    class D_CAA(C_A ,A):
        pass
    print(D_CAA.mro())
    print()


# issubclass
print(f"C_A is A's subclass? {issubclass(C_A, A)}")
print(f"D_CAA is A's subclass? {issubclass(D_CAA, A)}")
print()

# isinstance
print(f"ca_i is C_A's instance? {isinstance(ca_i, C_A)}")
print(f"ca_i is A's instance? {isinstance(ca_i, A)}")
print()