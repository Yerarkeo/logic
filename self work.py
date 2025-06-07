for i in range(11):
    print(i)
for i in range(1,11):
    print(i)
h=11-1
for i in range(11):
    print(h-i)
for i in range(17):
    if i%2==1:
       print(i)
for i in range(1,15):
    if i%2==0:
        print(i)
for i in range(15):
    if i>4 and i<8:
        print(i)
string="Banana"
counter=0
for i in range(len(string)):
    counter+=1
print(counter)
string="Banana"
print(string[4])
string='banana'
for i in range(len(string)):
 print(string[i])
string="banana"
result=""
h=len(string)-1
for i in range(len(string)):
     result = result+ string (h-i)
print(result)
dog={'name':'kiki',
     'color':"black",
     'age':12
     }
print(dog)
butterfly={'color':'colorful',
           'size':'5cm',
           'wing':2}
print(butterfly)
color_fruit={'apple':'red',
             'banana':'yellow',
             'mango':'green'}
print(color_fruit)
my_sibling={'sister':3,
            "broter":3}
print(my_sibling['broter'])
yon={'subject':"fish",
     'hight':160}
yon['subject']='phython'
yon['age']=23
# del yon['hight']
yon.pop('hight')
print(yon)
product={'name':'viso',
         'contact':{'new name':'yon',
                    'contact':95727373}}
print(product['name'])
print(product)