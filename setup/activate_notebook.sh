EXP_CONDA_VER=4.8.3

INSTALL_PREFIX=$HOME/miniconda-$EXP_CONDA_VER
SOURCE_SCRIPT="$HOME/miniconda-$EXP_CONDA_VER/etc/profile.d/conda.sh"

source $SOURCE_SCRIPT
conda activate aces_metrics
jupyter notebook
