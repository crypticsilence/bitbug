import sqlite

# Connect to the SQLite database
conn = sqlite3.connect('bitbug.db')

# Create a table to store the installers
conn.execute('''CREATE TABLE IF NOT EXISTS installers
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 name TEXT NOT NULL,
                 type TEXT NOT NULL,
                 desc TEXT,
                 prereq TEXT NOT NULL,
                 cmdinstall TEXT NOT NULL,
                 cmdupdate TEXT NOT NULL,
                 check TEXT NOT NULL,
                 checkresp TEXT NOT NULL)''')

# Define a function to insert a installer into the database
def add_installer(installer,type,desc,prereq,cmdinstall,cmdupdate,check,checkresp):
    conn.execute("INSERT INTO intallers (installer) VALUES (?,?,?,?,?,?,?,?)", (name,type,desc,preqreq,cmdinstall,cmdupdate,check,checkresp))
    conn.commit()

# Define a function to retrieve all the installers from the database
def get_installers():
    cursor = conn.execute("SELECT * from installers")
    installers = []
    for row in cursor:
        installers.append(row[1])
    return installers

# Add a installer to the database
# installer must only pertain to ONE application/technique.
#   The technique will be called 'type'.
#   The Syntax for installing the tool will be called 'cmd'.  There may be variables listed in the syntax, in the format @@VAR@@ or optionally ^^VAR^^
#   Any prereq's will be listed in the field 'prereq' in the form of the name field,optionally comma separated: "go,feroxbuster"
# A "scan" tool will try different requests to find IPs, urls or information
# A "enum" tool will try different requests to find IPs, urls or information
# A "fuzz" tool will try MANY different requests to find urls, information or vulnerabilities
# A "vuln" tool will try MANY different requests to find vulnerabilities
# FOR Any of the below:
#   Bitbug installation folder == ^^BITBUG^^
#   /opt folder == ^^OPT^^
#   Users home folder == ^^HOME^^
#   Wordlists will need to be installed in (or symbolically linked to, ideally: /w .. i.e : /w/seclists/Passwords/Common-Credentials/500-worst-passwords.txt
#   If the cmdupdate command is empty, try the installer command again to update (and hope it works!)

#add_installer("name","type","desc","prereq","install","update","check","checkresp")
#languages/etc
add_installer("apt","package tool","apt package tool","","","","apt --version","apt ")  # this should be already installed on any compatible distro
add_installer("python3","language","The famous Python 3 scripting/programming language","","sudo apt update; sudo apt install -y python3 pip","sudo apt update; sudo apt install -y python3 pip","python --version","Python 3")
add_installer("python2","language","The famous Python 2 scripting/programming language","","sudo apt update; sudo apt install -y python2","sudo apt update; sudo apt install -y python2","python2 --version","Python 2")
add_installer("go","language","golang language","","wget -q -O - https://git.io/vQhTU | bash; source /root/.bashrc","wget -q -O - https://git.io/vQhTU | bash; source /root/.bashrc","go --version","Go is a tool for managing Go source code.")
add_installer("rust","language","rust language","","curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y","rustup update","rustc","rustc [OPTIONS] INPUT")
#security tools
add_installer("feroxbuster","web-fuzz","Feroxbuster fuzzer for forced browsing, including Predictable Resource Location, File Enumeration, Directory Enumeration, and Resource Enumeration ","apt","sudo apt update; apt install -y feroxbuster","sudo apt update; sudo apt install -y feroxbuster","feroxbuster --help","(@epi052)")
add_installer("ffuf","web-fuzz","FFUF fuzzer","go","go install github.com/ffuf/ffuf/v2@latest","go install github.com/ffuf/ffuf/v2@latest","ffuf --help","Fuzz Faster U Fool")
add_installer("wfuzz","web-fuzz","wfuzz fuzzer","python","pip install wfuzz","pip install wfuzz","wfuzz -h","The Web Fuzzer")
add_installer("nikto","web-enum","nikto web enumeration tool","apt","sudo apt update; sudo apt install nikto -y","nikto -update","nikto -Version","Nikto Versions")

