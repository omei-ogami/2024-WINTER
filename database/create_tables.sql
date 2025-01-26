-- Books
CREATE TABLE Books (
    Book_id INT PRIMARY KEY,
    Title TEXT,
    Description TEXT,
    Cover TEXT
    Category VARCHAR(255)
);

-- Authors
CREATE TABLE Authors (
    Author_id INT PRIMARY KEY,
    Name VARCHAR(255)
);

-- Book Authors (Mapping between books and authors)
CREATE TABLE Book_Authors (
    Id INTEGER PRIMARY KEY,  -- Auto-incremented ID
    Book_id INT,
    Author_id INT,
    FOREIGN KEY (Book_id) REFERENCES Books(Book_id),
    FOREIGN KEY (Author_id) REFERENCES Authors(Author_id)
);

-- Reviews
CREATE TABLE Reviews (
    Review_id INTEGER PRIMARY KEY,
    User_id VARCHAR(255),  -- Identifier for the user who left the review
    Book_id INT,
    Helpfulness FLOAT,
    Score INT CHECK (Score >= 0 AND Score <= 5),
    Time INT,
    Summary TEXT,
    Comment TEXT,
    FOREIGN KEY (Book_id) REFERENCES Books(Book_id)
);

-- Image-based Recommendations
CREATE TABLE Image_Recommendations (
    Id INTEGER PRIMARY KEY,
    Book_id INT,
    Recommendation_book_id INT,
    Ranking INT
);
