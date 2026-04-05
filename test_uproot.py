import uproot

# Open the ROOT file
try:
    file = uproot.open("data/HZZ12.root")
    # Tree is usually called "Events" or "Tree" or similar in open data files.
    # Lets see what keys are there
    print(f"File keys: {file.keys()}")
    
    # Lets get the first tree and print its branches
    tree_name = file.keys()[0]
    tree = file[tree_name]
    print(f"Tree keys: {tree.keys()}")
    
except Exception as e:
    print(f"Error: {e}")
