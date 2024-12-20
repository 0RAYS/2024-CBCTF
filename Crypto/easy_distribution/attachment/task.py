from sage.all import *
from sage.stats.distributions.discrete_gaussian_integer import DiscreteGaussianDistributionIntegerSampler
from flag import flag


def ZZ_to_Fq(_vector, _q, _n):
    return [int(i % _q) if abs(_q - int(i % _q)) > int(i % _q) else (int(i % _q) - _q) for i in _vector] + [0] * (
            _n - len(_vector))


def LWE_PRNG(m, n, q, sigma_s, sigma_e):
    Ds = DiscreteGaussianDistributionIntegerSampler(sigma_s)
    De = DiscreteGaussianDistributionIntegerSampler(sigma_e)
    A = random_matrix(ZZ, m, n, x=-(q//2), y=q//2+1)
    s = vector(ZZ, [Ds() for _ in range(n)])
    e = vector(ZZ, [De() for _ in range(m)])
    b = A * s + e
    return ZZ_to_Fq(b, q, m)


def LWR_PRNG(m, n, q, sigma_s, k):
    Ds = DiscreteGaussianDistributionIntegerSampler(sigma_s)
    A = random_matrix(ZZ, m, n, x=-(q // 2), y=q // 2 + 1)
    s = vector(ZZ, [Ds() for _ in range(n)])
    b = A * s
    return [bi // k for bi in ZZ_to_Fq(b, q, m)]


n = 256
q = 307
sigma_s = 1
k = 3
samples_num = 12000
flag_bit = bin(int.from_bytes(flag, byteorder='big'))[2:]

data = []
for bi in flag_bit:
    if bi == '1':
        data.append(LWR_PRNG(samples_num, n, q, sigma_s, k))
    else:
        data.append(LWE_PRNG(samples_num, n, q//k+1, sigma_s, sigma_s))

open('./data.txt', 'w').write(str(data))
