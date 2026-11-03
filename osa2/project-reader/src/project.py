class Project:
    def __init__(self, name, description, license, authors, dependencies, dev_dependencies):
        self.name = name
        self.description = description
        self.license = license
        self.authors = authors
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def _stringify_dependencies(self, dependencies):
        return ", ".join(dependencies) if len(dependencies) > 0 else "-"

    def lista(self, items):
        if not items:
            return "-"

        return "\n".join(f"- {item}" for item in items)

    def __str__(self):
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicence: {self.license or '-'}"
            f"\nAuthors: \n{self.lista(self.authors)}"
            f"\nDependencies: \n{self.lista(self.dependencies)}"
            f"\nDevelopment dependencies: \n{self.lista(self.dev_dependencies)}"
        )
