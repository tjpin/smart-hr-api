import os
import sys


def clean_migrations():
    """
    This is a develepment file that removes all migrations.
    and also delete __pycache__ folders.
    If -db is passed as the first argument, develeopment database (db.sqlite3) will be deleted.
    """
    for root, dr, fl in os.walk("."):
        for d in dr:
            if d == "migrations" or d == "__pycache__":
                path = os.path.join(root, d)
                for _, __, mgs in os.walk(path):
                    for g in mgs:
                        if g == "__init__.py":  # or g == '0001_initial.py'
                            continue
                        if os.path.isfile(os.path.join(path, g)):
                            os.remove(os.path.join(path, g))
                            print("Deleting {}".format(os.path.join(path, g)))


if __name__ == "__main__":
    if "-db" in sys.argv and os.path.exists(
        os.path.join(os.path.dirname(__file__), "db.sqlite3")
    ):
        os.remove("db.sqlite3")
    clean_migrations()
