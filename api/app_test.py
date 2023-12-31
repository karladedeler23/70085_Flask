from app import process_query


def test_knows_about_dinosaurs():
    assert (
        process_query("dinosaurs") == "Dinosaurs \
            ruled the Earth 200 million years ago"
    )


def test_does_not_know_about_asteroids():
    assert process_query("asteroids") == "Unknown"


def test_knows_about_name():
    assert process_query("What is your name?") == "Howell_Karla_Joey"


def test_add():
    assert process_query("What is 2 plus 7?") == "9"


def test_multiply():
    assert process_query("What is 2 multiplied by 7?") == "14"


def test_largest_number():
    assert (
        process_query(
            "Which of the following \
                           numbers is the largest: 1, 2, 3?"
        )
        == "3"
    )
