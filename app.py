import pprint
import click

from flask import Flask

from db import db

app = Flask(__name__)


@app.route("/api/personal")
def personal_view():
    return {'data': db.get_personal_data}


@app.route("/api/experience")
def experience_view():
    return {'data': db.get_experience_data}


@app.route("/api/education")
def education_view():
    return {'data': db.get_education_data}


@app.cli.command("print-cv-data")
@click.argument('section')
def all_data_cmd(section):
    prop = getattr(db, f'get_{section}_data', None)
    if not prop:
        print('Please select one of the following sections: education, experience, personal')
    pprint.pprint(prop, depth=4)


app.cli.add_command(all_data_cmd)
