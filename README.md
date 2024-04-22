# Ensure venv pre-commit hook

A [pre-commit](https://pre-commit.com/) hook that ensures the Python virtual environment is activated.

## Use case

You have your own `.pre-commit-config.yaml' configuration with specified `repo: local' hooks that run locally installed linters and code formatters, i.e. `flake8`, `ruff`, `isort`, `mypy`, etc.

```yaml
-   repo: local
    hooks:
    -   id: mypy
        name: Type check (mypy)
        entry: mypy
        args: [--config-file, mypy.ini, app/, core/, main.py]
        types: [python]
        require_serial: true
        always_run: true
        language: system
        pass_filenames: false
```

You may want to ensure that the `mypy' executable used in the pre-commit hook is the one installed locally in your project's virtual environment, not the one taken from the global site-packages. You can use the `ensure-venv` hook to do this:

```yaml
-   repo: https://github.com/diachkow/ensure-venv-pre-commit
    rev: v1.0.0
    hooks:
    -   id: ensure-venv
```

You must place this hook before any `repo: local' hooks that need to use the locally installed executable. The final configuration will look like this

```yaml
# ... other non-local hooks ...
-   repo: https://github.com/diachkow/ensure-venv-pre-commit
    rev: v1.0.0
    hooks:
    -   id: ensure-venv
-   repo: local
    hooks:
    -   id: mypy
        name: Type check (mypy)
        entry: mypy
        args: [--config-file, mypy.ini, app/, core/, main.py]
        types: [python]
        require_serial: true
        always_run: true
        language: system
        pass_filenames: false
# ... other non-local hooks ...
```

If the virtual environment is not enabled, the pre-commit will fail fast at the `ensure-venv` step and will not run the `mypy`, giving you an error telling you to enable your virtual environment.
