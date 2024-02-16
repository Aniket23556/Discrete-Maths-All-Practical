class SET:
    def __init__(self, elements):
        self.set = set(elements)

    def difference(self, other):
        return list(self.set.difference(other.set))

    def symmetric_difference(self, other):
        return list(self.set.symmetric_difference(other.set))

if __name__ == '__main__':
    elements = list(map(int, input('Enter elements of the set: ').split()))
    set1 = SET(elements)

    while True:
        print('Menu')
        print('1. Difference\n2. Symmetric_difference\n0. exit')
        operation = int(input('Enter the operation number: '))

        if operation == 1:
            elements = list(map(int, input('Enter elements of the other set: ').split()))
            set2 = SET(elements)
            print(set1.difference(set2))
        elif operation == 2:
            elements = list(map(int, input('Enter elements of the other set: ').split()))
            set2 = SET(elements)
            print(set1.symmetric_difference(set2))
        elif operation == 0:
            break
