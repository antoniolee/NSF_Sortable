from datetime import datetime

def get_email():
    if auth.user:
        return auth.user.email
    else:
        return 'None'

db.define_table('sortable',
    # There is also a column called 'id'. 
    # Field('author', default = get_email()), # 512 chars at most
    Field('author', default = get_email()),
    Field('creation_date', 'datetime', default=datetime.utcnow()),
    Field('OG_order','text'),
    Field('new_order', 'text'),
    Field('card_data', 'text'),       
    )

db.sortable.author.writable = False
db.sortable.id.readable = False
db.sortable.creation_date.writable = False
