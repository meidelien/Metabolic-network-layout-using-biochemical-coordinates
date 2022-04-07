# Metabolic network layout using biochemical coordinates
Norwegian University of Science and Technology, Trondheim 2022\
Department of Biotechnology and Food Science Services\
[Machado lab](https://www.ntnu.edu/ibt/research/computational-biology/#/view/about) 


Thesis supervisor: [Daniel Machado](https://github.com/cdanielmachado/)\
Co-Supervisor: [Elise Marquez](https://github.com/emarquezz/)

## Dependencies
- Tested with Python 3.7, 3.8, 3.9, 3.10
- [RDKit](https://www.rdkit.org/docs/Install.html)
  - ``` $ conda create -c conda-forge -n YOUR_ENV_NAME_HERE rdkit```




1. Unpack chem_prop.zip & chem_xref.zip in the data folder [Source](https://www.metanetx.org/mnxdoc/mnxref.html)
   1. The unpacked files (chem_prop.tsv & chem_xref.tsv) have been added to 
   .gitignore because they are too large for git w/o git LFS 
2. Ignore emoticons in notebooks



### References


- King ZA, Lu JS, Dräger A, Miller PC, Federowicz S, Lerman JA, Ebrahim A, Palsson BO, and Lewis NE. BiGG Models: A platform for integrating, standardizing, and sharing genome-scale models (2016) Nucleic Acids Research 44(D1):D515-D522. doi:10.1093/nar/gkv1049
- MetaNetX/MNXref: unified namespace for metabolites and biochemical reactions in the context of metabolic models
Sébastien Moretti, Van Du T Tran, Florence Mehl, Mark Ibberson, Marco Pagni

