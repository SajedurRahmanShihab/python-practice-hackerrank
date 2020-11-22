'''https://www.hackerrank.com/challenges/python-lists/problem'''

myList = []

for i in range(int(input())):
    func = input().split()
    for i in range(1, len(func)):
        func[i] = int(func[i])

    if(func[0] == "insert"):
        myList.insert(func[1], func[2])
    elif(func[0] == "remove"):
        myList.remove(func[1])
    elif(func[0] == "append"):
        myList.append(func[1])
    elif(func[0] == "sort"):
        myList.sort()
    elif(func[0] == "pop"):
        myList.pop()
    elif(func[0] == "reverse"):
        myList.reverse()
    elif(func[0] == "print"):
        print(myList)
