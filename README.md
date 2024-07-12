# ace_tools_open
Open implementation of ace_tools referenced in GPT4o.

## Installation

```bash
pip install ace_tools_open
```

## Usage
Just copy the output of GPT4o that uses ace_tools and paste it in your code. Then replace all the `ace_tools` imports with `ace_tools_open`. The code should work as expected.

## Example
```python
import pandas as pd
import numpy as np

# Generate a random pandas dataframe
np.random.seed(0)
data = {
    'A': np.random.rand(10),
    'B': np.random.rand(10),
    'C': np.random.randint(1, 100, 10),
    'D': np.random.choice(['X', 'Y', 'Z'], 10)
}

df = pd.DataFrame(data)
import ace_tools_open as tools; tools.display_dataframe_to_user(name="Random DataFrame", dataframe=df)
```