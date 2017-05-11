from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError

from ..models import MyModel


@view_config(route_name='home', renderer='../templates/mytemplate.jinja2')
def my_view(request):
    try:
        query = request.dbsession.query(MyModel)
        one = query.filter(MyModel.name == 'one').first()
    except DBAPIError:
        return Response(db_err_msg, content_type='text/plain', status=500)
    return {'one': one, 'project': 'pyramid_hs'}


db_err_msg = """\
Pyramid is having a problem using your SQL database.  The problem
might be caused by one of the following things:

1.  You may need to run the "initialize_pyramid_hs_db" script
    to initialize your database tables.  Check your virtual
    environment's "bin" directory for this script and try to run it.

2.  Your database server may not be running.  Check that the
    database server referred to by the "sqlalchemy.url" setting in
    your "development.ini" file is running.

After you fix the problem, please restart the Pyramid application to
try it again.
"""


@view_config(route_name="hello_html", renderer='../templates/hello.jinja2')
def hello_h(request):
    request.response.status = 200
    return {'message': 'Hello World!'}


@view_config(route_name="hello_json", renderer='json')
def hello(request):
    request.response.status = 200
    return {'message': 'hello world'}

@view_config(route_name="simple_form", renderer="../templates/simple_form.jinja2")
def simple_form(request):
    request.response.status = 200
    return {}

@view_config(route_name="form_resp", renderer="../templates/form_response.jinja2")
def form_resp(request):
    request.response.status = 200
    return {'message': request.params['message']}
