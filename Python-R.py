# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     cell_metadata_json: true
#     comment_magics: false
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.4.2
#   kernelspec:
#     display_name: rpy
#     language: python
#     name: rpy
# ---

# %% {"slideshow": {"slide_type": "slide"}}
import pandas as pd
import numpy as np

# %% {"slideshow": {"slide_type": "slide"}}
pd.set_option("display.max_rows", 8)

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# ## Transferring R data sets into Python

# %% {"slideshow": {"slide_type": "fragment"}}
# %load_ext rpy2.ipython

# %% [markdown] {"slideshow": {"slide_type": "fragment"}}
# - conversions of R to pandas objects will be done automatically

# %% {"slideshow": {"slide_type": "fragment"}}
from rpy2.robjects import r
x = r('c(1,2,3,4)')
type(x)

# %% {"slideshow": {"slide_type": "fragment"}}
v = r('seq(1:10)')
v

# %% {"slideshow": {"slide_type": "slide"}}
from rpy2.robjects import pandas2ri

pandas2ri.activate()
r.library('missMDA')
r.data('orange')
orange = r('orange')

# %% {"slideshow": {"slide_type": "slide"}}
print(orange)

# %% {"slideshow": {"slide_type": "slide"}, "language": "R"}
# library('missMDA')
# data(orange)
# estim_ncpPCA(orange)

# %% {"slideshow": {"slide_type": "fragment"}}
from rpy2.robjects.packages import importr

miss_mda = importr('missMDA')
res = miss_mda.imputePCA(orange,ncp=2)
orange_r = res[0]
print(orange_r)

# %% {"slideshow": {"slide_type": "slide"}}
from rpy2.robjects import r
r('library(missMDA)')
r('df <- imputePCA(orange,ncp=2) ')
r('res <- as.data.frame(df$completeObs)')
orange = r('res')
print(orange)

# %%
import pandas as pd
from rpy2 import robjects as ro
from rpy2.robjects import pandas2ri
pandas2ri.activate()
R = ro.r

df = pd.DataFrame({'x': [1,2,3,4,5], 
                   'y': [2,1,3,5,4]})

M = R.lm('y~x', data=df)
print(R.summary(M).rx2('coefficients'))


# %%
