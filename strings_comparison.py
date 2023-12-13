#word = 'anusha'
#word = 'ANusha'

#Upper cases are less than the lower cases

word = 'anUsha'

if word == 'anusha':
    print("All right, It's perfect match")
    
if word < 'anusha':
    print('Your word,' + word + ', comes before anusha.')
elif word > 'banana':
    print('Your word,' + word + ', comes after banana.')
else:
    print('All right, done.')