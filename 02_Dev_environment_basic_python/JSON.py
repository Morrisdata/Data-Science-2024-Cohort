# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 07:52:14 2020

@author: Msmorris
"""

# What is JSON
'''
1) stands for Java Script Object Notation

2) light-wieght data interchange format.  
   (light-weight: small memory footprint, easy to impliment minimual syntax and features)

3) JSON is extremely import when working with restful APIs and sending data 
   back and forth it has replaced xml in that area. 

    API Application Program Interface: API stands for Application Programming Interface. 
    An API is a software intermediary that allows two applications to talk to each other. 
    In other words, an API is the messenger that delivers your request to the provider 
    that you're requesting it from and then delivers the response back to you.

    API A RESTful API (API) that uses HTTP requests to GET, PUT, POST and DELETE data.

4) Based on a subset of JavaScript

5) Often used with AJAX Asynchronus Javascript And Xml
   used to send data back and forth from client and server without having to refresh 
   the page in the browser.  you can make an AJAX request to a json to a JSON file
   and output results to a browser. 
6) Inspired by Javascript but independent of any 1 language
'''   
# DATA types
'''
 1) Number: No difference between integer and floats
 2) String: String of Unicode characters. Use double quotes
 3) Boolean: True or False
 4) Array: Ordered list of 0 or more values
 5) Object: Unordered collection of key/value pairs 
 6) Null: Empty Value
'''
# JSON Syntax Rules
'''
 1) Uses key/value pairs - {"name":"Brad"} 
 2) Uses double quotes around KEY and VALUE
 3) Must use the specified data types
 4) You can make file types of json they must be valid with ext. json
 5) MIME type is "application/json" 
    MIME - Multipurpose Internet Mail Extensions basically media types

# JSON             PYTHON
# Object           dict    
# array            list
# string           str
# number(int)      int
# number(real)     float
# true             True
# false            False
# null             None

'''    



# JSON Example
import json

''' People_string has a key of people and arrays as values. the arrays have a 
key of name, phone, emails has_license'''

people_string = ''' 
{
    "people":[
    {
     "name":"Mike Meyers",
     "phone":"550-555-5555",
     "emails": ["firstemail@email.com", "secondemail@email.com"],
     "has_license": false
     },
     {"name": "Jane Doe",
      "phone": "560-555-5555",
      "emails": null,
      "has_license": true
      }
     ]
}
'''
# load the above into a an object
data = json.loads(people_string)

print(data)
print(type(data))
print(type(data['people']))

#  put a json string into a python object  
for person in data['people']:
    print(person['name'])
    
# put a python object inot a json string
''' scenario remove phone number and add back to json
'''
for person in data['people']:
    del person['phone']

new_string = json.dumps(data)
print(new_string)

# to indent use indent and number you want to indent
new_string = json.dumps(data, indent = 2)
print(new_string)

# sort the keys
new_string = json.dumps(data, indent = 2, sort_keys=True)
print(new_string)

#load json files into python objects rite them back to json files
https://www.youtube.com/watch?v=9N6a-VLBa2I
import json
with open('states') as f:
    data = json.load(f) # load as a python object
for state in data['states']:
    print(state) # access the python object
for state in data['states']:
    print(state['name'], state['abbreviation'])
    
# now write the python object out to a json file
with open('new_states.json', 'w') as f:
    json.dump(data, f) # jsondump(what you want to dump, where to dump to)
# make it easier to read
with open('new_states.json', 'w') as f:
    json.dump(data, f, indent=2)

#real world example
'''
it is common for websites to work with json files because they
are easy to parse.
Grabbing json data from a public API and how to parse the data
Here is an api that converts US dollars into other currency
'''
Alter this code to musicbrainz




import json
from urllib.request import urlopen

with urlopen("https://prime.exchangerate-api.com/v5/f15c930592e5f577cee2311f/latest/USD") as response:
    source = response.read()
# load into a python object using a json module
data = json.loads(source)
# pass it into a string with indent
print(json.dumps(data,  indent = 2))

# count how many records
print(len(data['conversion_rates']))

# loop through items
for item in data['conversion_rates']:
    print(item)
###############################################################################
## NEED MORE BUILD A BRIDGE TO NEXT UNIT
##############################################################################
    
    
    
    
    
#MusicBrainz
# documentation review https://musicbrainz.org/doc/Development/JSON_Web_Service
'''
{
    "id": "5b11f4ce-a62d-471e-81fc-a69a8278c7da",
    "name": "Nirvana",
    "sort-name": "Nirvana"
    "type": "Group",
    "country": "US",
    "disambiguation": "90s US grunge band",
    "life-span": {
        "ended": true,
        "begin": "1988-02",
        "end": "1994-04-05"
    },
    "aliases": [ { "name": "Nirvana US", "sort-name": "Nirvana US" } ]]
}
'''
# Query to bring back a result set

"""
Take a look at the main() function for an example of how to use the code. What 
is each function doing?
"""
import json
import requests
import pprint


BASE_URL = "http://musicbrainz.org/ws/2/"
ARTIST_URL = BASE_URL + "artist/"


# query parameters are given to the requests.get function as a dictionary; this
# variable contains some starter parameters.
query_type = {  "simple": {},
                "atr": {"inc": "aliases+tags+ratings"},
                "aliases": {"inc": "aliases"},
                "releases": {"inc": "releases"}}


def query_site(url, params, uid="", fmt="json"):
    """
    This is the main function for making queries to the musicbrainz API. The
    query should return a json document.
    """
    params["fmt"] = fmt
    r = requests.get(url + uid, params=params)
    print("requesting", r.url)

    if r.status_code == requests.codes.ok:
        return r.json()
    else:
        r.raise_for_status()


def query_by_name(url, params, name):
    """
    This adds an artist name to the query parameters before making an API call
    to the function above.
    """
    params["query"] = "artist:" + name
    return query_site(url, params)


def pretty_print(data, indent=4):
    """
    After we get our output, we can use this function to format it to be more
    readable.
    """
    if type(data) == dict:
        print(json.dumps(data, indent=indent, sort_keys=True))
    else:
        print(data)


def main():
    """
    Below is an example investigation to help you get started in your
    exploration. Modify the function calls and indexing below to answer the
    questions on the next quiz.

    HINT: Note how the output we get from the site is a multi-level JSON
    document, so try making print statements to step through the structure one
    level at a time or copy the output to a separate output file. Experimenting
    and iteration will be key to understand the structure of the data!
    """

    # Query for information in the database about bands named Nirvana
    results = query_by_name(ARTIST_URL, query_type["simple"], "Nirvana")
    pretty_print(results)

    # Isolate information from the 4th band returned (index 3)
    print("\nARTIST:")
    pretty_print(results["artists"][3])

    # Query for releases from that band using the artist_id
    artist_id = results["artists"][3]["id"]
    artist_data = query_site(ARTIST_URL, query_type["releases"], artist_id)
    releases = artist_data["releases"]

    # Print information about releases from the selected band
    print("\nONE RELEASE:")
    pretty_print(releases[0], indent=2)

    release_titles = [r["title"] for r in releases]
    print("\nALL TITLES:")
    for t in release_titles:
        print(t)

if __name__ == '__main__':
    main()