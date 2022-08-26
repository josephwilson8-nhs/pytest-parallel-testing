# pytest-parallel-testing

Small little repository to test out pytest-parallel running on a remote machine

## Setting up

If you haven't already, [create a person access token for GitHub](https://github.com/settings/tokens) to enable access to clone down the repository.

Clone repository:

``` bash
git clone https://github.com/josephwilson8-nhs/pytest-parallel-testing.git
```

Create a conda environment:

``` bash
conda create -n parallel-test python=3.9
conda activate parallel-test
```

``` bash
pip install --upgrade pip setuptools==57.5.0
pip install -r requirements.txt
```

## Running the tests

In VSCode, bring up the command pallet with `Ctrl+Shift+P` and type `Python: Select Interpreter`. Select the `Python 3.9.12 ('parallel-test')` interpreter or type `~/anaconda3/envs/parallel-test/bin/python`. Then select the relevant launch configuration from the Run and Debug side menu and run it, `Ctrl+F5`.

Alternative, you can run the test manually from the Bash Prompt.

### In parallel

In the bash prompt while in the `~/pytest-parallel-testing` folder and the `parallel-test` conda environment activated:

``` bash
python -m pytest --tests-per-worker auto
```

This should take a little over 5 seconds to run.

### In series

In the bash prompt while in the `~/pytest-parallel-testing` folder and the `parallel-test` conda environment activated:

``` bash
python -m pytest
```

This should take a little over 60 seconds to run.
