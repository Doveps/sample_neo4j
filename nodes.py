from neo4jrestclient.client import GraphDatabase

db = GraphDatabase("http://localhost:7474", username="neo4j", password="doveps")

#create nodes
node = db.labels.create("Node");
n1 = db.nodes.create(name="categories")
node.add(n1)
n2 = db.nodes.create(name="customer")
node.add(n2)
n3 = db.nodes.create(name="employees")
node.add(n3)
n4 = db.nodes.create(name="orders")
node.add(n4)
n5 = db.nodes.create(name="products")
node.add(n5)
n6 = db.nodes.create(name="suppliers")
node.add(n6)

#create there relationships

n5.relationships.create("Has",n1)
n2.relationships.create("Purchased",n4)
n3.relationships.create("Sold",n4)
n4.relationships.create("Has",n5)
n6.relationships.create("Supplies",n5)




