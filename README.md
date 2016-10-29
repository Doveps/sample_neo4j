#Sample Neo4j

This module works as an example for our project. Although it is written somehow in Sql form.
What it does is to tranlate Sql into Neo4j Query.

#How To Use

Load the data using the neo4j-shell command, which will allow you to paste
multiple command at once. These command use the LOAD CSV command in Cypher to load the files 
over HTTP from the Neo4j Github Repository


# Create customers
```sql
USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM "https://github.com/Doveps/sample_neo4j/blob/master/customers.csv" AS row
CREATE (:Customer {companyName: row.CompanyName, customerID: row.CustomerID, fax: row.Fax, phone: row.Phone});
```
# Create products
```sql
USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM "https://github.com/Doveps/sample_neo4j/blob/master/products.csv" AS row
CREATE (:Product {productName: row.ProductName, productID: row.ProductID, unitPrice: toFloat(row.UnitPrice)});
```
# Create suppliers
```sql
USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM "https://github.com/Doveps/sample_neo4j/blob/master/suppliers.csv" AS row
CREATE (:Supplier {companyName: row.CompanyName, supplierID: row.SupplierID});
```
# Create employees
```sql
USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM "https://github.com/Doveps/sample_neo4j/blob/master/employees.csv" AS row
CREATE (:Employee {employeeID:row.EmployeeID,  firstName: row.FirstName, lastName: row.LastName, title: row.Title});
```
# Create categories
```sql
USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM "https://github.com/Doveps/sample_neo4j/blob/master/categories.csv" AS row
CREATE (:Category {categoryID: row.CategoryID, categoryName: row.CategoryName, description: row.Description});
```
# Create orders
```sql
USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM "https://github.com/Doveps/sample_neo4j/blob/master/orders.csv" AS row
MERGE (order:Order {orderID: row.OrderID}) ON CREATE SET order.shipName =  row.ShipName;
```




# Create indexes
```sql
CREATE INDEX ON :Product(productID);
CREATE INDEX ON :Product(productName);
CREATE INDEX ON :Category(categoryID);
CREATE INDEX ON :Employee(employeeID);
CREATE INDEX ON :Supplier(supplierID);
CREATE INDEX ON :Customer(customerID);
CREATE INDEX ON :Customer(customerName);
```


# Create relationships
```sql
USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM "https://github.com/Doveps/sample_neo4j/blob/master/orders.csv" AS row
MATCH (order:Order {orderID: row.OrderID})
MATCH (customer:Customer {customerID: row.CustomerID})
MERGE (customer)-[:PURCHASED]->(order);
USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM "https://github.com/Doveps/sample_neo4j/blob/master/products.csv" AS row
MATCH (product:Product {productID: row.ProductID})
MATCH (supplier:Supplier {supplierID: row.SupplierID})
MERGE (supplier)-[:SUPPLIES]->(product);
USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM "https://github.com/Doveps/sample_neo4j/blob/master/orders.csv" AS row
MATCH (order:Order {orderID: row.OrderID})
MATCH (product:Product {productID: row.ProductID})
MERGE (order)-[pu:PRODUCT]->(product)
ON CREATE SET pu.unitPrice = toFloat(row.UnitPrice), pu.quantity = toFloat(row.Quantity);
USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM "https://github.com/Doveps/sample_neo4j/blob/master/orders.csv" AS row
MATCH (order:Order {orderID: row.OrderID})
MATCH (employee:Employee {employeeID: row.EmployeeID})
MERGE (employee)-[:SOLD]->(order);
USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM "https://github.com/Doveps/sample_neo4j/blob/master/products.csv" AS row
MATCH (product:Product {productID: row.ProductID})
MATCH (category:Category {categoryID: row.CategoryID})
MERGE (product)-[:PART_OF]->(category);
USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM "https://github.com/Doveps/sample_neo4j/blob/master/employees.csv" AS row
MATCH (employee:Employee {employeeID: row.EmployeeID})
MATCH (manager:Employee {employeeID: row.ReportsTo})
MERGE (employee)-[:REPORTS_TO]->(manager);
```




#Querying Data

Typically it is best to run these quiries in the Neo4j query browser.

The Sample query is found at Sample Query File
