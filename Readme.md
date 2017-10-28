# Buildkite Python Example (using pipenv)

[![Add to Buildkite](https://buildkite.com/button.svg)](https://buildkite.com/new)

This repository is an example on how to test a [Python](https://python.org) project using [Buildkite](https://buildkite.com/) and [pipenv](https://github.com/kennethreitz/pipenv).

Note: this example assumes your Buildkite Agent machine has Python and pipenv already instealled. See the [Python Docker Example](https://github.com/buildkite/python-docker-example) for running your Python project on any agent machine that has only Docker installed.

## How does it work?

The [pipeline.yml](.buildkite/pipeline.yml) installs your dependencies and runs [py.test](https://github.com/pytest-dev/pytest):

```yml
steps:
  - label: ":python: Test"
    commands:
      - pipenv install --deploy
      - pipenv run py.test
```

## License

See [Licence.md](Licence.md) (MIT)