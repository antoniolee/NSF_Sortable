from datetime import datetime

def get_email():
    if auth.user:
        return auth.user.email
    else:
        return 'None'

db.define_table('survey',
    # There is also a column called 'id'. 
    # Field('author', default = get_email()), # 512 chars at most
    Field('author', default = get_email()),
    Field('creation_date', 'datetime', default=datetime.utcnow()),
    Field('Q1','text'),
    Field('Q2', 'text'),
    Field('Q3', 'text'),
    Field('Q4', 'text'),
    Field('Q5', 'text'),
    Field('Q6', 'text'),           
)

db.survey.author.writable = False
db.survey.id.readable = False
db.survey.creation_date.writable = False

