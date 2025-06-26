# Buildkite Python (pipenv) Example

[![Build status](https://badge.buildkite.com/f685180f6d059ee86697f997693e43237baebe1d0044707587.svg?branch=main)](https://buildkite.com/buildkite/python-pipenv-example)
[![Add to Buildkite](https://img.shields.io/badge/Add%20to%20Buildkite-14CC80)](https://buildkite.com/new)

This repository is an example for testing a [Python](https://python.org) project using [Buildkite](https://buildkite.com/) and [pipenv](https://github.com/kennethreitz/pipenv).

Note: this example assumes your Buildkite Agent machine has Python and pipenv already installed. See the [Python Docker Example](https://github.com/buildkite/python-docker-example) for running your Python project on any agent machine that has only Docker installed.

👉 **See this example in action:** [buildkite/python-pipenv-example](https://buildkite.com/buildkite/python-pipenv-example/builds/latest)

See the full [Getting Started Guide](https://buildkite.com/docs/guides/getting-started) for step-by-step instructions on how to get this running, or try it yourself:

[![Add to Buildkite](https://buildkite.com/button.svg)](https://buildkite.com/new)

<a href="https://buildkite.com/buildkite/python-pipenv-example/builds/latest?branch=main">
  <img width="2400" height="1600" alt="Screenshot of example pipeline build page" src=".buildkite/screenshot.png" />
</a>

## How does it work?

The [pipeline.yml](.buildkite/pipeline.yml) installs your dependencies and runs [py.test](https://github.com/pytest-dev/pytest):

```yml
steps:
  - label: ":python: Test"
    commands:
      - pipenv install --deploy --dev
      - pipenv run py.test
```

## License

See [LICENSE](LICENSE) (MIT)
