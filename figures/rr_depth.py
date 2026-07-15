'''
Copied from: https://doi.org/10.5281/zenodo.7425649
https://github.com/amsikking/any_immersion_remote_refocus_microscopy/
blob/main/figures/sf_and_rr_depth/sf_and_rr_depth.py
'''

import numpy as np

# Remote refocus depth:
def rr_depth(m, na, n_s, lambda_um):
    f_um = 1000 * 200 / m # objective focal length (200mm tube lens)
    na = np.where(na <= n_s, na, n_s) # limit na <= b_bio
    theta_s = np.arcsin(na / n_s)
    a = 1 / (2 * np.sin(theta_s/2)**2)
    b = 15*lambda_um**2 * f_um**2 * (3 + 8*np.cos(theta_s) + np.cos(2*theta_s))
    c = np.pi**2 * n_s**2 * (3 + 16*np.cos(theta_s) + np.cos(2*theta_s))
    z_rr_max_um = a * (b / c)**0.25
    return z_rr_max_um

# Nikon 20x1.0 water objective
print('z_rr_max_um = %0.2f'%rr_depth(m=20, na=1.00, n_s=1.33, lambda_um=0.532))

# z_rr_max_um = 181.92

# Nikon 20x0.95 water objective
print('z_rr_max_um = %0.2f'%rr_depth(m=20, na=0.95, n_s=1.33, lambda_um=0.532))

# z_rr_max_um = 206.35
