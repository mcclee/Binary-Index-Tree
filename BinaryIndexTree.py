class BinaryIndexTree:
    def __init__(self, input):
        self.__bit = []
        self.__prefix = [0]
        for i in input:
            self.__prefix.append(i + self.__prefix[-1])
        for i in range(len(input)):
            r = (i + 1) & -(i + 1)
            self.__bit.append(self.__prefix[i + 1] - self.__prefix[i + 1 - r])
        self.__prefix = input

    def update(self, index, val):
        diff = val - self.__prefix[index]
        self.__prefix[index] = val
        index += 1
        while index < len(self.__bit) + 1:
            self.__bit[index - 1] += diff
            index += (index & -(index))
        

    def get_sum(self, start, end):
        return self.__sum_from(end) - self.__sum_from(start - 1)

    def __sum_from(self, index):
        s = 0
        index += 1
        while index:
            s += self.__bit[index - 1]
            index -= ((index) & -(index))
        return s

            

if __name__ == "__main__":
    b = BinaryIndexTree([1, 3, 5])
    print(b.get_sum(0, 2))
    b.update(1, 2)
    print(b.get_sum(0, 2))
