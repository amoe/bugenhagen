import pickle
import pprint
import jinja2

env = jinja2.Environment(
    loader=jinja2.FileSystemLoader('templates'),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True
)

with open('foo.pkl', 'rb') as handle:
    articles = pickle.load(handle)

tmpl = env.get_template('mytemplate.xhtml.j2')


for record in articles:
    print(record['user'])
    body = record['body']
    
    tmpl_params = {
        'title': "foo bar",
        'body': body
    }

    result = tmpl.render(tmpl_params)
#    print(result)

