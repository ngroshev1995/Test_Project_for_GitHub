from pprint import pprint

data = [
    {'from': 'B', 'to': 'E'},
    {'from': 'A', 'to': 'C'},
    {'from': 'F', 'to': 'B'},
    {'from': 'D', 'to': 'A'},
    {'from': 'C', 'to': 'F'},
]

_from, _to = [], []
for i in data:
    _from.append(i['from'])
    _to.append(i['to'])

[start] = [i for i in _from if i not in _to]

new_data = []
cursor = ''

while len(new_data) != len(data):
    for elem in data:
        if len(new_data) == 0 and elem.get('from') == start:
            new_data.append(elem)
            cursor = elem['to']
        else:
            if elem.get('from') == cursor:
                new_data.append(elem)
                cursor = elem['to']

pprint(new_data, indent=4)