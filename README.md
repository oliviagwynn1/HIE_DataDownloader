# BME590final

## Description 
This project was completed as a final project for the course BME590 MEedical Software Design. 
The project was completed Dr. Jason Luck, a professor of Biomechanics at Duke University. 

Client: Jason Luck, PhD (Injury Biomechanics Laboratory)
Contact information: jfl1@duke.edu

### Background 
Dr. Luck is leading a prospective study in the Raleigh-Durham community where youth athletes are instrumented with the DASHR: a novel, noninvasive sensor that uses industry-standard earpieces (e.g. hearing aids) in the bony canal to quantify head impact exposure. In association with head exposure data measured by the DASHR the research team is also completing both novel and traditional on- and off-field injury assessments to assist with quantifying the symptomology of participants from concussive and cumulative sub-concussive insults to the pediatric brain.


### Client Need
Hardware and software solution that accepts multiple HIE sensors simultaneously to accommodate downloading of HIE data from the devices to a central storage unit. 

### Functional Specifications
Software toolkit (GUI) [Python] to facilitate all aspects of downloading, logging and storage management.

*Download data (binary files) from multiple devices simultaneously (using a hub )

*Store downloaded data in folders associated with specific HIE device (each device will be associated with a unique PIN number)

*Store data by the date HIE data was acquired 

*Ability for client to download variable number of devices

*Post-download log report 

*Flexibility to interface with a database (i.e. SQL) and NTFS file system. All data is associated with a unique PIN and these data include the HIE sensor data that is the focus of the current document but also includes additional assessment and background data. 

## Visuals 

## Code and Functional Description of Current State 
### Overview 

### Front-end: 
#### Installation
The DASHR data download interface is run using React which encompasses a JavaScript libary that must be downloaded to the local computer. To accomplish this, the following steps can be taken:

##### Install ReactJS

* Install Node.JS (which comes with 'npm'--the node package manager): https://nodejs.org/en/
* Install the 'create-react-app' scaffolding tool:
  ```
  npm install -g create-react-app
  ```
* Go ahead and create a sample project called `react-learning` using `create-react-app` as follows:
  ```
  create-react-app react-learning
  ```
  This will create and initialize a react application in a new folder called `react-learning` in your current working directory. 
  
##### Clone react project

* `git clone git@github.com:oliviagwynn1/bme590final.git`
  
##### Install Dependencies after Cloning
After cloning a new react project to your computer (say from a partner) that you haven't used before, you will have to install project dependencies (just like you did previously in a virtual environment). Run `npm install --save` from the root of the directory to install all project dependencies. After this is complete, you can run your project.

##### Instal Back-end dependencies
Follow commands below.

##### Run a ReactJS Project
When in the root of the project, simply run `npm run start` which will compile your application and open it in a browser.


#### Description and Use


### Back-end: 
#### Installation
The server must be run on the the same machine that the DASHR hub is connected. This can be accomplished by with the following commands:

* `cd bme590final/`
* `python3.7 -m venv .venv`
* `source .venv/bin/activate`
* `pip install -r requirements.txt`
* `python React_Talk_Server.py`

#### Description and Use
This server has two routes `GET /api/send_device_info` and `POST /api/send_data`. This server interacts directly with the front end to retrieve general info of all connected volumes. The front end then appends the afformentioned data based on the selections of the client and returns it to the second server route. This route then downloads data from the devices, compiles it into a dictionary and sends it to the remote server and database. 

##### `GET /api/send_device_info`
  * Route gathers information from devices connected to the database.
  * The route has the mounting point for macs hard coded into it. This can be found commented out in line 202 of React_Talk_Server.py. For macs the correct mounting point is at `/Volumes/`. None of us own PCs so the code should be changed for PCs and Linux machines based on the mounting points for those machines. Devices should be found in a more streamlined way in future releases of this software, but we were not able to find a suitable way to do so by this deadline. 
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
  `{"message": "No devices were found"}`
  
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



