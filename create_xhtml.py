import pickle
import pprint
import jinja2

env = jinja2.Environment(
    loader=jinja2.FileSystemLoader('templates'),
    autoescape=True
)

with open('foo.pkl', 'rb') as handle:
    foo = pickle.load(handle)

tmpl = env.get_template('mytemplate.xhtml.j2')

result = tmpl.render({'title': "foo bar"})

print(result)
