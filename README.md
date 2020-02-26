# vpype-text

Plug-in for [vpype](https://github.com/abey79/vpype) to generate text with stroke fonts (a.k.a.
[Hershey fonts](https://en.wikipedia.org/wiki/Hershey_fonts)). This plug-in is implemented as a thin wrapper on
Michael Fogleman's [axi](https://github.com/fogleman/axi) project.

Currently, a variety of fonts are supported, as well as control on alignment (left, right, center). Multi-line text or
wrapping is not (yet?) supported.


## Examples

_to be completed_


## Installation

See the [installation instructions](https://github.com/abey79/vpype/blob/master/INSTALL.md) for information on how
to install `vpype`.


### Existing `vpype` installation

Use this method if you have an existing `vpype` installation (typically in an existing virtual environment) and you
want to make this plug-in available. You must activate your virtual environment beforehand.

```bash
$ pip install git+https://github.com/abey79/vpype-text.git#egg=vpype-text
```

Check that your install is successful:

```
$ vpype --help
Usage: vpype [OPTIONS] COMMAND1 [ARGS]... [COMMAND2 [ARGS]...]...

Options:
  -v, --verbose
  -I, --include PATH  Load commands from a command file.
  --help              Show this message and exit.

Commands:
[...]
  Plugins:
    text
[...]
```

### Stand-alone installation

Use this method if you want to edit this project. First, clone the project:

```bash
$ git clone https://github.com/abey79/vpype-text.git
$ cd vpype-text
```

Create a virtual environment:

```bash
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install --upgrade pip
```

Install `vpype-text` and its dependencies (including `vpype`):

```bash
$ pip install -e .
```

Check that your install is successful:

```
$ vpype --help
Usage: vpype [OPTIONS] COMMAND1 [ARGS]... [COMMAND2 [ARGS]...]...

Options:
  -v, --verbose
  -I, --include PATH  Load commands from a command file.
  --help              Show this message and exit.

Commands:
[...]
  Plugins:
    text
[...]
```


## Documentation

The complete plug-in documentation is available directly in the CLI help:

```bash
$ vpype text --help
```


## License

See the [LICENSE](LICENSE) file for details.