import yaml

class KServeDeployer:
    def __init__(self, model_name="ai-model", image_uri="docker.io/credkellar/model:v1"):
        self.model_name = model_name
        self.image_uri = image_uri

    def generate_manifest(self, filepath="config/inferenceservice.yaml"):
        manifest = {
            "apiVersion": "serving.kserve.io/v1beta1",
            "kind": "InferenceService",
            "metadata": {"name": self.model_name},
            "spec": {
                "predictor": {
                    "model": {
                        "modelFormat": {"name": "pytorch"},
                        "storageUri": self.image_uri
                    }
                }
            }
        }
        with open(filepath, "w") as f:
            yaml.dump(manifest, f)
        return filepath
