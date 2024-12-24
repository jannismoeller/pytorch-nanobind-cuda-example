# Pytorch - nanobind - CUDA example

A minimal demo of a Python project that uses scikit-build-core (CMAKE) to compile a CUDA extension that accepts pytorch tensors via nanobind's DLPack support.

## Build and install (basic)
```console
$ pip install .
```

## Build and install (editable)
```console
$ pip install scikit-build-core nanobind ninja
$ pip install -e . --no-build-isolation
```
The former being necessary, as a rebuild does not automatically collect the packages specified in `pyproject.toml` under [build-system] > requires.

## Test
```
$ python test.py
```
