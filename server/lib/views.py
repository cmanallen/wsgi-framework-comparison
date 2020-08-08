from marshmallow_jsonapi import fields, Schema


def dasherize(key):
    return key.replace('_', '-')


class UserSchema(Schema):
    id = fields.Integer()
    username = fields.String()
    first_name = fields.String()
    middle_name = fields.String()
    last_name = fields.String()
    is_active = fields.Boolean()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()

    class Meta:
        type_ = 'users'
        inflect = dasherize
