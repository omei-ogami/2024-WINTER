# Week 4: Implementing Relational Databases

## Objective
Implement a relational database to manage user and product interaction data, as well as write complex SQL queries. This week will focus on applying what you learned in Week 3 to build and optimize a working database.

## Tasks

These are the tasks you should complete in this week:

### 1. **Database Setup**
- Choose a relational database system (e.g., SQLite or PostgreSQL) and set up a database instance.
- Implement the **relational schema** you designed in Week 3:
  - Create the necessary tables (e.g., Users, Products, Reviews, Interactions).
  - Ensure proper relationships between the tables using **foreign keys**.

### 2. **Populating the Database**
- Import sample data (e.g., a subset of the Amazon Review Data or another available dataset).
- Populate the tables with data related to users, products, reviews, and interactions.

### 3. **Writing SQL Queries**
- Write complex SQL queries to:
  - Retrieve all reviews for a specific product.
  - Get the top-rated products.
  - Find all products reviewed by a specific user.
  - Calculate the average rating for each product.
  - Perform joins to retrieve combined data (e.g., user data along with their reviews).
  
### 4. **Database Optimization**
- Add **indexes** on frequently queried columns (e.g., product ID, user ID) to optimize the database.
- Ensure that the database is properly normalized (1NF, 2NF, 3NF) and avoid redundancy.

### 5. **Integration with the Recommendation System**
- Plan how to integrate the database with your recommendation system:
  - Store user-item interaction data (e.g., product views, ratings).
  - Prepare the database for efficient querying by the recommendation system.

## Bonus
Do these if time permits:
- Set up a **database backup** strategy.
- Explore **advanced SQL** features like window functions or triggers.
- Implement basic **user authentication** to track and store individual users’ interactions.

## Learning Goals
- Learn how to implement a relational database in a real-world context.
- Practice writing complex SQL queries to manipulate and retrieve data.
- Understand how to optimize a database for performance.
- Learn how to integrate the relational database with your recommendation system.

## Resources
- **Databases:**
  - PostgreSQL, SQLite (based on your preference).
- **Tools:**
  - SQL, Python (with SQLite or psycopg2 for PostgreSQL), pandas.
  - Database management tools: pgAdmin (PostgreSQL) or DB Browser (SQLite).
- **References:**
  - SQL tutorials on W3Schools, SQLZoo.
  - PostgreSQL or SQLite documentation.
  - Resources on SQL performance optimization and indexing.
