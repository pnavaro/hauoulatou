library(missMDA)

data(orange)

nbdim <- estim_ncpPCA(orange) # estimate the number of dimensions to impute

res.comp <- imputePCA(orange, ncp = nbdim)

res.comp
