import overrides
import numpy as np
from grafical import ComplexFunction

class EulerFunction(ComplexFunction):
    # 1. Remove @staticmethod from __init__
    # 2. Accept **kwargs to catch resolution, real_range, etc.
    def __init__(self, a: complex, **kwargs):
        # Pass the configuration arguments to the parent class
        super().__init__(**kwargs)
        self.a = a

    # 3. Remove @staticmethod because we need 'self' to access 'self.a'
    @overrides.overrides
    def f(self, s: complex) -> complex:
        return 1 / (s - self.a)

def main():
    # 4. Pass the required argument 'a' (the pole location)
    f_instance = EulerFunction(
        a=2.0,  # The pole is at s = 2
        resolution=1000, 
        real_range=(-10, 10), 
        imag_range=(-10, 10)
    )
    
    print("Plotting Bode...")
    f_instance.plot_bode()
    
    print("Plotting Laplace Surface...")
    f_instance.plot_laplace(mesh_resolution=60)

if __name__ == "__main__":
    main()
