import csv
from pathlib import Path

import requests


API_URL = "https://openlibrary.org/search.json"
BOOK_COUNT = 50
PUBLICATION_YEAR = 2000
REQUEST_TIMEOUT = 30

BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUT_FILE = BASE_DIR / "output" / "books.csv"


def fetch_books(count: int = BOOK_COUNT) -> list[dict]:
    """Fetch books from the Open Library Search API."""
    params = {
        "q": "book",
        "limit": count,
        "fields": "key,title,author_name,first_publish_year",
    }

    response = requests.get(
        API_URL,
        params=params,
        timeout=REQUEST_TIMEOUT,
    )
    response.raise_for_status()

    data = response.json()
    return data.get("docs", [])


def filter_books_by_year(books: list[dict], year: int) -> list[dict]:
    """Keep only books published after the given year."""
    filtered_books = []

    for book in books:
        publish_year = book.get("first_publish_year")

        if isinstance(publish_year, int) and publish_year > year:
            filtered_books.append(book)

    return filtered_books


def prepare_books(books: list[dict]) -> list[dict]:
    """Prepare book data for CSV export."""
    prepared_books = []

    for book in books:
        title = book.get("title", "Unknown Title")
        authors = ", ".join(book.get("author_name", []))
        publish_year = book.get("first_publish_year")
        key = book.get("key", "")

        prepared_books.append(
            {
                "title": title,
                "authors": authors or "Unknown Author",
                "publication_year": publish_year,
                "openlibrary_key": key,
                "openlibrary_url": (
                    f"https://openlibrary.org{key}" if key else ""
                ),
            }
        )

    return prepared_books


def sort_books(books: list[dict]) -> list[dict]:
    """Sort books by publication year and then by title."""
    return sorted(
        books,
        key=lambda book: (
            -book["publication_year"],
            book["title"].lower(),
        ),
    )


def save_to_csv(books: list[dict], output_file: Path) -> None:
    """Save book data to a CSV file."""
    output_file.parent.mkdir(parents=True, exist_ok=True)

    fieldnames = [
        "title",
        "authors",
        "publication_year",
        "openlibrary_key",
        "openlibrary_url",
    ]

    with output_file.open(
        mode="w",
        encoding="utf-8-sig",
        newline="",
    ) as csv_file:
        writer = csv.DictWriter(
            csv_file,
            fieldnames=fieldnames,
        )
        writer.writeheader()
        writer.writerows(books)


def main() -> None:
    """Run the complete data collection and export process."""
    print("Fetching books from Open Library...")

    try:
        books = fetch_books()
    except requests.RequestException as error:
        print(f"Failed to fetch data from Open Library: {error}")
        return

    print(f"Fetched books: {len(books)}")

    filtered_books = filter_books_by_year(
        books,
        PUBLICATION_YEAR,
    )

    prepared_books = prepare_books(filtered_books)
    sorted_books = sort_books(prepared_books)

    save_to_csv(sorted_books, OUTPUT_FILE)

    print(f"Books after filtering: {len(sorted_books)}")
    print(f"CSV file saved to: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()