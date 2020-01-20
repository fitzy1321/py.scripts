conda env create -f environment.yml

conda activate pycon2019
# Add jupytertheme to make jupyter visually appealing
pip install -U jupyterthemes

# set monokai theme and include tool bar and name bar
jt -t monokai -T -N

# modified to work on windows 10 laptop
npm install cross-env
cross-env NODE_OPTIONS=--max_old_space_size=4096 jupyter labextension install @jupyter-widgets/jupyterlab-manager jupyter-threejs ipyvolume bqplot @jupyterlab/geojson-extension @jupyterlab/fasta-extension

jupyter lab build

# Optional extensions

conda install -c conda-forge --override-channels --yes ipyleaflet ipympl
pip install sidecar
NODE_OPTIONS=--max_old_space_size=4096 jupyter labextension install jupyterlab-toc jupyter-leaflet @jupyter-widgets/jupyterlab-sidecar jupyterlab-drawio
