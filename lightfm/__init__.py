try:
    __LIGHTFM_SETUP__
except NameError:
    from .lightfm import LightFM

__version__ = '1.14'

__all__ = ['LightFM', 'datasets', 'evaluation']
