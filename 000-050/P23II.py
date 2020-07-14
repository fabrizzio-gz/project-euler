# It continues where P23 left off
import pickle

f = open('abundant_sums.pkl', 'rb')
sum_abundant_numbers = pickle.load(f)
f.close()

# eliminate duplicates
sum_abundant_numbers = set(sum_abundant_numbers)
sum_abundant_numbers.remove(28123)
sum_abundant = sum(sum_abundant_numbers)
sum_normal = sum(list(range(28123)))
print(sum_normal - sum_abundant)
#sum_abundant_numbers.sort()
#sum_abundant_numbers_unique = []
#for num in sum_abundant_numbers:
#    if num not in sum_abundant_numbers_unique:
#        sum_abundant_numbers_unique.append(num)
