# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------
# This is a sample controller
# this file is released under public domain and you can use without limitations
# -------------------------------------------------------------------------

# ---- example index page ----
def index():
    return dict()

def services():
    return dict(message=T('Welcome to web2py!'))

def reviews():
    return dict(message=T('Welcome to web2py!'))

def contacts():
    return dict()

def vipiska_egrul():
    return dict()

def vipiska_egrn():
    return dict()

def grazdanskie_dogovory():
    return dict()

def zashhita_prav_potrebitelej():
    return dict()

def podgotovka_juridicheskih_documentov():
    return dict()

def pismennaya_konsultacia():
    return dict()

def yuridicheskaya_ekspertiza():
    return dict()

def oznakomlenie_s_materialamy():
    return dict()

def database():
    grid1 = SQLFORM.grid(db.register, deletable=True, editable=False)
    grid2 = SQLFORM.grid(db.consultation)
    return dict(grid1=grid1, grid2=grid2)

# ---- API (example) -----
@auth.requires_login()
def api_get_user_email():
    if not request.env.request_method == 'GET': raise HTTP(403)
    return response.json({'status':'success', 'email':auth.user.email})

# ---- Smart Grid (example) -----
@auth.requires_membership('admin') # can only be accessed by members of admin groupd
def grid():
    response.view = 'generic.html' # use a generic view
    tablename = request.args(0)
    if not tablename in db.tables: raise HTTP(403)
    grid = SQLFORM.smartgrid(db[tablename], args=[tablename], deletable=False, editable=False)
    return dict(grid=grid)

# ---- Embedded wiki (example) ----
def wiki():
    auth.wikimenu() # add the wiki to the menu
    return auth.wiki() 

# ---- Action for login/register/etc (required for auth) -----
def new_client():
    form = SQLFORM(db.register)
    form.process()
    if request.ajax:
        if form.accepted:
            return DIV("Message posted")
        elif form.errors:
            return TABLE(*[TR(k, v) for k, v in form.errors.items()])
    return dict(form=form)
 
def new_consultation():
    form = SQLFORM(db.consultation)
    form.process()
    if request.ajax:
        if form.accepted:
            return DIV("Message posted")
        elif form.errors:
            return TABLE(*[TR(k, v) for k, v in form.errors.items()])
    return dict(form=form)
 

def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())

# ---- action to server uploaded static content (required) ---
@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)
