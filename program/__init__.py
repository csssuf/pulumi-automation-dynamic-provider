import pulumi

from program.provider import BlankDynamicResource


def main():
    pulumi.info("Constructing resource")
    BlankDynamicResource("test")
