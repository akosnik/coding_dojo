x = [[5, 2, 3], [10, 8, 9]]


students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]
sports_directory = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer': ['Messi', 'Ronaldo', 'Rooney']
}
z = [{'x': 10, 'y': 20}]

# 1.1
x[1][0] = 15
# 1.2
students[0]["last_name"] = "Jordaner"
# 1.3
sports_directory['soccer'][0] = 'Aaaagh'
# 1.4
z[0]['y'] = 30

# 2 ---------------------------------------------------------------

students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]


def iterateDictionary(myList):
    for i in myList:
        myStr = ''
        for key, val in i.items():
            myStr += (f"{key} - {val}")
            if (key != list(i)[-1]):
                myStr += (", ")
        print(myStr)


iterateDictionary(students)


# 3 ---------------------------------------------------------------


def iterateDictionary2(myKey, myList):
    for i in myList:
        print(i[myKey])


# iterateDictionary2("first_name", students)

# 4 ---------------------------------------------------------------

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}


def printInfo(myDict):
    for key, val in myDict.items():
        print(f"{len(val)} {key.upper()}")
        for i in val:
            print(i)
        print(' ')


# printInfo(dojo)
