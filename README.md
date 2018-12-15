### Front-end: 

#### Installation
##### Local Server
The server must be run on the the same machine that the DASHR hub is connected. This can be accomplished by with the following commands:

* `git clone git@github.com:oliviagwynn1/bme590final.git`
* `cd bme590final/`
* `python3.7 -m venv .venv`
* `python3.7 -m venv .venv`
* `source .venv/bin/activate`
* `pip install -r requirements.txt`
* `python React_Talk_Server.py`

#### Description and Use
This server has two routes `GET /api/send_device_info` and `POST /api/send_data`. This server interacts directly with the front end to retrieve general info of all connected volumes. The front end then appends the afformentioned data based on the selections of the client and returns it to the second server route. This route then downloads data from the devices, compiles it into a dictionary and sends it to the remote server and database. 

##### `GET /api/send_device_info`

