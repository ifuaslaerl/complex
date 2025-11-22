import overrides
from grafical import ComplexFunction

class impulseFunction(ComplexFunction):
    @staticmethod
    @overrides.overrides
    def f(s: complex) -> complex:
        return 1 

def main():
    # Instantiate the function
    # Note: You can adjust ranges here if needed, e.g., real_range=(-10, 10)
    f_instance = impulseFunction(resolution=1000, real_range=(-20, 20), imag_range=(-20, 20))
    
    print("Plotting Bode...")
    f_instance.plot_bode()
    
    print("Plotting Laplace Surface...")
    f_instance.plot_laplace(mesh_resolution=60)

if __name__ == "__main__":
    main()
