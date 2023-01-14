
def recursive_pascal(array, lines):
    # start with array of just 1 and lines = 10
    if lines == 1:
        print(array)
        return array
    else:
        print(array)
        lines = lines - 1
        new_array = [array[0]]
        for i in range(0, len(array) - 1):
            new_array.append(array[i] + array[i + 1])
        new_array.append(array[len(array) - 1])
        return recursive_pascal(new_array, lines)



if __name__ == '__main__':
    recursive_pascal([1], 10)


