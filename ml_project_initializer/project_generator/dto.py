from typing import List


class GenerateProjectRequestDTO:
    def __init__(self, project_name: str, description: str, package_manager: str, model_type: str, packages: List[str]):
        self.project_name = project_name
        self.description = description
        self.package_manager = package_manager
        self.model_type = model_type
        self.packages = packages
