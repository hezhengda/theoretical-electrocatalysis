# import the aiida profile
import aiida
aiida.load_profile()

# import
from aiida.orm import StructureData

from ase.io import write

# using hzdplugins
from hzdplugins.structure.build import bulkFromString, millerSurfaces, adsorptionSites, addAdsorbates

# create Pt bulk
Pt_bulk = bulkFromString('Pt', 'fcc', 3.98, True, [1, 1, 1])

# create Pt111 surface
Pt111_surf = millerSurfaces(Pt_bulk, [1, 1, 1], 4, 8, get_orthogonal=True)

Pt111_surf_aiida = StructureData(pymatgen_structure=Pt111_surf[0])

# find adsorption sites
adsSites = adsorptionSites(Pt111_surf_aiida)

# add adsorbates
slab_aiida = addAdsorbates(Pt111_surf_aiida, 
                           adsSiteDictionary={
                               'CO': [adsSites['ontop'][0]]
                           })

slab_ase = slab_aiida.get_ase()

write('Pt111-CO.cif', slab_ase, 'cif')