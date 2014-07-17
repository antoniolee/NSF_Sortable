# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
## - call exposes all registered services (none by default)
#########################################################################
import random

def index():
    images = db().select(db.images.ALL, orderby=db.images.title)
    return dict(images=images)  

@auth.requires_login()
def database():
    grid = SQLFORM.grid(db.sortable,
        searchable=True,
        fields=[db.sortable.creation_date, db.sortable.author, 
                db.sortable.OG_order, db.sortable.new_order, db.sortable.card_data],
        csv=False,
        details=True, create=False, editable=False, deletable=True,
        maxtextlength=500, paginate=10,
        )
    return dict(grid=grid)  

@auth.requires_login()
def surveyDatabase():
    grid = SQLFORM.grid(db.survey,
        searchable=True,
        fields=[db.survey.creation_date, db.survey.author, 
                db.survey.Q1, db.survey.Q2, db.survey.Q3, db.survey.Q4, db.survey.Q5, db.survey.Q6],
        csv=False,        
        details=True, create=False, editable=False, deletable=True,
        maxtextlength=500, paginate=10,
        )
    return dict(grid=grid)        

@auth.requires_login()
def sortable():
    images = db().select(db.images.ALL, orderby=db.images.title)
    randomImages = list(images)
    random.shuffle(randomImages)
    return dict(images=randomImages)  

@auth.requires_login()
def survey():
    return dict()

@auth.requires_login()
def saveSurvey():
    var1 = request.vars.var1
    var2 = request.vars.var2
    var3 = request.vars.var3
    var4 = request.vars.var4
    var5 = request.vars.var5
    var6 = request.vars.var6
    db.survey.insert(Q1=var1,Q2=var2,Q3=var3, Q4=var4, Q5=var5, Q6=var6)
    return dict()      

@auth.requires_login()
def saveSortable():
    varA = request.vars.varA
    varB = request.vars.varB
    varC = request.vars.varC
    db.sortable.insert(OG_order=varA, new_order=varB, card_data=varC)
    return dict()     

def test():
    return dict()  

def download():
 return response.download(request, db)


def user():
    
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/manage_users (requires membership in
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())

@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()


@auth.requires_signature()
def data():
    """
    http://..../[app]/default/data/tables
    http://..../[app]/default/data/create/[table]
    http://..../[app]/default/data/read/[table]/[id]
    http://..../[app]/default/data/update/[table]/[id]
    http://..../[app]/default/data/delete/[table]/[id]
    http://..../[app]/default/data/select/[table]
    http://..../[app]/default/data/search/[table]
    but URLs must be signed, i.e. linked with
      A('table',_href=URL('data/tables',user_signature=True))
    or with the signed load operator
      LOAD('default','data.load',args='tables',ajax=True,user_signature=True)
    """
    return dict(form=crud())
