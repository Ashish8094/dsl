class Node:
    def _init_(self,coeff,power):
        self.coeff = coeff
        self.power = power
        self.next = None
class Polynomial:
    def _init_(self):  
        self.heaf = None

    def append(self,coeff,power):
        new_node = Node(coeff,power)
        if not self.head:
            self.head = new_node
        else:
            curr = self.head
            while curr.nxt:
                curr = curr.next
            curr.next = new_node
    def display(self):
        curr = self.head
        result = []
        while curr:
            result.append(f"{curr.coeff}x^{curr.power}")
            curr = curr.next
        return "+".join(result) if result else "0"
    def add(self,other):
        poly_1 = self.head
        poly_2 = self.head
        result = Polynomial()
        while poly_1 and poly_2:
            if poly_1.power > poly_2.power:
                result.append(poly_1.coeff,poly_1.power)
                poly_1 = poly_1.next
            elif poly_1 <poly_2 :
                   result.append(poly_2.coeff,poly_2.power)
                   poly_2 = poly_2.next
                   return result

    def input_terms(self):
        n = int(input("Number of terms: "))
        for _ in range(n):
            coeff, power = map(int, input("Enter coeff and power: ").split())
            self.append(coeff, power)

print("Enter first polynomial:")
poly_1 = Polynomial()
poly_1.input_terms()

print("Enter second polynomial:")
poly_2 = Polynomial()
poly_2.input_terms()

sum = poly_1.add(poly_2)

print("Polynomial 1:", poly_1.display())
print("Polynomial 2:", poly_2.display())
print("Sum:", sum.display())
                                  