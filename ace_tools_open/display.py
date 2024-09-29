import pandas as pd
from IPython import get_ipython
import matplotlib.pyplot as plt
from io import BytesIO
from PIL import Image

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

def display_matplotlib_image_to_user(title: str, reason: str, exception_ids: list):
    """
    Capture the current Matplotlib figure and display it to the user with a title and reason.
    This example saves the figure to a buffer, converts it to an image, and then displays it.
    
    Args:
        title (str): The title for the image display.
        reason (str): The reason or context for the display.
        exception_ids (list): Any specific exceptions or IDs to handle (not used in this basic example).
    """
    # Save the current figure to a buffer
    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    
    # Convert the buffer to an image and display it
    img = Image.open(buf)
    # check if in Jupyter notebook
    if get_ipython() is not None and 'IPKernelApp' in get_ipython().config:
        # disable plt.show() to avoid double display
        plt.close()
        from IPython.display import display
        display(img)
    else:
        img.show()
    
    print(f"Displaying image: {title}")
    print(f"Reason: {reason}")
    if exception_ids:
        print(f"Exceptions handled: {exception_ids}")
    
    buf.close()

def display_chart_to_user(path, title, chart_type='line'):
    # load figure from path and display
    img = Image.open(path)
    # check if in Jupyter notebook
    if get_ipython() is not None and 'IPKernelApp' in get_ipython().config:
        # disable plt.show() to avoid double display
        plt.close()
        from IPython.display import display
        display(img)
        print(f"{title}")
    else:
        img.show(title=title)