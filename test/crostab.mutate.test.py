from foba.tabulars.crostabs import crostab_collection
from pyspare.deco.deco_crostab import deco_crostab

from crostab import Crostab

crostab = Crostab(**crostab_collection['AreaByCountry'])

print(deco_crostab(crostab))

crostab.mutate(lambda x: round(x))
crostab.mutate_head(lambda x: str(x).lower())
crostab.mutate_side(lambda x: str(x).lower())

print(deco_crostab(crostab))
