db.define_table('post',
    Field('content', 'text'),
    Field('user_id', db.auth_user))