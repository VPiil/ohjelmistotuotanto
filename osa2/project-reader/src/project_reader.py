from urllib import request
from project import Project
import tomllib


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")

        data = tomllib.loads(content)
        print(data)

        project = data["project"]

        nimi = project["name"]

        desc = project["description"]

        license = project["license"]

        authors = project["authors"]

        dependencies = project["dependencies"]

        dependencygroups = data["dependency-groups"]
        dev_dependencies = dependencygroups["dev"]

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(nimi, desc, license, authors, dependencies, dev_dependencies)
