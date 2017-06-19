import rdflib
from rdflib import Graph, Literal, BNode, RDF
from rdflib.namespace import FOAF, DC


g=rdflib.Graph()
g.load("/Users/andre/Downloads/peel.rdf")
cont = 0

##############
#### PERSON
####
for person in g.subjects(RDF.type, FOAF["Person"]):
    cont = cont + 1
    print cont, person

##############
#### MUSICAL ARTIST
####
# for musicArtist in g.subjects(RDF.type, FOAF["MusicArtist"]):
#     cont = cont + 1
#     print cont, musicArtist, FOAF.name

# for s,p,o in g:
#     print s,p,o
    

# with open("/Users/andre/Downloads/peel.rdf") as f:
#     content = f.readlines()
# content = [x.strip() for x in content] 
# print len(content)