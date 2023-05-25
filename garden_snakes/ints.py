int_ranges = [2,4,8,16,32,64,128,256,512,1024,2048]
for i in int_ranges:
	signed = 2 ** (i - 1)
	unsigned = (2 ** i) - 1
	print('Signed {0}-bit int goes from -{1} to {2}'.format(i, f"{signed:,}", f"{signed - 1:,}"))
	print('Unsigned {0}-bit int goes from 0 to {1}'.format(i, f"{unsigned:,}"))
