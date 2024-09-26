import sqlite3
import sys

# class MyError(Exception):
#     def __init__():
#         self.message = "my custom message"


while True:
    x = input("Enter a number ")
    try:
        value = float(x)   # create instance of ValueError class
    except (ValueError, TypeError) as err:
        # print(err)
        # log the error here...
        print("Please enter a valid number.")
    except ZeroDivisionError as err:
        err.add_note("this is more info")  # added in 3.11
        raise err
    except Exception as err:
        pass   # no-op
    else:
        result = value / 2
        print(f"{result = }")
        break

print("DONE")

db_conn = None
try:
    db_conn = sqlite3.connect("/foo/bar/blah/monsters.db")
except sqlite3.DatabaseError as err:
    print(err)
    print("quitting")
    sys.exit()
else:
    ...
    #  access db here
finally:
    if db_conn:
        db_conn.close()