### Database : 
#### Installation

##### Installation of Local DB on VM: 

These are steps to follow if the current set-up is not functioning and it must be set up again. 

Follow the instructions in this helpful link: https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/

In order to initiate use of the DB, one instance of the VM must run the command: "mongo" in the shell and be kept open in order to access the DB. 

Once this is running, you can manually access the DB with a different instance of the VM using iPython. However, this software does so using a post request and a FLASK server, which is further described below. 

The client (local), database, and collection that is being accessed in the DB can be altered in Lines 95-98 of `mongoserver_Dec11.py` as shown: 

    newdict = request.get_json()
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["practice_Dec11"]
    mycol = mydb["Players"]



##### Installation of Server
These are steps to follow if the current set-up is not function and it must be set up again. 

Using python, run the server script name `mongoserver_Dec11.py`. For example, in the shell of the VM, run the command: `python mongoserver_Dec11.py`.

This must be kept open in order to receive post requests. It may be necessary to change the port number in the bottom of the script. 

#### Description and Use

MongoDB is used to store the data. The MongoDB was deployed locally on a VM. The VM was a VCM Ubunutu. Details below: 

`Hostname:vcm-7653.vm.duke.edu`

`Operating System: Ubuntu 16.04`

`Base memory: 2 GB`

The data is stored in the db called: `Luck Data` and the collection called: `Players`

The server (run by flask and mongoserver_Dec11.py) is implemented on the same VM. It is able to receive post requests as structured as: 

`r=requests.post("http://vcm-7653.vm.duke.edu:5000/api/luck/add_data",json={DATA})`   

The 'DATA' is in the form of a dictionary with the keys: 
1. "_id" which is type str and stores a unique identifier for each player
2. "session_data" which is a dictionary 

The dictionary "session_data" contains the keys are the dates of sessions which data was uploaded. Within these keys are another dictionary which have keys of BIN files names. These dictionaries have the keys of "hash" (string of calculated hash of the decoded data sent to the sever), "data" (string of binary encoded session data), and "mod_time" (the time of data collection). 

To make things more clear, included is a correct format of a dictionary that could be uploaded: 

 `{'_id': '12',
 'session_data': {'date1': {'LBIN1': {'data': '8903hjfsisdfs',
    'hash': '9012ej.df',
    'mod_time': 'Feb127PM'}},
  'date2': {'LBIN': {'data': 'dajklfdajkl',
    'hash': 'sjf90j3lasd',
    'mod_time': 'Feb129PM'}}}}`
    
The mongoserver_Dec11.py code goes through the following steps which can be found in the script: 

*Connect to the DB and the correct collection

*Validate the dictionary that was received (correct structure, keys, type of data) and return error if incorrect and do not upload data. This is done with the function `validate_keys`

*Validate the correct data was received. This is done by a checksum using the hash sent in the dictinoary and a new hash one the data is decoded with the function `check_hash_server.py`

*Structure the received data correctly to be organized based on session date

*Add data to DB

*Go back into DB and make sure the data can be accessed, which means it was added correctly

*RETURNS: True if added correctly and data can be deleted of device and False if there was an error and data should not be deleted 

#### NOTE ABOUT CURRENT STATE: 

The current software cannot handle a full file of data. Thus, this software currently functions by cutting the size of the data in the dictionary that is sent with the post request. Thus, the checksum to make sure data was recieved correctly does not apply, even though it would function correctly. This function can be commented out.




## Authors and Acknowledgement 

Authors: Nikki Molino, Clark Bulleit, Rebecca Cohen, Olivia Gwynn

Other contributors: Jason Luck, Mark Palmeri, Suyash Kumar 

## Issues 

Please feel free to contact any of the team members with questions or issues. 

Nikki (nkm12@duke.edu, 6307449693)

Clark Bulleit (cb329@duke.edu)

Rebecca Cohen

Olivia Gwynn (og29@duke.edu)
