# i-hate-boilerplate

i-hate-boilerplate is a command-line tool for instantly scaffolding machine learning projects. It sets up everything you need—folders, training scripts, config files, and a README—so you can skip the setup and get straight to the good stuff (or the debugging).

## Usage

The CLI exposes a `create` command which generates a project skeleton:

```bash
python ihb.py create <project_name> \
  --type <cv|nlp|tabular> \
  --framework <pytorch|tensorflow> \
  --model <resnet50|vit|bert|custom> \
  --aug --wandb --git --docker --license --venv
```

All options are optional except `project_name`. Flags such as `--aug`, `--wandb` and `--git` enable data augmentation, W&B logging and git initialization respectively. Additional flags like `--docker`, `--license` and `--venv` can set up a Dockerfile, add an MIT license and create a Python virtual environment for you.

The tool now generates a more complete project structure:

```
<project_name>/
├── README.md
├── Dockerfile (optional)
├── LICENSE     (optional)
├── .gitignore
├── data/
├── models/
├── src/
│   ├── train.py
│   └── augmentations.py (optional)
└── configs/
    ├── config.yaml
    └── wandb.yaml (optional)
```
