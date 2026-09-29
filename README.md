Open Library Books API

A simple Python project that retrieves book information from the public Open Library API, filters books published after the year 2000, sorts the results, and saves them as a CSV file.

Features

- Fetches 50 books from the Open Library Search API
- Filters books published after 2000
- Extracts useful book information
- Sorts the filtered results by publication year and title
- Exports the final data to a CSV file
- Handles API request errors
- Uses a simple and modular project structure

Project Structure

openlibrary-books-api/
│
├── src/
│   └── main.py
│
├── output/
│   └── books.csv
│
├── .gitignore
├── README.md
└── requirements.txt

Requirements

- Python 3.9 or newer
- Internet connection

Installation

Clone the repository:

git clone https://github.com/YOUR_USERNAME/openlibrary-books-api.git

Move into the project directory:

cd openlibrary-books-api

Create a virtual environment:

Windows

python -m venv .venv

Activate it:

.venv\Scripts\activate

Install the required package:

pip install -r requirements.txt

Usage

Run the script from the project root:

python src/main.py

The script will:

1. Request 50 books from the Open Library API.
2. Keep only books whose first publication year is greater than 2000.
3. Sort the results by publication year and title.
4. Save the results to:

output/books.csv

Output

The generated CSV file contains the following columns:

Column| Description
"title"| Book title
"authors"| Book author or authors
"publication_year"| First publication year
"openlibrary_key"| Open Library work identifier
"openlibrary_url"| Link to the book's Open Library page

Example

A generated CSV row looks like this:

title,authors,publication_year,openlibrary_key,openlibrary_url
Example Book,Example Author,2024,/works/OL123W,https://openlibrary.org/works/OL123W

The actual contents of "books.csv" depend on the data returned by Open Library when the script is executed.

API

This project uses the Open Library Search API:

https://openlibrary.org/search.json

The API provides book information including title, authors, first publication year, and Open Library identifiers.

Notes

The project intentionally uses a small number of dependencies. Python's standard library is used for CSV generation, file handling, and path management, while "requests" is used for HTTP communication with the Open Library API.

License

This project is created for educational purposes.