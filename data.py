import json
import sqlite3
from webbrowser import get

# Connect to db
try:
    con = sqlite3.connect('', check_same_thread=False)
    db = con.cursor()
except:
    print("Could not connect to Database")

# Grab JSON data
with open('', 'r') as read_file:
    data = json.load(read_file)

# Data value
x = data['']
count = 0

# For every item inside of the JSON file, add to db
for item in x:
    item = x[count]['']
    db.execute(f"ALTER TABLE user_bar ADD [{item}] BOOLEAN")
    count += 1
con.commit()
