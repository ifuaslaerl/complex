# Grafical

**Grafical** is a Python tool for visualizing complex functions. It generates:
- **Bode Plots**: 2D frequency response (Magnitude and Phase).
- **Laplace Surfaces**: 3D visualizations of magnitude over the complex plane, colored by phase.

## Installation

Requires Python 3.9+.

```bash
pip install .
```

## Creating Your Own Functions

To create a new function, inherit from `ComplexFunction` and implement the `f` method. Note that `f` is now an instance method and must accept `self`.

```python
import overrides
from grafical import ComplexFunction

class MyFunction(ComplexFunction):
    @overrides.overrides
    def f(self, s: complex) -> complex:
        # Example: 1 / (s + 1)
        return 1 / (s + 1)

if __name__ == "__main__":
    # Instantiate the function with defined resolution
    func = MyFunction(resolution=1000, real_range=(-10, 10), imag_range=(-10, 10))
    
    # Generate the plots
    func.plot_bode()
    func.plot_laplace(mesh_resolution=60)
```

## Project Structure

- `src/grafical/core.py`: Base class `ComplexFunction` and plotting logic.
