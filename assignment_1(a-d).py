class SET:
    def __init__(self, elements):
        self.set = set(elements)

    def ismember(self, element):
        return element in self.set

    def powerset(self):
        power_set = [[]]
        for i in self.set:
            for subset in power_set:
                power_set = power_set + [list(subset)+[i]]
        return power_set

    def subset(self, other):
        return self.set.issubset(other.set)
        
    def union(self, other):
        return list(self.set.union(other.set))

    def intersection(self, other):
        return list(self.set.intersection(other.set))


if __name__ == '__main__':
    elements = list(map(int, input('Enter elements of the set: ').split()))
    set1 = SET(elements)
    
    while True:
        print('Menu')
        print('1. ismember\n2. powerset\n3. subset\n4. union\n5. intersection\n0. exit')
        operation = int(input('Enter the operation number: '))

        if operation == 1:
            element = int(input('Enter element: '))
            print(set1.ismember(element))
        elif operation == 2:
            print(set1.powerset())
        elif operation == 3:
            elements = list(map(int, input('Enter elements of the other set: ').split()))
            set2 = SET(elements)
            print(set1.subset(set2))
        elif operation == 4:
            elements = list(map(int, input('Enter elements of the other set: ').split()))
            set2 = SET(elements)
            print(set1.union(set2))
        elif operation == 5:
            elements = list(map(int, input('Enter elements of the other set: ').split()))
            set2 = SET(elements)
            print(set1.intersection(set2))
        elif operation == 0:
            break
        else:
            print("Invalid Input")
