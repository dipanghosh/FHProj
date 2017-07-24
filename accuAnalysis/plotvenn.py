import loadfiles as ld
from matplotlib import pyplot as plt
from matplotlib_venn import venn3, venn2

venn2([set(ld.listAll1006), set(ld.listInconAll588342)])
plt.show()