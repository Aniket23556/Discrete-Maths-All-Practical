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
    element_2 = list(map(int, input('Enter elements of the second set: ').split()))
    set2 = SET(element_2)

    print('1. Set1\n2. Set2')
    choice = int(input('Choose which set to perform operation on (1/2):'))

    if choice == 1:
        while True:
            print('Menu')
            print('1. Difference\n2. Symmetric_difference\n0. exit')
            operation = int(input('Enter the operation number: '))

            if operation == 1:
                print(set1.difference(set2))
            elif operation == 2:
                print(set1.symmetric_difference(set2))
            elif operation == 0:
                break
        
    elif choice == 2:
        while True:
            print('Menu')
            print('1. Difference\n2. Symmetric_difference\n0. exit')
            operation = int(input('Enter the operation number: '))

            if operation == 1:
                print(set2.difference(set1))
            elif operation == 2:
                print(set2.symmetric_difference(set1))
            elif operation == 0:
                break

    else:
        print('Invalid Choice')

