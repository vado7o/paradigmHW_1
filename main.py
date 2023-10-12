
numbers = [101, 3, 55, 67, 201, 5, 12, 73, 16, 100, 90, 32, 88]

def sort_list_imperative(numbers):
    change = True
    while (change):
        change = False
        for index in range(1, len(numbers)):
            if numbers[index] < numbers[index - 1]:
                numbers[index], numbers[index - 1] = numbers[index - 1], numbers[index]
                change = True
    return numbers

def sort_list_declarative(numbers):
    print(sorted(numbers))



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(sort_list_imperative(numbers))
    sort_list_declarative(numbers)

