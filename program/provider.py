from pulumi import dynamic
import pulumi


class BlankDynamicProvider(dynamic.ResourceProvider):
    def __init__(self):
        pulumi.info("Constructing dynamic provider")

    def create(self, props) -> dynamic.CreateResult:
        return dynamic.CreateResult(props["name"], {})


class BlankDynamicResource(dynamic.Resource):
    def __init__(self, name: str, opts: pulumi.ResourceOptions = None):
        provider = BlankDynamicProvider()

        super().__init__(provider, name, {"name": name}, opts)
