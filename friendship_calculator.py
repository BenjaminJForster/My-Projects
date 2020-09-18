name = input('Please enter a name to calculate: ')
name1 = input('Please enter another name to calculate: ')
special = '[@_!#$%^&*()<>?/\|}{~:]1234567890'

score = 0

specialInMessage = [c for c in special if c in name, name1]
if specialInMessage:
    print('Invalid character found in a name, exiting program')
    exit()
    
for character in name, name1:
  if character in 'aeiou':
    score += 5
  if character in 'friend':
    score += 10

print('Your friendship score is:', score)
exit()

if score > 100:
  print('You are best friends!')
  exit()
