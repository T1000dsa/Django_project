# venv/Scripts/activate | deactivate; venv -> 1 | 0
# pip install -U aiogram; -U when venv: 1 | -U if venv == True
# git add <file> | git add .
# git commit -m "disciption"
# git push origin main
# python3 -m venv venv
# venv/Scripts/activate.bat
# ./venv/Scripts/activate
# virtualenv .env
# git ls-files | xargs wc -l
# python manage.py runserver -O port
from jinja2 import Template, FileSystemLoader, Environment
from markupsafe import escape
pes = ['Alex', 'Bob','Jonson', 'Bill', 'Smith', 'Jeremy']
persons = [{'name':i, 'id':k, 'age':10*k}for k, i in enumerate(pes)]

file_loader = FileSystemLoader('newsite/main/frontend')
env = Environment(loader=file_loader)

tm = env.get_template('extends.html')
msg = tm.render(users=persons, domain='ooo.cringe', title='TestHtmlJinja')
with open('newsite/main/frontend/test_0.html', 'w') as file:
    file.write(msg)
print(msg)


html_0 = '''
{% macro input(name, value="", type='text', size=20) -%}
    <input type="{{ type }}" name="{{ name }}" value="{{ value|e }}" size="{{ size }}">
{%- endmacro %}
<p>{{ input("username") }}
<p>{{ input("email") }}
<p>{{ input("passwprd") }}
'''