from pyspare import deco, deco_matrix

from crostab import Table
from tests.assets import bistro_duty_roster

bistro_duty_roster['types'] = [1, 2, 3]
bistro_duty_roster['rule'] = '-------------'
print(bistro_duty_roster)

table = Table.from_dict(bistro_duty_roster)

print(deco(table))

print('height', table.height, 'width', table.width)
print(deco_matrix(table.rows))
print(deco_matrix(table.columns))
