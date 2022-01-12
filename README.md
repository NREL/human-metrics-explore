# Human metrics exploration

This is a set of notebooks to support exploring human centered metrics. You can explore the metrics interactively using the `Interactive_Metrics` juypter notebook.

# Quick start

Run in your browser without any setup using binder.

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/NREL/human-metrics-explore.git/HEAD)

[![interactive-metrics-test-binder](https://github.com/NREL/human-metrics-explore/actions/workflows/interactive-metrics-test-binder.yml/badge.svg)](https://github.com/NREL/human-metrics-explore/actions/workflows/interactive-metrics-test-binder.yml)

## Manual install

[![exploratory-notebook-test-osx](https://github.com/NREL/human-metrics-explore/actions/workflows/interactive-metrics-test-osx.yml/badge.svg)](https://github.com/NREL/human-metrics-explore/actions/workflows/interactive-metrics-test-osx.yml)

This is primarily needed if you want to modify or extend the analysis.
This repo has Continous Integration (CI) enabled. So if any of these steps
fail:
- please compare your environment and output against CI and bring them into alignment
- if that also fails, please **file an issue** with the output of each CI step in your environment.

#### One-time installation

```
$ source setup/setup_notebook.sh
```

Follow any subsidiary instructions and re-run until the command succeeds.

#### Start the notebook (every time)

```
$ source setup/activate_notebook.sh
```

Your browser will have a listing of this directory. Open and run the
[Interactive_Metrics.ipynb](Interactive_Metrics.ipynb) file to experiment with
the metrics.

#### One-time uninstall

```
$ source setup/teardown.sh
```

If you want to uninstall the current conda version as well

```
$ source setup/teardown_conda.sh
```

#### Testing

```
$ python bin/run_notebooks.py *.ipynb
```
