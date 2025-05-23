menu=[]
id=1
def addfood(name,photo,price,quan,rate):
    global id
    dct={
        'id':id,
        'name':name,
        'photo':photo,
        'price':price,
        'quan':quan,
        'rate':rate
    }
    menu.append(dct)
    id+=1
    print()
    print('New food aded succesfully')
    print()
    print()
def getmenu():
     for i in menu:
        print('-'*30)
        print(f"""
id     --->{i['id']}
name   --->{i['name']}
photo  --->{i['photo']}
price  --->{i['price']}
quan   --->{i['quan']}
rate   --->{i['rate']}
-----------------------
total  --->{i['price']*i['quan']}
-----------------------
""")
def getid(id):
     b=True
     for i in menu:
          if i["id"]==id:
               b=False
               print('-'*30)
               print(f"""
id     --->{i['id']}
name   --->{i['name']}
photo  --->{i['photo']}
price  --->{i['price']}
quan   --->{i['quan']}
rate   --->{i['rate']}
-----------------------
total  --->{i['price']*i['quan']}
-----------------------
""")
def deletid(id):
     b=True
     for i in menu:
          if i['id']==id:
               b=False
               s=input(f'are you sure y/n---> ')
               if s=='y' or s=='yes' or s=='YES':
                    menu.remove(i)
                    print()
                    print(f'food with id {id} deleted succesfuly')
                    print()
     if b:
          print('id not found')
def update(id):
     b=True
     for i in menu:
          if['id']==id:
               b=False
               m=int(input(
                    """
1  --->updade only name
2  --->updade only photo
3  --->updade only price
4  --->updade only qantity
5  --->updade only rate
6  --->updade all
7  --->main menu
-- -- -- -- -- -- -- -- --
What do you want to update
"""
               ))
          if m==1:
               name=input('enter new name for this food --> ')
               i['name']=name
               print(f'name of food with id {id} changed succesfully')
               update(id)
          if m==2:
               photo=input('enter new photo for this food --> ')
               i['photo']=photo
               print(f'photo of food with id {id} changed succesfully')
               update(id)
          if m==3:
               price=input('enter new price for this food --> ')
               i['price']=price
               print(f'price of food with id {id} changed succesfully')
               update(id)
          if m==4:
               quan=input('enter new quantity for this food --> ')
               i['quan']=quan
               print(f'quantity of food with id {id} changed succesfully')
               update(id)
          if m==5:
               rate=input('enter new rate for this food --> ')
               i['rate']=rate
               print(f'rate of food with id {id} changed succesfully')
               update(id)
          if m==6:
               name=input('enter new name for this food --> ')
               i['name']=name

               photo=input('enter new photo for this food --> ')
               i['photo']=photo

               price=input('enter new price for this food --> ')
               i['price']=price

               quan=input('enter new quantity for this food --> ')
               i['quan']=quan

               rate=input('enter new rate for this food --> ')
               i['rate']=rate

               print(f'food with id {id} changed succesfully')
               update(id)
          if m==7:
               return 0
     if b:
          print(f'id {id} not found')
def  maxprice():
     mx=0
     for i in menu:
      if i['price']>=mx:
           mx=i['price']
     print(f'max-price: {mx}')
def  maxquan():
     mx=0
     for i in menu:
      if i['quan']>=mx:
           mx=i['quan']
     print(f'max-qwantity: {mx}')
def  maxtotal():
     mx=0
     for i in menu:
      if i['price']*i['quan']>=mx:
           mx=i['price']*i['quan']
     print(f'max-total: {mx}')
def  minprice():
     mn=9999999
     for i in menu:
      if i['price']<=mn:
           mn=i['price']
     print(f'min-price: {mn}')
def  minquan():
     mn=9999999
     for i in menu:
      if i['quan']<=mn:
           mn=i['quan']
     print(f'min-qwantity: {mn}')
def  mintotal():
     mn=9999999
     for i in menu:
      if i['price']*i['quan']<=mn:
           mn=i['price']*i['quan']
     print(f'min-total: {mn}')
while True:
    n=int(input("""
1   ----->add new food)
2   ----->get all menu
3   ----->get by id
4   ----->delete food by id
5   ----->update food by id
6   ----->max-price
7   ----->max-qwantity
8   ----->max-total
9   ----->min-price
10  ----->min-qwantity
11  ----->min-total

Choose your option -----> """))
    if n==1:
        print()
        addfood(input('inter name of food ---> '),
                input('inter photo of food ---> '),
                int(input('inter price of food ---> ')),
                int(input('inter quantity of food ---> ')),
                int(input('inter rate of food ---> '))
                )
        print()
    if n==2:
            getmenu()
    if n==3:
         getid(int(input('enter your id -->' )))
    if n==4:
         deletid(int(input('enter your id for delete -->' )))
    if n==5:
         update(int(input('enter your id for update -->')))
    if n==6:
         maxprice()
    if n==7:
         maxquan()
    if n==8:
         maxtotal()
    if n==9:
        minprice()
    if n==10:
        minquan()
    if n==11:
        mintotal()
         
         