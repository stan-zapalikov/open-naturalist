from marshmallow import fields, Schema

class UserSchema(Schema):
    id = fields.String()
    username = fields.String()
    email = fields.String()
    password = fields.String()

class SightingSchema(Schema):
    id = fields.String()
    name = fields.String()
    latitiude = fields.Float()
    longitude = fields.Float()