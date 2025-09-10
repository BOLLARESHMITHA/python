"""You are building a simple E-commerce application in Python. The system should maintain a list of products available in the cart. Write a Python program to perform the following operations using Lists:
1.Add a product to the cart.
2.Remove a product from the cart 
3.Search for a product in the cart 
4.Display all products in the cart
5.Show the total number of products in the cart
 
Cart Operations:
1. Add Product
2. Remove Product
3. Search Product
4. Display Cart
5. Count Products
6. Sort Cart
7. Clear Cart
8. Exit

 
Enter choice: 1
Enter product to add: Laptop
Product 'Laptop' added to cart.
 
Enter choice: 1
Enter product to add: Phone
Product 'Phone' added to cart.
 
Enter choice: 4
Cart: ['Laptop', 'Phone']
 
Enter choice: 3
Enter product to search: Phone
Yes, 'Phone' is in the cart.
 
Enter choice: 5
Total products in cart: 2"""

def Add_Product(cart,item):
    cart.append(item)
    print("Product '",item,"' added to cart.")
    return cart

def Remove_Product(cart,item):
    new_cart=[]
    for i in cart:
        if(i!=item):
            new_cart.append(i)
    print("Product '",item,"' removed from cart.")
    return new_cart

def Search_Product(cart,item):
    found=False
    for i in range(0,len(cart)):
        if(cart[i]==item):
            found=True
            break
    if(found):
        print("Product '",item,"' found in cart.")
    else:
        print("Product '",item,"' not found in cart.")

def Display_cart(cart):
    print("cart = ",cart)

def Count_products(cart):
    print("Total products in cart: ",len(cart))

def Sort_cart(cart):
    return cart.sort()

def Clear_cart(cart):
    return cart.clear()

cart=[]

while(True):

    ch=int(input("Enter choice :"))

    if(ch>=1 and ch<=7):
        if(ch==1):
            product=input("Enter product to add:")
            Add_Product(cart,product)
        elif(ch==2):
            product=input("Enter product to remove:")
            Remove_Product(cart,product)
        elif(ch==3):
            product=input("Enter product to search:")
            Search_Product(cart,product)
        elif(ch==4):
            Display_cart(cart)
        elif(ch==5):
            Count_products(cart)
        elif(ch==6):
            Sort_cart(cart)
        else:
            Clear_cart(cart)
    else:
        break