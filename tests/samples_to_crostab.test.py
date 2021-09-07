import palett.cards as cards
from pyspare import deco
from pyspare.deco.deco_crostab import deco_crostab

from crostab.convert import samples_to_crostab


def module_to_dict(module): return {k: getattr(module, k) for k in dir(module) if not k.startswith('_')}


card_collection = module_to_dict(cards)

print(deco(card_collection))

crostab = samples_to_crostab(
    card_collection,
    ['amber', 'indigo', 'yellow'],
    ['base', 'lighten_1', 'darken_1']
)

print(deco_crostab(crostab))
