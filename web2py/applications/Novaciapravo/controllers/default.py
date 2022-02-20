# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------
# This is a sample controller
# this file is released under public domain and you can use without limitations
# -------------------------------------------------------------------------

# ---- example index page ----
def index():
    form1 = SQLFORM(db.register)
    if form1.process(session=None, formname='main').accepted:
        response.flash = 'form accepted'
        redirect(URL('post_success'))
    elif form1.errors:
        response.flash = 'form has errors'
    else:
        response.flash = 'please fill the form'
    # Note: no form instance is passed to the view
    form2 = SQLFORM(db.email_problem)
    if form2.process(session=None, formname='email').accepted:
        response.flash = 'form accepted'
        redirect(URL('post_success'))
    elif form2.errors:
        response.flash = 'form has errors'
    else:
        response.flash = 'please fill the form'
    return dict()

def services():
    return dict(message=T('Welcome to web2py!'))

def reviews():

    form = SQLFORM(db.review)
    if form.process(session=None, formname='review').accepted:
        response.flash = 'form accepted'
        redirect(URL('review_success'))
    elif form.errors:
        response.flash = 'form has errors'
    else:
        response.flash = 'please fill the form'
    # Note: no form instance is passed to the view
    return dict()
    
def reviews_list():
    query = db.review.id > 0
    reviews = db(query).select()
    return dict(reviews=reviews)

def articles_list():
    query = db.article.id > 0
    articles = db(query).select()
    return dict(articles=articles)


def poleznaya_informacia():
    form = SQLFORM(db.article)
    if form.process(session=None, formname='article').accepted:
        response.flash = 'form accepted'
        redirect(URL('review_success'))
    elif form.errors:
        response.flash = 'form has errors'
    else:
        response.flash = 'please fill the form'


    # Note: no form instance is passed to the view
    return dict()

def article_detail():
    id=request.vars.id
    articles=db(db.article.id==id).select()
    if not len(articles): redirect(URL('index'))

    return dict(article=articles[0])

def contacts():
    return dict()

def privacy():
    return dict()

# ---- SERVICES ----

def predstavitelstvo_v_grazhdanskom_sude():
    response.view = 'default/services/predstavitelstvo_v_grazhdanskom_sude.html'
    return dict()

def vipiska_egrul():
    response.view = 'default/services/vipiska_egrul.html'
    return dict()

def vipiska_egrn():
    response.view = 'default/services/vipiska_egrn.html'
    return dict()

def grazdanskie_dogovory():
    response.view = 'default/services/grazdanskie_dogovory.html'
    return dict()

def zashhita_prav_potrebitelej():
    response.view = 'default/services/zashhita_prav_potrebitelej.html'
    return dict()

def podgotovka_juridicheskih_documentov():
    response.view = 'default/services/podgotovka_juridicheskih_documentov.html'
    return dict()

def pismennaya_konsultacia():
    response.view = 'default/services/pismennaya_konsultacia.html'
    return dict()

def yuridicheskaya_ekspertiza():
    response.view = 'default/services/yuridicheskaya_ekspertiza.html'
    return dict()

def oznakomlenie_s_materialamy():
    response.view = 'default/services/oznakomlenie_s_materialamy.html'
    return dict()

def vklyuchenie_v_reestr_trebovanij_kreditorov():
    response.view = 'default/services/vklyuchenie_v_reestr_trebovanij_kreditorov.html'
    return dict()

def vzyskanie_dolgov():
    response.view = 'default/services/vzyskanie_dolgov.html'

    form1 = SQLFORM(db.register)
    if form1.process(session=None, formname='main').accepted:
        response.flash = 'form accepted'
        redirect(URL('post_success'))
    elif form1.errors:
        response.flash = 'form has errors'
    else:
        response.flash = 'please fill the form'

    return dict()

# ---- SUCCESS PAGE ----
def post_success():
    response.view = 'default/redirect/post_success.html'
    return dict()

def review_success():
    response.view = 'default/redirect/review_success.html'
    return dict()

@auth.requires_login()
def database():
    grid1 = SQLFORM.grid(db.register, editable=True, deletable=True, details=True   )
    grid2 = SQLFORM.grid(db.consultation)
    grid3 = SQLFORM.grid(db.review, deletable=True, details=True)
    grid4 = SQLFORM.grid(db.email_problem, deletable=True)
    grid5 = SQLFORM.grid(db.article, deletable=True)
    return dict(grid1=grid1, grid2=grid2, grid3=grid3, grid4=grid4, grid5=grid5)

# ---- API (example) -----

def api_get_user_email():
    if not request.env.request_method == 'GET': raise HTTP(403)
    return response.json({'status':'success', 'email':auth.user.email})

# ---- Smart Grid (example) -----
# can only be accessed by members of admin groupd
def grid():
    response.view = 'generic.html' # use a generic view
    tablename = request.args(0)
    if not tablename in db.tables: raise HTTP(403)
    grid = SQLFORM.smartgrid(db[tablename], args=[tablename], deletable=False, editable=False)
    return dict(grid=grid)

# ---- Action for login/register/etc (required for auth) -----
def new_consultation_ajax():
    form = SQLFORM(db.consultation, formstyle='divs')
    form.process()
    if request.ajax:
        if form.accepted:
            redirect(URL('post_success'), client_side=True)
            
        elif form.errors:
            response.flash("Что-то пошло не так")
    return dict(form=form)
    
 
def new_consultation():
    form = SQLFORM(db.consultation)
    if form.accepts(request, formname=None):
        redirect(URL('post_success'))
    elif form.errors:
        return TABLE(*[TR(k, v) for k, v in form.errors.items()])
    
 

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
