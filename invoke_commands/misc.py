from invoke import task
from .vars import package_name, boilerplate_branch


@task
def lint(c):
    c.run("black {}".format(package_name))
    c.run("flake8 {}".format(package_name))


@task
def update_boilerplate(c):
    c.run("git fetch boilerplate")  # TODO: this knows the name of the remote
    c.run("git merge boilerplate/{} --no-edit".format(boilerplate_branch))


@task
def notebook(c):
    c.run("export PATH=$PATH:..")
    c.run("jupyter-notebook")
