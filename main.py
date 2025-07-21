'''
I will  create a phone_book  using   the concept of  dictionary in pythioon programming language.
'''

Phoe_book={
    'Rahul':9365476198,
    'Mohan':7002605460,
    'Neha':8011224629,
    'old_man':9101124288.
}


for key ,value in Phoe_book.items():
    print(f'The  phonebook is {key}:{value}')


print('\n here is the feature using which a user can  add new contact on phone-book .')

new_name=input('Enter your name :')
new_contact=int(input('Enter your number = '))

Phoe_book[new_name]=new_contact

for key ,value in Phoe_book.items():
    print(f'The  phonebook is {key}:{value}')


print('\n here is the feature using which a user can  delete any existing  contact on phone-book .')

Delete=input('Enter your name :')

del Phoe_book[Delete]

for key ,value in Phoe_book.items():
    print(f'The  phonebook is {key}:{value}')


Search=input('Enter  your  name : ')

if Search in Phoe_book:
    print(f' In  the  search person contact number is :{Phoe_book[Search]}')


