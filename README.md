# Cleanowledge

[![Linters](https://github.com/baclrary/cleanowledge/actions/workflows/linters.yml/badge.svg)](https://github.com/baclrary/cleanowledge/actions/workflows/linters.yml)

My own study platform project built with Django

## Table of Contents
- [Installation](#installation)
- [Configuration](#configuration)
  * [Change environment](#change-environment)
  * [Add pre-commit hooks](#add-pre-commit-hooks)
- [Usage](#usage)

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

### Add pre-commit hooks

Run the following command to add pre-commit hooks:
```bash
pipenv run pre-commit install
```
> **_NOTE:_** dev dependencies should be installed for this to work properly

## Usage

Start server:
```bash
pipenv run dev-server
```
