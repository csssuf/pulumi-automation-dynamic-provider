from pulumi import dynamic
import pulumi


class BlankDynamicProvider(dynamic.ResourceProvider):
    def create(self, props) -> dynamic.CreateResult:
        return dynamic.CreateResult(props["name"], {})


class BlankDynamicResource(dynamic.Resource):
    def __init__(self, name: str, opts: pulumi.ResourceOptions = None):
        super().__init__(BlankDynamicProvider(), name, {"name": name}, opts)


def main():
    resource = BlankDynamicResource("test")
