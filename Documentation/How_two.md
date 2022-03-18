Necessary stuff for the repo

Data:
Chem_xref/chem_prop.zip (too large unzipped if not using git lfs) required for 

iML1515.xml (comprises BiGG Species & MNXM id's )

We need to use MNXM id's to get InChI keys from chem_prop.tsv and pop the BiGG species ID
into the final dataframe so we can get links between each metabolite from ReFramed

Notes: chem_xref does not have species BiGG IDs, only universal (missing the "M__" prefix) so we cannot use that as a point of reference without processing and also does not have InChI

Walkthrough:
Step 1: Compile MNXM & BiGG species ID from GEM(iML1515.xml) (notepad++ magic ?)
Step 2: Locate InChI's for each MNXM id from step 1 by locating each corresponding entry in the InChI column
Step 3: Compute chemical features using RDkit 


Step x: PCA (pca.ipynb) plotly & such

Step x: Get links between metabolites using ReFramed (Thanks Daniel)
so 