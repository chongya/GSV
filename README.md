# GSV
GSV (general spectral vectors) is an empirical model for hyperspectral soil reflectance simulation

Jiang, C., & Fang, H. (2019). GSV: a general model for hyperspectral soil reflectance simulation. International Journal of Applied Earth Observation and Geoinformation, 83(July), 101932. https://doi.org/10.1016/j.jag.2019.101932

###############################################################################

GSV simulates hyperspectral soil reflectance (400–2500nm) using the formula below:

ρ(λ) = c_1*V_1(λ) + c_2*V_2(λ) + c_3*V3(λ) + c_SM*V_SM(λ)    (1)

λ: spectral wavelength
V_1(λ): the 1st dry soil spectral vector
V_2(λ): the 2nd dry soil spectral vector
V_3(λ): the 3rd dry soil spectral vector
V_SM(λ): the soil moisture spectral vector
c_1: the 1st dry soil coefficient
c_2: the 2nd dry soil coefficient
c_3: the 3rd dry soil coefficient
c_SM: the soil moisture coefficient

V_1(λ), V_2(λ), V_3(λ), and V_SM(λ) have been derived from global dry and humid soil reflectance databases including 23,871 soil spectra. As a user, you do not need to derive them by yourself. Just use what we have provided in this repository. 

c_1, c_2, c_3, and c_SM are free parameters. As a user, you have to set their values by yourself. If you have a multispectral soil reflectance, then you can fit those parameters using the above equation (1). For example, if you have Landsat 8 bare soil reflectance at 480nm, 560nm, 650nm, 860nm, 1610nm, and 2200nm, then you have six known values of ρ(λ) to solve the four unknown c parameters from the multivariate linear equations:

ρ(480nm) = c_1*V_1(480nm) + c_2*V_2(480nm) + c_3*V3(480nm) + c_SM*V_SM(480nm)
ρ(560nm) = c_1*V_1(560nm) + c_2*V_2(560nm) + c_3*V3(560nm) + c_SM*V_SM(560nm)
ρ(650nm) = c_1*V_1(650nm) + c_2*V_2(650nm) + c_3*V3(650nm) + c_SM*V_SM(650nm)
ρ(860nm) = c_1*V_1(860nm) + c_2*V_2(860nm) + c_3*V3(860nm) + c_SM*V_SM(860nm)
ρ(1610nm) = c_1*V_1(1610nm) + c_2*V_2(1610nm) + c_3*V3(1610nm) + c_SM*V_SM(1610nm)
ρ(2200nm) = c_1*V_1(2200nm) + c_2*V_2(2200nm) + c_3*V3(2200nm) + c_SM*V_SM(2200nm)

Once you estimate c_1, c_2, c_3, and c_SM from linear regression, you can reconstruct hyperspectral soil reflectance using the above equation (1).

###############################################################################

Files of spectral vectors:

MD.vec.txt: dry soil spectral vectors (V_1(λ), V_2(λ), V_3(λ)) derived using a matrix decomposition method. Recommanded and examples can be found in Table 3 and Fig.8 in (Jiang and Fang, 2019).
BR.vec.txt: dry soil spectral vectors (V_1(λ), V_2(λ), V_3(λ)) derived using a band regression method. 
SA.vec.txt: dry soil spectral vectors (V_1(λ), V_2(λ), V_3(λ)) derived using a successive approximation method. 
SM.vec.txt: soil moisture spectral vector (V_SM(λ)).

MD.vec.txt, BR.vec.txt and SA.vec.txt are 3 x 211 matrix, where 3 rows refer to V_1(λ), V_2(λ), and V_3(λ), respectively, and 211 columns refer to 211 wavelengths (400–2500nm with 10nm interval).

###############################################################################

You can refer to Example.py or test1.m and test2.m.
