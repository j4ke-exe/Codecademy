import numpy

coin_flip = numpy.random.binomial(n=1, p=0.5, size=1000)

tails = 0
heads = 0
for num in coin_flip:
  if num == 0:
    tails += 1
  else:
    heads += 1

print(f'Number of tails: {tails}')
print(f'Number of heads: {heads}')
