import calendar


def first_func():
    print(calendar.weekheader(3))


def hidden_func():
    print(calendar.firstweekday())
    print()

    print(calendar.month(2021, 9))

    print(calendar.monthcalendar(2021, 9))

    print(calendar.calendar(2021))

    day_of_the_week = calendar.weekday(2021, 9, 8)

    # is_leap = calendar.isleap(2021)
    # print(is_leap)

    # how_many_leap_days = calendar.leapdays(2000, 2021)
    # print(how_many_leap_days)

    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    # print(digits[0:10:5])

    # for i in range(len(digits)):
    #    print(digits[0:i])

    window_size = 5
    for i in range(len(digits) - (window_size - 1)):
        print(digits[i:i + window_size])

    problems = 'broke, pale, short, nerdy'
    print(problems)

    g = problems.split(", ")

    print(g)

    joined = ' and '.join(g)
    print(joined)

    csv = ','.join(g)
    print(csv)

    t = (1, 2, 3)

    credit_card1 = (5321123412341234, 'Joe Rogan', '11/20', 123)
    credit_card2 = (5321123412341235, 'Jane Rogan', '11/20', 123)

    credit_cards = [credit_card1, credit_card2]

    print(credit_cards)

    person1 = ("Nancy Drew", 26, 'Lasagne')
    person2 = ("John Drew", 24, 'Pizza')

    people = [person1, person2]

    # (name, age, favfood) = person

    # print(name)
    # print(age)
    # print(favfood)

    for name, age, favfood in people:
        print(name)
        print(age)
        print(favfood)
        print()

    s = {'blueberry', 'raspberry'}

    s.add('strawberry')

    print(s)

    library_1 = {'Harry Potter', 'Hunger Games', 'Lord of the Rings'}
    library_2 = {'Harry Potter', 'Romeo and Juliet'}

    all_movies_in_town = library_1.union(library_2)
    print(all_movies_in_town)

    at_both_libraries = library_1.intersection(library_2)
    print(at_both_libraries)

    groceries = {'bananas': 5, 'oranges': 3}

    print(groceries.get('bananas'))
    print(groceries.get('apples'))

    contacts = {
        'Joe': ['123-4567', 'ea@website.com'],
        'Jane': ['987-6543', 'em@web.com']
    }

    print(contacts['Joe'])

    t = (1, 2, [1, 2, 3])
    print(t)

    t[2][0] = 7
    print(t)

    names = ['Jennifer', 'Susan', 'Jane', 'Sophie']

    l = []
    for person in names:
        l.append(person)
    print(l)

    print([person for person in names])

    l = []
    for person in names:
        l.append(person + ' dumped me.')
    print(l)

    print([person + ' dumped me.' for person in names])

    movies_and_ratings = {"Interstellar": 9, "Dark Knight": 8, "50 Shades": 3, "50 Shades Darker": 2,
                          "50 Shades Darkest": 1}

    l = []
    for movie in movies_and_ratings:
        if movies_and_ratings[movie] > 6:
            l.append(movie)
        print(l)

        print([movie for movie in movies_and_ratings if movies_and_ratings[movie] > 6])

    import re

    text = "random string. MyName123@website.com . some more randoom text. YourName888@company.net"

    pattern = re.compile("[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z]+")

    result = pattern.search(text)
    print(result)


def main():
    first_func()


if __name__ == "__main__":
    main()
