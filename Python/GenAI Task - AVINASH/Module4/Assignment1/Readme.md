Module 4 / Assignment 1 / Task 1: Product Collection (Lists and Tuples)
What this task is about

This task shows how to use lists and tuples in Python for a small e-commerce store. Only standard Python is used (no extra libraries).

File in this folder
task1.ipynb - the notebook with all the code and outputs
What I did
1. Created a list of products

I made a list called products with 6 product names: Computer, Laptop, Mobile, Earbud, CPU, Charger. A list is used because I can change it later (add or remove items).

2. Created a tuple for one product

I made a tuple called sample_product that stores: ("Laptop", 5000, "Electronics") which is (product name, price, category). A tuple is used because the details of one product should stay fixed.

3. Printed the 2nd and last product
products[1] gives the 2nd product (index starts from 0) -> Laptop
products[-1] gives the last product (negative index counts from the end) -> Charger
4. Added two new products

I used append() two times to add Keyboard and Mouse. The updated list is: ['Computer', 'Laptop', 'Mobile', 'Earbud', 'CPU', 'Charger', 'Keyboard', 'Mouse']

Extra: Changed the price in a tuple

A tuple cannot be changed directly, so I did this:

Converted the tuple into a list using list()
Changed the price from 5000 to 6000
Converted it back into a tuple using tuple()

Final result: ('Laptop', 6000, 'Electronics')

How to run
1. Open task1.ipynb in Jupyter Notebook or VS Code.
2. Run all the cells from top to bottom.










Module 4 / Assignment 1 / Task 2: Categories (Sets)
What this task is about

This task shows how to use a set in Python to store product categories. A set keeps only unique values, so duplicate categories are removed automatically. Only standard Python is used (no extra libraries).

File in this folder
task2.ipynb - the notebook with all the code and outputs
What I did
1. Created a set of categories

The product names do not contain categories, so I made a separate list called category with a category name for each product, for example Electronics, Audio, Accessories, Computer Accessories.

Then I converted it into a set: category_set = set(category)

The list has repeated values (like Electronics many times), but the set keeps each category only once: {'Computer Accessories', 'Accessories', 'Audio', 'Electronics'}

2. Added a new category and checked duplicates
category_set.add("Gaming") -> Gaming is new, so it is added.
category_set.add("Audio") -> Audio is already there, so it is ignored and the set does not change.

Set after both steps: {'Computer Accessories', 'Accessories', 'Electronics', 'Gaming', 'Audio'}

3. Checked if a category exists

I used the in keyword, which gives a boolean (True or False): print("Audio" in category_set) -> True

Extra: Total number of unique categories

print(len(category_set)) -> 5

How to run
1. Open task2.ipynb in Jupyter Notebook or VS Code.
2. Run all the cells from top to bottom.








Module 4 / Assignment 1 / Task 3: Product Pricing (Dictionaries)
What this task is about

This task shows how to use a dictionary in Python to store product names with their prices. A dictionary stores data as key-value pairs: the key is the product name and the value is the price. Only standard Python is used (no extra libraries).

File in this folder
task3.ipynb - the notebook with all the code and outputs
What I did
1. Created a dictionary of prices

I made a dictionary called price_dict with 6 products: Laptop, Mobile, Keyboard, Mouse, Headphones, Monitor.

2. Changed the dictionary
Added a new product: price_dict["Tablet"] = 30000
Updated an existing price: price_dict["Mobile"] = 27000 (was 25000)
Removed a product by name: price_dict.pop("Mouse", None)
If the product exists, it is removed and its price is returned (800).
If the product does not exist (like "Nokia"), it returns None and does not give an error. This handles the case when the product is missing.

Dictionary after all changes: {'Laptop': 70000, 'Mobile': 27000, 'Keyboard': 1000, 'Headphones': 3500, 'Monitor': 12000, 'Tablet': 30000}

3. Found the average price

Using only dictionary operations and basic arithmetic:

sum(price_dict.values()) gives the total of all prices -> 143500
len(price_dict) gives the number of products -> 6
Total divided by count gives the average -> 23916.666666666668
Extra: Maximum and minimum price
max(price_dict.values()) -> 70000
min(price_dict.values()) -> 1000
How to run
1. Open task3.ipynb in Jupyter Notebook or VS Code.
2. Run all the cells from top to bottom.






Module 4 / Assignment 1 / Task 4: Combined Operations
What this task is about

This task combines everything from the earlier tasks (lists, tuples, sets and dictionaries) into one small inventory program for an e-commerce store. Only standard Python is used (no extra libraries).

File in this folder
task4.ipynb - the notebook with all the code and outputs
Data used
products - list of product names
price_dict - dictionary with the price of each product
categories - list with the category of each product (same order as products)
What I did
1. Created catalog (list of tuples)

I looped over products by index. For each product I took:

the name from products
the price from price_dict (using .get(name, 0), so a missing price gives 0 and not an error)
the category from categories (same index)

Then I put them in a tuple (product_name, price, category) and added it to catalog.

2. Created category_to_products (dictionary of lists)

I looped over catalog and unpacked each tuple.

If the category was not in the dictionary yet, I created an empty list for it.
Then I added the product name to that category's list.

Result: {'Computing': ['Computer', 'Laptop', 'CPU'], 'Mobile': ['Mobile'], 'Accessories': ['Earbud', 'Charger']}

3. Printed the products of the biggest category

I kept a variable max_category and compared the len() of each category's list. The category with the most products is kept, and its products are printed.

Edge cases handled
A product with no price: .get(name, 0) avoids a KeyError.
An empty catalog: prints "No products available." instead of failing.
Two categories with the same count: the first one found is used.
How to run
Open task4.ipynb in Jupyter Notebook or VS Code.
Run all the cells from top to bottom.