cars = [
    {'number': 'AE235436', 'year': 2020},
    {'number': 'GTd4tegf', 'year': 2000},
    {'number': 'GNJ46546', 'year': 1980},
    {'number': 'HJKLJ686', 'year': 1990},
    {'number': 'GRF5673R', 'year': 2003},
    {'number': 'SSR325325', 'year': 1999}
]

a = []
for item in cars:
    if item['year'] >= 2000:
        a.append([item['number'], item['year']])

print(a)

new_list = [[i['number'], i['year']]for i in cars if i['year'] >= 2000]
print(new_list)
