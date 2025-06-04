import typer
from pathlib import Path

app = typer.Typer(help="i-hate-boilerplate CLI")


def generate_project(*args, **kwargs):
    """Stub for project generation logic."""
    pass


@app.command()
def create(
    project_name: str = typer.Argument(..., help="Name of the project"),
    type: str = typer.Option("cv", "--type", help="Project type: cv | nlp | tabular"),
    framework: str = typer.Option(
        "pytorch", "--framework", help="Framework: pytorch | tensorflow"
    ),
    model: str = typer.Option(
        "resnet50",
        "--model",
        help="Model: resnet50 | vit | bert | custom",
    ),
    aug: bool = typer.Option(False, "--aug", help="Enable data augmentation"),
    wandb: bool = typer.Option(False, "--wandb", help="Include W&B logging"),
    git: bool = typer.Option(False, "--git", help="Initialize a git repo"),
):
    """Create a new project with the specified options."""
    if framework == "tensorflow" and model == "resnet50":
        typer.secho(
            "Warning: using resnet50 with tensorflow is not recommended.",
            fg=typer.colors.YELLOW,
        )

    project_path = Path(project_name)
    project_path.mkdir(parents=True, exist_ok=True)

    typer.echo("Project configuration:")
    typer.echo(f"  Name      : {project_name}")
    typer.echo(f"  Type      : {type}")
    typer.echo(f"  Framework : {framework}")
    typer.echo(f"  Model     : {model}")
    typer.echo(f"  Augment   : {aug}")
    typer.echo(f"  W&B       : {wandb}")
    typer.echo(f"  Git       : {git}")

    generate_project(
        name=project_name,
        project_type=type,
        framework=framework,
        model=model,
        aug=aug,
        wandb=wandb,
        git=git,
    )


if __name__ == "__main__":
    app()
