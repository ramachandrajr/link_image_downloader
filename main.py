import urllib
import re
import os
import random
import sys


# ONE LINERS
# ====
is_full         = lambda link: re.compile(r'.*?(https?\:\/\/[a-zA-Z0-9_\-\/\.\?\=]*?\.(?:png|jpg|jpeg|gif|bmp)).*').findall(link)
is_root_based   = lambda link: re.compile(r'.*?((?!\/\/)[a-zA-Z0-9_\-\/\.\?\=]*?\.(?:png|jpg|jpeg|gif|bmp)).*').findall(link)
is_relative     = lambda link: re.compile(r'.*?((?!\/\/|\/)[a-zA-Z0-9_\-\/\.\?\=]*?\.(?:png|jpg|jpeg|gif|bmp)).*').findall(link)


# FUNCTIONS
# ====
def random_name(length):
    """Gets you a random filename."""
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_/"
    name = ""
    
    for i in range(length):
        name += chars[int(len(chars) * random.random())]
    return name


def get_extension(url):
    """Gets the extension from URL."""
    matches = re.match(r'.*?\.(png|jpeg|jpg|bmp|gif)', url)
    return matches.group(1)
    

def download_image(url, image_name=None):
    """Downloads an image."""
    DIR_NAME = os.getcwd()+"/rj_images"
    
    if not os.path.exists(DIR_NAME):
        os.makedirs(DIR_NAME)
        
    print "Downloading image from '%s'" % url,

    if image_name is None:
        image_name = random_name(10)
    else:
        pass

    try:        
        image_save_location = DIR_NAME+"/"+image_name+"."+get_extension(url)
        urllib.urlretrieve(url, image_save_location)
        print " | Downloaded!"
    except IOError as e:
        print "| Error: " + e.strerror + " !!"
        return None


def append_links(links, array):
    """List flattener"""
    for link in links:
        array.append(link)


def get_all_links(line, BASE_URL):
    """Gets all image links out of a line into an array."""
    links = []    

    # Matches http://blah.../some.png
    if len(is_full(line)) > 0:
        append_links(is_full(line), links)
        
    # Matches /blah.../some.png                
    if len(is_root_based(line)) > 0:
        temp_links = is_root_based(line)        
        for i in range(len(temp_links)):
            temp_links[i] = BASE_URL+temp_links[i]                
        append_links(temp_links, links)
        
    # Matches blah.../some.png        
    if len(is_relative(line)) > 0:
        temp_links = is_relative(line)        
        for i in range(len(temp_links)):
            temp_links[i] = BASE_URL+"/"+temp_links[i]                
        append_links(temp_links, links)        
        
    return links
    


# MAIN
# ===========

try:
    URL = sys.argv[1]
except IndexError:
    URL = raw_input("Give me a URL:")
    #URL = "http://google.com" 

my_page = urllib.urlopen(URL)
all_the_links_of_the_world = []

for line in my_page.readlines():
    links_for_this_line = get_all_links(line, URL)
    append_links(links_for_this_line, all_the_links_of_the_world)

for link in all_the_links_of_the_world:
    download_image(link)
