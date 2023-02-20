import sqlite

# Connect to the SQLite database
conn = sqlite3.connect('bitbug.db')

# Create a table to store tNhe rules
conn.execute('''CREATE TABLE IF NOT EXISTS rules
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 name TEXT NOT NULL,
                 type TEXT NOT NULL,
                 desc TEXT,
                 syntax TEXT NOT NULL,
                 vars TEXT NOT NULL)''')

# Define a function to insert a rule into the database
def add_rule(rule,type,desc):
    conn.execute("INSERT INTO rules (rule) VALUES (?,?,?,?,?,?)", (name,type,desc,syntax,vars))
    conn.commit()

# Define a function to retrieve all the rules from the database
def get_rules():
    cursor = conn.execute("SELECT * from rules")
    rules = []
    for row in cursor:
        rules.append(row[1])
    return rules

# Add a rule to the database
# Rule must only pertain to ONE application/technique.
#   The technique will be called 'type'.
#   The Syntax for using the tool will be called 'Syntax'.  There will be variables listed in the syntax, in the format @@VAR@@ or optionally ^^VAR^^
#   The variables will be needed to be added separately into a vars field for quick access, i.e @@VAR1@@, @@VAR2@@, ^^VAR3^^
# FOR Any of the below:  There will be another database table based on the 'name-type' i.e: in errors, installers, etc - "ffuf-fuzz-dirfile"
#   Installer will need to be stored separately in a database 'installers'
#   Errors resultant from using the tool/rule will need to be stored separately in a database 'errors'
#   Wordlists will need to be installed in (or symbolically linked to, ideally: /w .. i.e : /w/seclists/Passwords/Common-Credentials/500-worst-passwords.txt
add_rule("feroxbuster","fuzz-dirfile","Feroxbuster general file/dirfuzzer","feroxbuster -u @@URL@@ --insecure ^^-w==WORDLIST^^","^^WORDLIST^^")
add_rule("feroxbuster","fuzz-dirfile-proxy","Feroxbuster Proxied file/dirfuzzer","feroxbuster -u http://127.1 --insecure --proxy http://127.0.0.1:@@PROXY_PORT@@","@@PROXY_PORT")
add_rule("ffuf","fuzz-dirfile","FFUF general file/dirfuzzer","","")
add_rule("wfuzz","fuzz-dirfile","wfuzz general file/dir fuzzer","","")
add_rule("ffuf","fuzz-api","FFUF api fuzzer","","")
add_rule("wfuzz","fuzz-api","wfuzz api fuzzer","","")
add_rule("ffuf","fuzz-subdomain","wfuzz subdomain fuzzer","","")
add_rule("wfuzz","fuzz-subdomain","wfuzz subdomain fuzzer","","")

# Retrieve all the rules from the database and print them

print(get_rules())

# Close the database connection
conn.close()

