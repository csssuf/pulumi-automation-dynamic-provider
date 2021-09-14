from pulumi import automation

from program import main


project_settings = automation.ProjectSettings("myproject", runtime="python")
stack = automation.create_or_select_stack(
    stack_name="mystack",
    project_name="myproject",
    program=main,
    opts=automation.LocalWorkspaceOptions(
        project_settings=project_settings,
    ),
)
stack.preview(on_output=print, diff=True)
