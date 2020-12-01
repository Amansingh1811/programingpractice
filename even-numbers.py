class EvenNumbers:
    def even(self, start:int, end: int):
        print('Even numbers are: ')
        for item in range(start,end) :
            if item %2 ==0:
                print(item)


N = EvenNumbers()
N.even(10,20)