import matplotlib
matplotlib.use('Agg')
matplotlib.rcParams['font.sans-serif'] = 'Hiragino Kaku Gothic Pro, MigMix 1P'
import matplotlib.pyplot as plt

plt.plot([1,2,3,4,5], [1,2,3,4,5], 'bx--', label='１次関数')
plt.plot([1,2,3,4,5], [1,4,7,11,45], 'ro--', label='２次関数')
plt.xlabel('Xの値')
plt.xlabel('Yの値')
plt.title('sample')

plt.legend(loc='best')
plt.xlim(0, 6)
plt.savefig('adv.png', dpi=300)