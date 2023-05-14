![air_bnb_clone](https://github.com/MimiSuri/AirBnB_clone/assets/117779612/30d91b24-84be-4bd1-aeaf-bb4d4438c50e)
AirBnB clone - The console
Console
A python command interpreter program built using the python module cmd. Contains to create, update, delete and print a class instance or all instaces created.

Getting Started
To start the command interpreter type in these commands in your terminal:

Cloning the repo and starting the console:
==========================================

git clone https://github.com/MimiSuri/AirBnB_clone.git
cd AirBnB_clone
./console.py
Usage
Help for the console program can be obtained by running the program first and with the help command. This will show the available commands:

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

You can get help for specific command by specifing help <command>. For example

(htnb) help create

Usage: create BaseModel

        Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id.
Usage and Examples
./console.py

# Create a BaseModel instance and print its id
(htnb) create BaseModel
b61e46d6-9143-4d37-b271-ce76a759d6a6

# to print the instance
(htnb) show BaseModel b61e46d6-9143-4d37-b271-ce76a759d6a6
[BaseModel] (b61e46d6-9143-4d37-b271-ce76a759d6a6) {'id': 'b61e46d6-9143-4d37-b271-ce76a759d6a6', 'created_at': datetime.datetime(2021, 6, 30, 11, 34, 53, 117968), 'updated_at': datetime.datetime(2021, 6, 30, 14, 34, 53, 118060)}

# to print all object created previously
(htnb) all
["[BaseModel] (b61e46d6-9143-4d37-b271-ce76a759d6a6) {'id': 'b61e46d6-9143-4d37-b271-ce76a759d6a6', 'created_at': datetime.datetime(2021, 6, 30, 11, 34, 53, 117968), 'updated_at': datetime.datetime(2021, 6, 30, 14, 34, 53, 118060)}", "[BaseModel] (426aea0f-5012-4a52-9a3a-3c775ff98e07) {'id': '426aea0f-5012-4a52-9a3a-3c775ff98e07', 'created_at': datetime.datetime(2021, 6, 30, 13, 29, 6, 1369), 'updated_at': datetime.datetime(2021, 6, 30, 13, 29, 6, 1383)}"]
Contributing
Pull requests are welcome.

Please make sure to update tests as appropriate.

License
This software is open-source.

Author
miimiisurii@yahoo.com
Aminu Umar Hassan
