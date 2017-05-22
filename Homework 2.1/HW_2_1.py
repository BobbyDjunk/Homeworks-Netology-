def reading_file():
  cook_book = []
  cb_dict = {}
  x = int(1)
  
  with open('cook_book.txt') as f:
    for line in f:
      cook_book += [line.strip()]

  while x < len(cook_book):
    cb_dict[cook_book[x-1]] = [{'ingridient_name':'', 'quantity': 0, 'measure':''} for i in range(int(cook_book[x]))]
    for i in range(int(cook_book[x])):
      cb_dict[cook_book[x-1]][i]['ingridient_name'] += cook_book[i+(x+1)].split(' ')[0]
      cb_dict[cook_book[x-1]][i]['quantity'] += int(cook_book[i+(x+1)].split(' ')[1])
      cb_dict[cook_book[x-1]][i]['measure'] += cook_book[i+(x+1)].split(' ')[2]
    x += int(cook_book[x])+2
    
  return cb_dict

def get_shop_list_by_dishes(dishes, person_count):
  shop_list = {}
  
  for dish in dishes:
    for ingridient in reading_file()[dish]:
      new_shop_list_item = dict(ingridient)
      new_shop_list_item['quantity'] *= person_count
      if new_shop_list_item['ingridient_name'] not in shop_list:
        shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
      else:
        shop_list[new_shop_list_item['ingridient_name']]['quantity'] += new_shop_list_item['quantity']
        
  return shop_list

def print_shop_list(shop_list): 
  # for shop_list_item in shop_list.values():
  #   print('{} {} {}'.format(shop_list_item['ingridient_name'], shop_list_item['quantity'], shop_list_item['measure']))
  for shop_list_item in shop_list.values():
    print('{ingridient_name} {quantity} {measure}'.format(**shop_list_item))
  
def create_shop_list():
  person_count = int(input('Введите количество человек: '))
  dishes = input('Введите количество блюд в расчете на одного (через запятую): ').lower().split(', ')
  shop_list = get_shop_list_by_dishes(dishes, person_count)
  print_shop_list(shop_list)


create_shop_list()
