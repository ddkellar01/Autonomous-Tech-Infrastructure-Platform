import yaml

class RayClusterConfigurator:
    def __init__(self, cluster_name="ray-tpu-cluster"):
        self.cluster_name = cluster_name

    def generate_manifest(self, filepath="config/raycluster-tpu.yaml"):
        manifest = {
            "apiVersion": "ray.io/v1",
            "kind": "RayCluster",
            "metadata": {"name": self.cluster_name},
            "spec": {
                "rayVersion": "2.35.0",
                "headGroupSpec": {"rayStartParams": {"dashboard-host": "0.0.0.0"}},
                "workerGroupSpecs": [{
                    "groupName": "tpu-workers",
                    "replicas": 4,
                    "rayStartParams": {}
                }]
            }
        }
        with open(filepath, "w") as f:
            yaml.dump(manifest, f)
        return filepath
