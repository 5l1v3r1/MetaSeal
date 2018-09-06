# ------------------------ IMPORTS ------------------------

try:
    import argparse
except ImportError:
    print("Error importing argparse")
    exit()
try:
	import sys
except ImportError:
	print("Error importing 'sys' module")
    exit()
try:
    from google import google
except ImportError:
    print("Error importing google module, try: pip install Google-Search-API")
    exit()

try:
    import urllib.request
except ImportError:
    print("Error importing 'urllib.request' module")
    exit()
try:
    from os.path import basename
except ImportError
    print("Error 'importing basename', from 'os.path'")
    exit()

# ------------------------ FILE ------------------------

if sys.argv > 2:
	extensions = sys.argv[:2] # if suer selected fyletypes we select it
else: # if not, we use default extensions
    try:
        filex=open("extensions.txt", "r")  #open
    except FileNotFoundError:
        print("[¡] File extensions.txt does not exist")          
        exit()
    except IOError:
        print("[¡] 'IOError' Error opening FILE")
        exit()
              
    extensions = filex.readlines() #asign openned lines to dork list


# ------------------------ CATCHING USER INPUT ------------------------

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


for extension in extensions:

#------------------------ SEARCH FILES ------------------------

    files_2_download = input("searching {}, how many files do you want to download?: ".format(extension[i]))
    query = "site:" + web + " filetype:" + extension[i]
    google_search = google.search(query, 1)
    while google_search > len(files_2_download):
        google_search.pop()
# ------------------------ DOWNLOAD FILES ------------------------

    for link in google_search:
        filename = basename(link)
        filename = "files/" + filename
        print("Downloading {}".format(filename))
        urllib.request.urlretrieve(link, filename) 
        

#------------------------ EXIFTOOL FILES ------------------------


