import urllib, re

def is_full_link(link, return_selected_text=False):
    """Returns if link is 'http://somewebsite.com/../someImage.png' style."""
    matches = re.search('https?\:\/\/[a-zA-Z0-9_\-\/\.\?\=]*?\.(?:png|jpg|jpeg|gif|bmp)', link)
    
    if matches != None && return_selected_text == False:
        return True
    elif matches != None && return_selected_text != False:
        return matches.group(1)
    else:
        return False
        
def is_root_relative_link(link, return_selected_text=False):
    matches = re.search('(?!\/\/)[a-zA-Z0-9_\-\/\.\?\=]*?\.(?:png|jpg|jpeg|gif|bmp)', link)
    
    if matches != None && return_selected_text == False:
        return True
    elif matches != None && return_selected_text != False:
        return matches.group(1)
    else:
        return False

def is_normal_relative_link(link, return_selected_text=False):
    matches = re.search('(?!\/\/|\/)[a-zA-Z0-9_\-\/\.\?\=]*?\.(?:png|jpg|jpeg|gif|bmp)', link)
    
    if matches != None && return_selected_text == False:
        return True
    elif matches != None && return_selected_text != False:
        return matches.group(1)
    else:
        return False
    

URL = "http://google.com"
my_page = urllib.urlopen(URL)

for line in my_page.readlines():
    # Matches http://blah.../some.png
    full_link_matches = re.search('https?\:\/\/[a-zA-Z0-9_\-\/\.\?\=]*?\.(?:png|jpg|jpeg|gif|bmp)', line)
    # Matches /blah.../some.png
    root_relative_link_matches = re.search('(?!\/\/)[a-zA-Z0-9_\-\/\.\?\=]*?\.(?:png|jpg|jpeg|gif|bmp)', line)
    # Matches blah.../some.png
    relative_link_matches = re.search('(?!\/\/|\/)[a-zA-Z0-9_\-\/\.\?\=]*?\.(?:png|jpg|jpeg|gif|bmp)', line)
    if full_link_matches != None:
        print full_link_matches.group(0)
    elif root_relative_link_matches != None:
        print root_relative_link_matches.group(0)
    elif relative_link_matches != None:
        print relative_link_matches.group(0)
            


