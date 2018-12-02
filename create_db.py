from pymodm import connect
from pymodm import MongoModel, fields

connect("mongodb://bme590:hello12345@ds123664.mlab.com:23664/concussion")


# use list field
class Player(MongoModel):
    player_id = fields.IntegerField(primary_key=True)
    session_label = fields.ListField(field=fields.BigIntegerField())
    session_data = fields.ListField(field=fields.DateTimeField())
    upload_time = fields.ListField(field=fields.DateTimeField())
    # session_label and session_data line up by index
