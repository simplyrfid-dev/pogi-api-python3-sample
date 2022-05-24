# PogiAPI - Python3

This Python 3 script - [pogiApi-cli.py](https://github.com/simplyrfid-dev/pogi-api-python3-sample/blob/master/pogiApi-cli.py), demonstrates how to login and retrieved data via Pogi API.
Connecting to PogiAPI via Python3 interpreter using Python's [request library](https://requests.readthedocs.io/en/master/)

Here is the list of operations you can do using this app:

| op         | Description |
| :---:      |:---         |
|id-current   | Get current inventory data|
|id-history     | Get inventory data  |
|id-get      | Get item by tag-id |
|id-add      | Create new item  |
|id-update   | Edit existing item by tag-id |
|id-delete   | Deiete an item by tag-id|

## Prerequisites
1. Python3 and pip3 installed
2. Python request library [installed](https://requests.readthedocs.io/en/master/user/install/#install)
3. Fill out the `user_id` and `user_pwd` variables inside the **pogiApi-cli.py** file.

To start the app, run this from the command line
```
% python3 pogiApi-cli.py

Signing in as: [user_id]
Log in (via token-get) succesful. User: [user_id]

==================================================
1. Fetch items (id-current)
2. Fetch item history (id-history)
3. Fetch item details (id-get)
4. Add item (id-add)
5. Update item (id-update)
6. Delete item (id-delete)
0. Exit
Enter op: (0-6):
```

### Important Note
You can check the whole information about the Pogi API here: [Pogi API Manual](https://www.simplyrfid.com/manuals/pogi-api-manual/)
