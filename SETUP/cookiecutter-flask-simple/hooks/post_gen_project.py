import sys
from subprocess import run

print("Installing module in editable mode")
run([sys.executable, '-m', 'pip', 'install', '-e', '.'])
print()
run(["flask", "--app", "{{cookiecutter.app_slug}}", "init-db"])
print()

print("""
Now add your code to src/{{cookiecutter.app_slug}}/{{cookiecutter.app_slug}}.py.

Because of the editable install, you can run your app with the development server from anywhere on your computer with:
flask --app {{cookiecutter.app_slug}} run --debug


The following tasks may be run from the {{cookiecutter.app_slug}}_project folder:


Run all tests:
    pytest -v
   
Generate documentation:
    cd docs
    make latexpdf

    or
    
    cd docs
    make html
    
""")
