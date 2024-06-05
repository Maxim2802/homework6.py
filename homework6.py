# Практическое задание по теме: "Словари и множества"

# Словари
my_dict = {'Антон': 1996, 'Максим': 1754, 'Петя': 2012}
print(my_dict)
print(my_dict['Максим'])
print(my_dict.get('Мария'))
my_dict.update({'Ксюша': 1923,
                'Миша': 1829})
print(my_dict)
del my_dict['Ксюша']
print(my_dict['Миша'])
print(my_dict)

# Множества
my_set = {1, 2, 3, 6, 'Stamping', 28, 1, 2, 'Stamping', 2, 3, 6,}
print(my_set)
my_set.add((5, 77))
my_set.add(5)
my_set.add(77)
print(my_set)
my_set.discard(77)
print(my_set)
