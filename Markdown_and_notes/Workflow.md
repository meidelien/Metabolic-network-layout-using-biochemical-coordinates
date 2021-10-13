# Workflow

### Data gathering and metabolite feature computation
1. Extract inchi_key  field from e_coli_core.json/xml (backup is using n++)
2. Search through metacyc with inchi_key (pref automated but can be done manually, only 72)
3. Append descriptors and SMILE to e_ecoli_core_descriptors.xml for the respective metabolites
4. Parse Smile from e_coli_core_descriptors.xml into rdkit & reframed and append feature computation

## TODO scripts that does this

