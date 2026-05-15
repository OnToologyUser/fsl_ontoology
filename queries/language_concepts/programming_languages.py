from pathlib import Path
from rdflib import Graph

# Parse all Turtle files of the ontology
ttl_dir = Path("../../ontologies")
ttl_files = sorted(ttl_dir.glob("*.ttl"))
g = Graph()
for ttl in ttl_files:
    g.parse(ttl, format="turtle")

# Query of interest
query = """
PREFIX rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX tbox: <http://www.softlang.org/ontologies/tbox#>
PREFIX pe: <http://www.softlang.org/ontologies/pe#>

SELECT DISTINCT ?l
WHERE {

  # An assertiom between programming language and concept
  {
    ?c ?p ?l
  }
  UNION
  {
    ?l ?p ?c
  }

  # An actual programming language
  {
    SELECT DISTINCT ?l 
    WHERE {
      ?lsc rdfs:subClassOf* pe:ProgrammingLanguage .
      ?l rdf:type ?lsc .
    }
  }

  # A concept entity
  { 
    SELECT DISTINCT ?c
    WHERE {
      {
        ?csc rdfs:subClassOf+ tbox:LanguageConcept .
        ?c rdf:type ?csc .
      }
      UNION
      {
        ?c rdfs:subClassOf+ tbox:LanguageConcept .
      }
    }
  }

  # Counting only ontological properties
  FILTER(?p != rdf:type) 
  FILTER(?p != rdfs:subClassOf)
  FILTER(?p != rdfs:domain)
  FILTER(?p != rdfs:range)
  FILTER(?p != rdfs:label)
  FILTER(?p != rdfs:comment)
  FILTER(?p != foaf:isPrimaryTopicOf)
  FILTER(?p != foaf:page)
}
ORDER BY ?l
"""

# Reporting query result
for row in g.query(query):
    print(row['l'])
