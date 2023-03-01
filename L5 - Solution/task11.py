import re
from movies import movies

regex = r"(?:^|,\s?)(?=[^\"]?)\"?((?:[^\"]*|[^,\"]*))\"?(?=,\s?|$)"

all_movies = re.findall(regex, movies)

print('The default regular expresion is any symbol')
print('Enter `exit` to finish or `list` to see all movies')
while True:
    command = input('Enter a regular expression (or press ENTER to use the default`): ')

    if command == 'exit':
        break

    if command == 'list':
        print('\n'.join(all_movies))
        continue

    regex = command if command else '.*'

    r = re.compile(regex)
    found_movies = list(filter(r.match, all_movies))

    if found_movies:
        print(f'found {len(found_movies)} movie(s): {found_movies[0]}, ...')
    else:
        print('Not found any movie')

print('Exit...')