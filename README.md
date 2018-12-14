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
####Installation
#### Description and Use


### Back-end: 
####Installation
#### Description and Use

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

Clark Bulleit ()

Rebecca Cohen

Olivia Gwynn 









