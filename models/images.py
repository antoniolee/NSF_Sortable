db.define_table('images',
    Field('title', unique=True),
    Field('file', 'upload'),
    format = '%(title)s')
