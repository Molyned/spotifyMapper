def func1():
    global a, locationData
    a = 9
    locationData = 'dog'
    return a, locationData

def func2(val1, val2):
    string = str(val1) + val2
    print(string)

def main():
    func1()
    func2(a, locationData)

if __name__ == '__main__':
    main()