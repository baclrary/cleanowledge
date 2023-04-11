# Cleanowledge

My own study platform project built with Django


## Installation

Use the package manager [pipenv](https://pipenv.pypa.io/en/stable/) to install dependencies:
```bash
pipenv install
```
> **_NOTE:_** append --dev to the above command to install dev packages.

## Configuration

Create .env file from template:
```bash
cp .env.example .env
```

### Change environment

```
# for prod
DJANGO_SETTINGS_MODULE=studyplatform.settings

# for dev
DJANGO_SETTINGS_MODULE=studyplatform.dev_settings
```
