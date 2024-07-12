import pandas as pd
from IPython import get_ipython

def display_dataframe_to_user(name: str, dataframe: pd.DataFrame) -> None:
    """
    This function is used to visually present a pandas DataFrame to the user.

    Parameters:
    name (str): The name/title of the DataFrame.
    dataframe (pd.DataFrame): The DataFrame to be displayed.
    """
    # Check if running in a Jupyter notebook
    if get_ipython() is not None and 'IPKernelApp' in get_ipython().config:
        from itables import show
        print(f"{name}")
        show(dataframe)
    else:
        print(f"{name}")
        print(dataframe)