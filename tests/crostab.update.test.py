from pyspare.deco import deco_object, deco_crostab
from veho import matrix

from crostab import Crostab

lex = {
    'side': ['foo', 'bar', 'zen'],
    'head': ['alpha', 'beta', 'gamma'],
    'rows': matrix.init(3, 3, lambda i, j: i * j)
}
crostab = Crostab(**lex)

print('raw', deco_crostab(crostab))

crostab.push_column('delta', [0, 3, 6])
crostab.push_row('ace', [0, 3, 6, 9])

print('pushed', '\n', deco_crostab(crostab))

print('popped column', deco_object(column := crostab.pop_column()))
print('popped row', deco_object(row := crostab.pop_row()))

print('popped', '\n', deco_crostab(crostab))

crostab.unshift_column('delta', [0, 3, 6])
crostab.unshift_row('ace', [0, 0, 3, 6])

print('unshifted', '\n', deco_crostab(crostab))

print('shifted column', deco_object(column := crostab.shift_column()))
print('shifted row', deco_object(row := crostab.shift_row()))

print('shifted', '\n', deco_crostab(crostab))
