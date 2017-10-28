# Buildkite Ruby rbenv Example

[![Add to Buildkite](https://buildkite.com/button.svg)](https://buildkite.com/new)

This repository is an example on how to test a [Python](https://python.org) project using [Buildkite](https://buildkite.com/) and [pipenv](https://github.com/kennethreitz/pipenv).

## How does it work?

It uses a local agent environment hook in [.buildkite/hooks/environment](.buildkite/hooks/environment) to setup pipenv.

See the [agent hook documentation](https://buildkite.com/docs/agent/hooks) for more information on how agent hooks work.

## License

See [Licence.md](Licence.md) (MIT)