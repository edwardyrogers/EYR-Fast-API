Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\venv\Scripts\Activate.ps1


autoflake --remove-unused-variables --remove-all-unused-imports --recursive --in-place .
isort .
black .
