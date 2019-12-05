cart ={}
items_cart = {}
add_item ={}
tot_amount =[]
choice = 0

def print_output(tot_amt_val,offer):
    discount = tot_amt_val * offer
    final_total = tot_amt_val - discount
    print("Total amount ",tot_amt_val)
    print("discount ",discount)
    print("Amount payable ",final_total)

while(choice != 4):
    print("1.To purchase 2.view items 3.Generate Bill 4.exit")
    choice = int(input())
    if choice == 1:
        no_items = int(input())
        for i in range(no_items):
            item = input()
            qnt = int(input())
            price = int(input())
            add_item[item + "quantity"] = qnt
            add_item[item + "price"] = price
            cart[item] = add_item
            add_item = {}
    if choice == 2:
        inc_val = 1
        if cart == {}:
            print("Add some items to the cart")
        else:
            print("{:<10}{:<12}{:<12}{:<12}{:<12}".format("S.no","name","product","price","total"))
            for k,v in cart.items():
                print("{:<10}{:<12}{:<12}{:<12}{:<12}".format(inc_val,str(k),list(v.values())[0],list(v.values())[1],(list(v.values())[0]*list(v.values())[1])))
                tot = (list(v.values())[0]*list(v.values())[1])
                tot_amount.append(tot)
                inc_val+=1
    if choice == 3:
        tot_amt_val = sum(tot_amount)
        if tot_amt_val <=500:
            offer = 0.02
            print_output(tot_amt_val,offer)
        elif tot_amt_val > 500 and tot_amt_val <= 1000:
            offer = 0.05
            print_output(tot_amt_val,offer)
        elif tot_amt_val > 1000:
            offer = 0.08
            print_output(tot_amt_val,offer)
    if choice == 4:
        print("Purchase Finished!!")