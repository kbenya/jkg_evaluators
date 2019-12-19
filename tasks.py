from invoke import task, Collection

from invoke_commands import docs, clean, sonar, test, release

from invoke_commands.vars import package_name, boilerplate_branch


@task
def lint(c):
    c.run("black {}".format(package_name))
    c.run("flake8 {}".format(package_name))

@task
def update_boilerplate(c):
    c.run("git fetch boilerplate")  # TODO: this knows the name of the remote
    c.run("git merge boilerplate/{} --no-edit".format(boilerplate_branch))


ns = Collection()
ns.add_collection(Collection.from_module(release))
ns.add_collection(Collection.from_module(docs))
ns.add_collection(Collection.from_module(clean))
ns.add_collection(Collection.from_module(sonar))
ns.add_collection(Collection.from_module(test))
