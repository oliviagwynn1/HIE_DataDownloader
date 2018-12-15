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
  * Route gathers information from devices connected to the database.
  * The route has the mounting point for macs hard coded into it. This can be found commented out in line 202 of React_Talk_Server.py. For macs the correct mounting point is at `/Volumes/`. None of us own macs so the code should be changed for PCs and Linux machines based on the mounting points for those machines. Devices should be found in a more streamlined way in future releases of this software, but we were not able to find a suitable way to do so by this deadline. 
  * The `/Test/` folder in this repo contains test data from both of the DASHRS. The current version of the React_Talk_Server.py code accesses this folder in order to work correctly. 
  * The route outputs device information in the following format:
  ```sh
    {
        'Players': ['261758686', '261813717'],
        'Mount_Points': ['/Volumes/MV1', '/Volumes/MV1 1'],
        'Num_Files': [609, 14],
    }
   ```
  * If no devices can be accessed the server will return a response of 250 with a message in the following format. The front end will handle this accordinly
  `{"message": "No devices were found"})`
  
##### `POST /api/send_data`
  * Route downloads data from devices based on the response of the client. It expects the following input:
   ```sh
    {
        'Players': ['261758686', '261813717'],
        'Mount_Points': ['/Volumes/MV1', '/Volumes/MV1 1'],
    }
   ```
   * The route goes into the given mounting point for each of the Players, downloads the data and then posts the following dictionary to the remote server and database:
   ```sh
   {
        '_id': '261758686', {
            'session_data': {
                '2018-10-12': {
                    'L0': {
                        'data': '8903hjfsisdfs',
                        'hash': '9012ej.df',
                        'mod_time': 'Feb127PM'}},
                '2018-10-13': {
                    'L0': {
                        'data': 'dajklfdajkl',
                        'hash': 'sjf90j3lasd',
                        'mod_time': 'Feb129PM'
                        }
                    }
                }
            }
   ```
   * If the dictionary is not in the correct form then the it will return one of the following error messages based on the error and the response integer of 205 which the front end will be able to handle. 
   ```sh
   error_messages = {
        0: {"message": "Post Keys not correct"},
        1: {"message": "Device dictionary keys are not lists"},
        2: {"message": "Device dictionary lists are not equal"},
   ```
   
   * If the route cannot connect to the remote server or the database then it will return a response of 210 and the following error message:
   ```sh
   {"message": "Cannot connect to remote server"}
   ```
   * The current route cannot send the full ammount of data to the remote server, the connection keeps getting lost with this amount of data. If this issue is fixed in the future, the code can be fixed in line 157 of React_Talk_Server.py. 
   
 
    
    
  
  

