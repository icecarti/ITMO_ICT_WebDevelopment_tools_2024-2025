from datetime import date

mock_db = [
    {
        "id": 1,
        "name": "Pal Palych",
        "register_date": date(2024, 10, 15),
        "birth_date": date(1989, 2, 11),
        "books": [
            {
                "id": 1,
                "own_since": date(2024, 10, 15),
                "info": {
                    "id": 1,
                    "title": "Идиот",
                    "author": "Достоевский Ф.М.",
                    "release_date": date(1869, 1, 19),
                    "genre": "Роман",
                    "tags": []
                }
            },
            {
                "id": 2,
                "own_since": date(2024, 12, 25),
                "info": {
                    "id": 2,
                    "title": "Три Товарища",
                    "author": "Ремарк Э.М.",
                    "release_date": date(1936, 12, 5),
                    "genre": "Военная проза",
                    "tags": []
                }
            }
        ]
    },
    {
        "id": 2,
        "name": "Ivan Ivanych",
        "register_date": date(2023, 5, 19),
        "birth_date": date(1997, 7, 22),
        "books": [
            {
                "id": 3,
                "own_since": date(2023, 5, 19),
                "info": {
                    "id": 3,
                    "title": "Старик и море",
                    "author": "Хемингуэй Э.",
                    "release_date": date(1952, 9, 1),
                    "genre": "Роман",
                    "tags": []
                }
            },
            {
                "id": 4,
                "own_since": date(2023, 5, 19),
                "info": {
                    "id": 4,
                    "title": "История государства Российского",
                    "author": "Карамзин Н.М.",
                    "release_date": date(1816, 1, 1),
                    "genre": "История",
                    "tags": []
                }
            }
        ]
    }
]
