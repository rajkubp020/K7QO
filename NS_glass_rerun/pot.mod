# potential
pair_style      hybrid/overlay buck/coul/long 8.0 12.0 table linear 1180
pair_coeff      * * buck/coul/long 0.0 1.0 0.0
pair_coeff      1 3 buck/coul/long 101093.3472    0.243838  707.96963 #Na-O
pair_coeff      2 3 buck/coul/long 316001.3219145 0.193817  1260.9930729 #Si-O
pair_coeff      3 3 buck/coul/long 42541.49842    0.343645  4441.068122 #O-O
#pair_coeff      3 4 buck/coul/long 473370.4486    0.233708  1187.38268 #O-K
#pair_coeff      3 5 buck/coul/long 946694.637     0.156116  0.0 #O-Li
pair_coeff      1 3 table rnteter.dat RN_ONA
pair_coeff      2 3 table rnteter.dat RN_SIO
pair_coeff      3 3 table rnteter.dat RN_OO

kspace_style    pppm 1.0e-4
neighbor        2.0 bin
neigh_modify    every 1 check yes
timestep        1.0 #fs

