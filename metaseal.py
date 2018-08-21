
# ------------------------ IMPORTS ------------------------
try:
    import argparse
except ImportError:
    print("Error importing argparse")


try:
	import sys
except ImportError:
	print("Error importing 'sys' module")

# ------------------------ FILE ------------------------

if sys.argv > 2:
	extensions = sys.argv[:2]
else:
    try: #except error
        filex=open("extensions.txt", "r")  #open
    except FileNotFoundError:
        print("[¡] File extensions.txt does not exist")          
        exit()
    except IOError:
        print("[¡] 'IOError' Error opening FILE")
        exit()
              
    extensions = filex.readlines() #asign openned lines to dork list


# ------------------------ CATCHING USER INPUT ------------------------
filetypes = NULL 
if sys.arg > 2:
	filetypes = sys.arg[2:] # if user select some filetypes we will search for it
web = sys.arg[1]


parser = argparse.ArgumentParser()

parser.add_argument('--no-search', '-n', action='append', dest='avoid',
default=[],
help='MetaSeal will avoid this filetypes')

parser.add_argument('--add', '-a', action='append', dest='add',
default=[],
help='MetaSeal will add to search this filetypes')

results = parser.parse_args()

# ------------------------ FILETYPES TO SEARCH ------------------------

#user removed some files?
if results.avoid:
	for avoid_this in results.avoid:
        extensions.remove(avoid_this)

if results.add:
	for filetype_to_add in results.add:
		extensions.append(filetype_to_add)


#foreach extension
#------------------------ SEARCH FILES ------------------------

# ------------------------ DOWNLOAD FILES ------------------------

#------------------------ EXIFTOOL FILES ------------------------

