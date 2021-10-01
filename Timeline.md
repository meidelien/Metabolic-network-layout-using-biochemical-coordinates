# Task 1 – Select best biochemical features

Task 1.1 – Compare features available in RDKit and OpenBabel (Oct 21)
Compare the number and type of features available in both tools. Decide if we can cover most cases with one of them or if it is best to use both in parallel. 

Task 1.2 – Compute all available features for E. coli core model (Oct 21)
Based on the selection above, try to compute all possible features for all the compounds in the E. coli core model. Create an overall table with compounds vs features.

Task 1.3 – Plot pairwise combinations of features (Nov 21)
Create scatter plots to layout the metabolites in a 2D space using pairwise combinations of features. Try to find combinations that result in a well-spread, clean, and intuitive layout. 

Task 1.4 – Apply PCA / PCoA (Nov/Dec 21)
It is possible that no single pairwise combination gives a good layout. Use dimensionality reduction methods such as Principal Component Analysis (PCA) or Principal Coordinate Analysis (PCoA) to condense all features into a more compact representation and plot the principal components. 

# Task 2 – Apply to genome-scale models

Task 2.1 – Select most relevant features (Jan 22)
Based on the previous task, select which features are most relevant to compute. The component loadings of PCA tell which features have the largest contribution to the principal components.

Task 2.2 – Compute at genome-scale (Jan 22)
Compute all the selected features for the most recent genome-scale metabolic model of E. coli (iML1515 model from the BiGG database).

Task 2.3 – Evaluate combinations for different pathways (Jan/Feb 22)
Try to plot all (hundreds) of compounds at once using the best layout previously selected. It is possible that this layout will not scale well at this level. Group compounds into pathways (nucleotides, amino acids, carbohydrates, lipids, etc), and try to find a layout that works well for each pathway, it is possible that this will be different for different pathways. 

Task 2.4 – Generate metabolic network layout (Feb 22)
Now that the biochemical coordinates of the compounds are defined, use the reaction information in the model to draw arrow connections between compounds and export the network diagram (either global or at pathway level) into a suitable format.

# Task 3 – Thesis Writing

Task 3.1 – First full draft (Mar/Apr)  try to have first draft by April 15th

Task 3.2 – Final thesis (Apr/May)  incorporate revisions and submit until deadline on May 15th 
