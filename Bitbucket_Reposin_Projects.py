import stashy

bitbucket = stashy.connect("Bitbucket Host", "UserName", "Password")

projects =["project1"]

for project in projects:
    for repo in bitbucket.projects["%s" % project].repos.list():
        print(repo["project"]['key'],repo["name"])



