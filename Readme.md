How to run:

1. Installation: pip install -r requirements.txt (preferably into a virtual env)
2. Run flask server: flask run (optionally set FLASK_ENV=development for dev server)
3. Access endpoints at:  http://{hostname}:{port}/api/{{section-name}}, where section is one of: experience, personal, education
4. Run the command by running: flask print-cv-data {{section-name}}, where section is one of: experience, personal, education