#
add_installer("subfinder","dns-fuzz","subfinder","go","go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest","","subfinder -h","Subfinder is a subdomain discovery tool that discovers subdomains for websites")
add_installer("massdns","dns-fuzz","MassDNS","python3","git clone https://github.com/blechschmidt/massdns.git ; cd massdns ; make; cp bin/massdns /usr/local/bin","","massdns -h","Usage: massdns")
add_installer("sublist3r","dns-fuzz","sublist3r","python3","git clone https://github.com/aboul3la/Sublist3r.git; cd Sublist3r; python3 setup.py install","","sublist3r -h","usage: sublist3r [-h]")
add_installer("nmap","scan","nmap - the ultimate network scanning tool!!","","apt update; apt install -y nmap","","nmap --version","Nmap version ")
add_installer("gobuster","web-fuzz","gobuster","go","go install github.com/OJ/gobuster/v3@latest","","gobuster","gobuster [command]")
add_installer("getjs","web-enum","GetJS","go","go install github.com/003random/getJS@latest","","","")
add_installer("golinkfinder","web-enum","GoLinkFinder","go","go install github.com/0xsha/GoLinkFinder@latest","","go","")
add_installer("getallurls","web-enum",") fetches known URLs from AlienVault's Open Threat Exchange, the Wayback Machine, Common Crawl, and URLScan for any given domain. Inspired by Tomnomnom's waybackurls.","go","go install github.com/lc/gau/v2/cmd/gau@latest","","gau --help","Usage of gau:")
add_installer("waybackurls","web-enum","Search WayBack Machine for other URLs","go","go install github.com/tomnomnom/waybackurls@latest","","waybackurls --help","Usage of waybackurls:")
add_installer("waybackrobots","web-enum","Search WayBack Machine for robots.txt","go","go install github.com/vodafon/waybackrobots@latest","","waybackrobots --help","Usage of waybackrobots:")
add_installer("xsshunter","web-vuln-xss","XSS Hunter","python3","pip install XSSHunter","","","")
add_installer("trufflehog","web-enum","A tool for finding credentials.","git clone https://github.com/trufflesecurity/trufflehog.git; cd trufflehog ; go install","","trufflehog --help","TruffleHog is a tool for finding credentials.")
add_installer("sqlmap","sql-vuln","The best SQL Injection tool!","python3","git clone --depth 1 https://github.com/sqlmapproject/sqlmap.git sqlmap-dev; cd sqlmap-dev; echo '#!/usr/bin/python3'>sqlmap; echo 'python3 /opt/sqlmap-dev/sqlmap.py \"$@\"'>>sqlmap; chmod +x sqlmap; mv sqlmap /usr/local/bin","","sqlmap -h","Usage: python3 sqlmap")
add_installer("tplmap","web-vuln-template","Template injection scanner","python3","git clone https://github.com/epinna/tplmap.git; cd tplmap; pip install -r requirements.txt; echo '#!/usr/bin/python3'>tplmap; echo 'python3 /opt/tplmap/tplmap.py \"$@\"'>>tplmap; chmod +x tplmap; mv tplmap /usr/local/bin","","","")
add_installer("ppmap","web-vuln-python","Parameter Pollution scanner","git clone https://github.com/kleiton0x00/ppmap.git ; cd ppmap; bash setup.sh","","echo 'hi' | ppmap","@kleiton0x7e")
#"commix",
#"cmseek",
#"W3broot",
add_installer("fuxploider","web-vuln","File upload exploitation tool","git clone https://github.com/almandin/fuxploider.git; cd fuxploider ; sudo pip3 install -r requirements.txt; echo '#!/usr/bin/python3'>fuxploider; echo 'python3 /opt/fuxploider/fuxploider.py \"$@\"'>>fuxploider; chmod +x fuxploider; mv fuxploider /usr/local/bin","","fuxploider","")



add_installer("xxeinjector","web-vuln","XXEInjector","python3","pip install XXEInjector","pip install XXEInjector",
add_installer("","web-vuln","SSRFDetector","python3","pip install SSRFDetector","pip install SSRFDetector",
add_installer("","web-vuln","RaceTheWeb","python3","pip install RaceTheWeb","pip install RaceTheWeb",
add_installer("","web-vuln","CORStest","python3","pip install CORStest","pip install CORStest",
add_installer("","web-enum","GitTools","python3","pip install GitTools","pip install GitTools",
add_installer("","web-enum","gitallsecrets","python3","pip install gitallsecrets","pip install gitallsecrets",
add_installer("","web-enum","EyeWitness","python3","pip install EyeWitness","pip install EyeWitness",
add_installer("","web-enum","parameth","python3","pip install parameth","pip install parameth",

# Retrieve all the installers from the database and print them

print(get_installers())

# Close the database connection
conn.close()

