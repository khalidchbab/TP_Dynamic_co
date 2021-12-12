from pyld import jsonld
import json


output = open('output.json',)
data = json.load(output)

context_f = open('context2.json',)
context = json.load(context_f)

# compacted = jsonld.compact(data, context)

rdf = jsonld.to_rdf(data, {
    'expandContext': context,  # contexte à appliquer
    'format': 'application/n-quads', # format de sortie
})

f = open("traceGit.nq", "w+")
f.write(rdf)

print("Done")



