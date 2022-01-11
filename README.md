# Human metrics exploration

This is a set of notebooks to support exploring human centered metrics. Until we publish this externally, in which case it can be run using binder, you will have to run this locally.

## One-time installation

```
$ source setup/setup_notebook.sh
```

Follow any subsidiary instructions and re-run until the command succeeds.

## Start the notebook (every time)

```
$ source setup/activate_notebook.sh
```

Your browser will have a listing of this directory. Open and run the
[Interactive_Metrics.ipynb](Interactive_Metrics.ipynb) file to experiment with
the metrics.

## One-time uninstall

```
$ source setup/teardown.sh
```

If you want to uninstall the current conda version as well

```
$ source setup/teardown_conda.sh
```

## Testing

```
$ python bin/run_notebooks.py *.ipynb
```
