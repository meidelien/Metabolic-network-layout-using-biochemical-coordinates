import xml.etree.ElementTree 




tree = xml.etree.ElementTree.parse('C:\\Users\\meide\\Documents\\GitHub\\Master\\data\\e_coli_core.xml')
root = tree.getroot()
print (root.find("chemicalFormula").text)