EXP_CONDA_VER=4.8.3

INSTALL_PREFIX=$HOME/miniconda-$EXP_CONDA_VER
SOURCE_SCRIPT="$HOME/miniconda-$EXP_CONDA_VER/etc/profile.d/conda.sh"

if [ -f $SOURCE_SCRIPT ]; then
    echo "Found $SOURCE_SCRIPT, all is good!"
    source $SOURCE_SCRIPT
else
    echo "$SOURCE_SCRIPT not found, run 'bash setup/setup_conda.sh $EXP_CONDA_VER <platform>' to get the correct version"
    echo "Or install manually after downloading from https://repo.anaconda.com/miniconda/"
fi

