Medgar_Evers = {"CS  241","CS  244","CS  246","CS  260","CS  260","CS  265", "CS  281","CS  312",
"CS  315","CS  325","CS  345","CS  350","CS  360",
"CS  395","MTH  151","MTH  202","MTH  203","MTH  204","MTH  237","PHY  212","PHYL  212","PHYW  212","PHY  213",
"PHYL  213","PHYW  213"   
}

no_spaces_list = [item.replace(" ", "") for item in Medgar_Evers]

# Convert the list with no spaces to a set
unique_classes_set = set(no_spaces_list)

print(unique_classes_set)

