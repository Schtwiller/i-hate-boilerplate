from pathlib import Path
import subprocess
import sys

import typer

app = typer.Typer(help="i-hate-boilerplate CLI")


def generate_project(
    name: str,
    project_type: str,
    framework: str,
    model: str,
    aug: bool,
    wandb: bool,
    git: bool,
    docker: bool,
    license: bool,
    venv: bool,
):
    """Generate a minimal ML project skeleton."""

    project_path = Path(name)

    # Basic directories
    for sub in ["data", "models", "src", "configs"]:
        (project_path / sub).mkdir(parents=True, exist_ok=True)

    # README
    (project_path / "README.md").write_text(
        f"# {name}\n\nGenerated with i-hate-boilerplate."
    )

    # gitignore
    (project_path / ".gitignore").write_text("__pycache__/\n*.pyc\nvenv/\n")

    # Training script stub
    train_file = project_path / "src" / "train.py"
    if framework == "pytorch":
        train_file.write_text(
            """import torch\n\n\ndef main():\n    pass  # TODO: implement training\n\n\nif __name__ == '__main__':\n    main()\n"""
        )
    else:
        train_file.write_text(
            """import tensorflow as tf\n\n\ndef main():\n    pass  # TODO: implement training\n\n\nif __name__ == '__main__':\n    main()\n"""
        )

    # Config file
    config_content = (
        f"project_type: {project_type}\n"
        f"framework: {framework}\n"
        f"model: {model}\n"
        f"augmentation: {aug}\n"
        f"wandb: {wandb}\n"
    )
    (project_path / "configs" / "config.yaml").write_text(config_content)

    if aug:
        (project_path / "src" / "augmentations.py").write_text(
            "# Add augmentation functions here\n"
        )

    if wandb:
        (project_path / "configs" / "wandb.yaml").write_text(
            "project: my-awesome-project\n"
        )

    if git:
        subprocess.run(["git", "init"], cwd=project_path)

    if docker:
        (project_path / "Dockerfile").write_text(
            "FROM python:3.10-slim\nWORKDIR /app\nCOPY . /app\n"
        )

    if license:
        (project_path / "LICENSE").write_text(
            "MIT License\n\n<your license text here>\n"
        )

    if venv:
        subprocess.run([sys.executable, "-m", "venv", "venv"], cwd=project_path)


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
    docker: bool = typer.Option(False, "--docker", help="Include a Dockerfile"),
    license: bool = typer.Option(False, "--license", help="Add an MIT license"),
    venv: bool = typer.Option(False, "--venv", help="Create a Python venv"),
):
    """Create a new project with the specified options."""
    if framework == "tensorflow" and model == "resnet50":
        typer.secho(
            "Warning: using resnet50 with tensorflow is not recommended.",
            fg=typer.colors.YELLOW,
        )

    typer.echo("Project configuration:")
    typer.echo(f"  Name      : {project_name}")
    typer.echo(f"  Type      : {type}")
    typer.echo(f"  Framework : {framework}")
    typer.echo(f"  Model     : {model}")
    typer.echo(f"  Augment   : {aug}")
    typer.echo(f"  W&B       : {wandb}")
    typer.echo(f"  Git       : {git}")
    typer.echo(f"  Docker    : {docker}")
    typer.echo(f"  License   : {license}")
    typer.echo(f"  Venv      : {venv}")

    generate_project(
        name=project_name,
        project_type=type,
        framework=framework,
        model=model,
        aug=aug,
        wandb=wandb,
        git=git,
        docker=docker,
        license=license,
        venv=venv,
    )


if __name__ == "__main__":
    app()
