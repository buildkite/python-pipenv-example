# Buildkite Python (pipenv) Example

[![Build status](https://badge.buildkite.com/f685180f6d059ee86697f997693e43237baebe1d0044707587.svg?branch=main)](https://buildkite.com/buildkite/python-pipenv-example/builds/latest?branch=main)
[![Add to Buildkite](https://img.shields.io/badge/Add%20to%20Buildkite-14CC80)](https://buildkite.com/new)

This repository is an example [Buildkite](https://buildkite.com/) pipeline that tests a [Python](https://python.org) project using [pipenv](https://github.com/kennethreitz/pipenv).

👉 **See this example in action:** [buildkite/python-pipenv-example](https://buildkite.com/buildkite/python-pipenv-example/builds/latest?branch=main)

See the full [Getting Started Guide](https://buildkite.com/docs/guides/getting-started) for step-by-step instructions on how to get this running, or try it yourself:

[![Add to Buildkite](https://buildkite.com/button.svg)](https://buildkite.com/new)

<a href="https://buildkite.com/buildkite/python-pipenv-example/builds/latest?branch=main">
  <img width="2400" alt="Screenshot of Buildkite Python pipenv example pipeline" src=".buildkite/screenshot.png" />
</a>

<!-- docs:start -->

## How it works

This example:
- Assumes Python and pipenv are installed on the agent
- Installs dependencies with `pipenv install --deploy --dev`
- Runs tests using `pipenv run py.test`

Example pipeline step:
```yml
steps:
  - label: ":python: Test"
    commands:
      - pipenv install --deploy --dev
      - pipenv run py.test
```

> 💡 Looking for a Docker-based setup instead? Check out the [Python Docker Example](https://github.com/buildkite/python-docker-example).

<!-- docs:end -->

## License

See [LICENSE](LICENSE) (MIT)
