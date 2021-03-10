import numpy as np
import cudf
s = cudf.Series([1,2,3,None,4])
df = cudf.DataFrame([('a', list(range(20))),
                     ('b', list(reversed(range(20)))),
                     ('c', list(range(20)))])