class Node:
    def __init__(self, coeff, power):
        self.coeff = coeff
        self.power = power
        self.next = None

class Polynomial:
    def __init__(self):  
        self.head = None

    def append(self, coeff, power):
        if coeff == 0:
            return
        new_node = Node(coeff, power)
        if not self.head:
            self.head = new_node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node

    def display(self):
        curr = self.head
        result = []
        while curr:
            result.append(f"{curr.coeff}x^{curr.power}")
            curr = curr.next
        return " + ".join(result) if result else "0"

    def input_terms(self):
        n = int(input("Number of terms: "))
        for _ in range(n):
            coeff, power = map(int, input("Enter coeff and power: ").split())
            self.append(coeff, power)

    def multiply(self, other):
        result_terms = {}
        ptr1 = self.head
        while ptr1:
            ptr2 = other.head
            while ptr2:
                coeff = ptr1.coeff * ptr2.coeff
                power = ptr1.power + ptr2.power
                if power in result_terms:
                    result_terms[power] += coeff
                else:
                    result_terms[power] = coeff
                ptr2 = ptr2.next
            ptr1 = ptr1.next

        result = Polynomial()
        for power in sorted(result_terms.keys(), reverse=True):
            result.append(result_terms[power], power)
        return result

print("Enter first polynomial:")
polynomail_1 = Polynomial()
polynomail_1.input_terms()

print("Enter second polynomial:")
polynomail_2 = Polynomial()
polynomail_2.input_terms()

product = polynomail_1.multiply(polynomail_2)

print("\nPoly1:", polynomail_1.display())
print("Poly2:", polynomail_2.display())
print("Product:", product.display())
