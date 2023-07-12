# One-to-many relationships represent the relationship between two entities where one entity is related to multiple instances of the other entity.In a database context, it means that one row in one table is related to multiple rows in another table.For example one customer may have multiple orders, but each order belongs to only one customer.
# Example one post many comments so comments is the many side of the relationship
# In SQLAlchemy, one-to-many relationships are defined using a Foreign Key on the many side of the relationship, which points to the primary key of the one side.In the example above the "order" table(many side of the relationship) would have a foreign key column that refers to the primary key of the "customer"(one customer can have many oders) table.

# important points
# - The many side of a one-to-many relationship is the side of the relationship that can have many rows.
# - The one side of a one-to-many relationship is the side of the relationship that can have only one row
# - The parent table is the table that has the many side
# - The child table is the table that has the one side
# - The primary key is a unique identifier for each row in a table.The primary key of the parent table is always found on the many side of the relationship
# - The foreign key is a field in the child table that references the primary key of the parent table.The foreign key of the child table is always found on the one side of the relationship
# - The difference in number of rows between the parent table and the child table can be greator than one. This is because each row in the child table can reference multiple rows in the parent table.
# Example
"""
Parent Table (Books)
  - ISBN (primary key)
  - Title
  - Author
  - Genre

Child Table (Authors)
  - Author ID (primary key)
  - Name
  - Date of Birth
  - Books (foreign key)

"""
# In this example the 'Books' table is the parent table and the 'Authors' table is the child table
