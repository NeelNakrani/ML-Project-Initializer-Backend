from typing import List


class GenerateProjectRequestDTO:
    def __init__(self, project_name: str, description: str, package_manager: str, model_type: str, packages: List[str]):
        self.project_name = project_name
        self.description = description
        self.package_manager = package_manager
        self.model_type = model_type
        self.packages = packages

    @staticmethod
    def validate(data) -> "GenerateProjectRequestDTO":
        print(data)
        required_fields = ['projectName', 'description','packageManager', 'modelType', 'packages']

        for field in required_fields:
            if field not in data:
                raise ValueError(f"Missing required field: {field}")

        return GenerateProjectRequestDTO(
            project_name=data['projectName'],
            description=data['description'],
            package_manager=data['packageManager'],
            model_type=data['modelType'],
            packages=data['packages']
        )