import abc
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as pltcolors
from typing import Tuple

class ComplexFunction(abc.ABC):
    """
    Abstract base class for defining and visualizing complex functions.
    """

    def __init__(self, resolution: int = 500, 
                 real_range: Tuple[float, float] = (-1000, 1000), 
                 imag_range: Tuple[float, float] = (-1000, 1000),
                 **kwargs):
        """
        Initialize the complex function visualizer.

        Args:
            resolution: Number of points for 2D plots (Bode).
            real_range: Tuple (min, max) for the real axis.
            imag_range: Tuple (min, max) for the imaginary axis (frequency).
        """
        self.resolution = resolution
        self.real_range = real_range
        self.imag_range = imag_range

    @abc.abstractmethod
    def f(self, s: complex) -> complex:
        """
        The complex function f(s) to be implemented by subclasses.
        Must be an instance method to allow access to self (state).
        """
        pass

    @staticmethod
    def module(s: complex) -> float:
        """Returns the magnitude (absolute value) of the complex number."""
        return np.abs(s)

    @staticmethod
    def phase(s: complex) -> float:
        """
        Returns the phase angle of the complex number in radians.
        Uses np.angle (equivalent to arctan2) to cover the full (-pi, pi) range.
        """
        return np.angle(s)

    def _ensure_array(self, output: any, input_shape: tuple) -> np.ndarray:
        """
        Helper to broadcast scalar outputs (e.g., return 1) to the input array shape.
        """
        if np.isscalar(output) or np.ndim(output) == 0:
            return np.full(input_shape, output)
        return output

    def plot_bode(self, cut: float = 0.0) -> None:
        """
        Generates a 2D Bode plot (Magnitude and Phase vs Frequency).
        
        Args:
            cut: The real part value at which to slice the complex plane (s = cut + jw).
        """
        freq = np.linspace(self.imag_range[0], self.imag_range[1], self.resolution)
        full_domain = cut + 1j * freq

        # Calculate function values
        f_jw = self.f(full_domain)
        
        # Handle constant functions (e.g. return 1)
        f_jw = self._ensure_array(f_jw, full_domain.shape)
        
        # Calculate module and phase
        mag = self.module(f_jw)
        phase = self.phase(f_jw)

        plt.figure(figsize=(9.6, 10))

        # Magnitude Plot
        plt.subplot(2, 1, 1)
        plt.title("Bode Plot")
        plt.ylabel("Magnitude")
        plt.grid(True, which="both", ls="-", alpha=0.6)
        plt.plot(freq, mag, color="black")

        # Phase Plot
        plt.subplot(2, 1, 2)
        plt.ylabel("Phase (rad)")
        plt.xlabel("Frequency (Im[s])")
        plt.grid(True, which="both", ls="-", alpha=0.6)
        plt.plot(freq, phase, color="black")

        plt.tight_layout()
        plt.show()

    def plot_laplace(self, mesh_resolution: int = 50) -> None:
        """
        Generates a 3D surface plot of the function's magnitude over the complex plane.

        Args:
            mesh_resolution: Grid size for the 3D mesh (default 50 for performance). 
                             Higher values give smoother plots but are slower.
        """
        # Use specific mesh resolution for 3D plot to avoid rendering lag
        real_domain = np.linspace(self.real_range[0], self.real_range[1], mesh_resolution)
        freq = np.linspace(self.imag_range[0], self.imag_range[1], mesh_resolution)
        
        real_part, imag_part = np.meshgrid(real_domain, freq)
        full_domain = real_part + 1j * imag_part

        f_s = self.f(full_domain)
        
        # Handle constant functions
        f_s = self._ensure_array(f_s, full_domain.shape)

        mag = self.module(f_s)
        # Calculate phase for coloring
        phase = self.phase(f_s)

        fig = plt.figure(figsize=(10, 10))
        ax = fig.add_subplot(111, projection="3d")

        # Normalize phase to map to colormap (-pi to pi)
        norm = pltcolors.Normalize(vmin=-np.pi, vmax=np.pi)
        colors = plt.cm.viridis(norm(phase)) 

        ax.plot_surface(real_part, imag_part, mag, 
                        facecolors=colors, rstride=1, cstride=1, 
                        linewidth=0.1, antialiased=True, shade=False)

        # Colorbar setup
        mappable = plt.cm.ScalarMappable(cmap='viridis', norm=norm)
        mappable.set_array([])
        cbar = fig.colorbar(mappable, ax=ax, shrink=0.5, pad=0.1)
        cbar.set_ticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi])
        cbar.set_ticklabels([r"$-\pi$", r"$-\frac{\pi}{2}$", r"$0$", r"$\frac{\pi}{2}$", r"$\pi$"])
        cbar.set_label('Phase (rad)')

        ax.set_xlabel(r"Real part ($\sigma$)")
        ax.set_ylabel(r"Imaginary part ($j\omega$)")
        ax.set_zlabel("Magnitude")

        plt.show()
