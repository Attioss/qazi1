import calendar as cal
import re

def dates():
    print(cal.weekheader(3))
    print(cal.firstweekday())
    print(cal.month(2021, 9))
    print(cal.monthcalendar(2021, 9))
    print(cal.calendar(2021))
    day_of_the_week = cal.weekday(2021, 9, 8)


def digits():

    one_digits = 1
    two_digits = "2"
    three_digits = 1.5
    four_digits = True

    template_string = "Randomszöveg"
    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    window_size = 5
    print(template_string[:3])

    dif = len(template_string) - len(digits)
    for i in range(len(template_string)):
        if digits[i] >= digits[len(digits)-1]:

            print(f"{i + 1}: {template_string[i]}, {digits[i]-dif}")



def data_types():

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


def loops():

    person1 = ("Nancy Drew", 26, 'Lasagne')
    person2 = ("John Drew", 24, 'Pizza')
    people = [person1, person2]
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


def add_string():
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


def movies():

    movies_and_ratings = {"Interstellar": 9, "Dark Knight": 8, "50 Shades": 3, "50 Shades Darker": 2,
                          "50 Shades Darkest": 1}

    l = []
    for movie in movies_and_ratings:
        if movies_and_ratings[movie] > 6:
            l.append(movie)
        print(l)
        print([movie for movie in movies_and_ratings if movies_and_ratings[movie] > 6])


def search_complex_data_types():

    text = "random string. MyName123@website.com . some more randoom text. YourName888@company.net"
    pattern = re.compile("[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z]+")
    result = pattern.search(text)
    print(result)


def main():
    digits()


if __name__ == "__main__":
    main()
