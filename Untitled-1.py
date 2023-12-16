
# Function to display big and bold text
def display_big_text(text):
    print("\033[1m" + text + "\033[0m")  # This is for terminal/console bold text

# Display big and bold welcome message
display_big_text("WELCOME TO AMMARA'S VENDING MACHINE")


from prettytable import PrettyTable
#vending machine items:
VENDING_MACHINE_ITEMS=[
    "DRINKS",
    "SNACKS",
    "JELLY",
    "BISCUITS",
    "COTTON_CANDY",
    "POPCORN"
    "CHOCOLATE",
    "CUP_NOODLES",
    "CHEWING_BUBBLE_GUM"
]
#storing the menu showing diffrent food items.
DRINKS=[{
    "srlno":"A1",
    "name":"DEW",
    "price": 5.00,
    "merchandise":20
    
    },
{ "srlno":"A2",
  "name":"SPRITE",
    "price": 5.00,
    "merchandise":20
},
{ "srlno":"A3",
    "name":"FANTA",
     "price": 5.00,
    "merchandise":25
}, 
{ "srlno":"A4",
    "name":"COKE",
     "price": 5.00,
    "merchandise":27
}, 
{ "srlno":"A5",
    "name":"PEPSI",
     "price": 5.00,
    "merchandise":24
}, ]

SNACKS=[
    {"srlno":"B1",
    "name":"LAYS SALTY",
     "price": 2.50,
    "merchandise":12
},
{ "srlno":"B2",
    "name":"LAYS SPICY",
     "price": 2.50,
    "merchandise":24
},
{ "srlno":"B3",
    "name":"CHEETOS CHEESE",
     "price": 5.50,
    "merchandise":15
},
{ "srlno":"B4",
    "name":"SMALL PRINGLES ORIGNAL",
     "price": 7.00,
    "merchandise":24
},
{ "srlno":"B5",
    "name":"DORITOS CHEESE",
     "price": 5.00,
    "merchandise":15
},
]
JELLY=[
{"srlno":"C1",
    "name":"GUMMY BEARS",
     "price": 3.00,
    "merchandise":24
},
{"srlno":"C1",
    "name":"GUMMY BEARS",
     "price": 4.00,
    "merchandise":15
},
    
{"srlno":"C2",
    "name":"JELLY BEANS",
     "price": 3.50,
    "merchandise":25
}
]
BISCUITS=[
{"srlno":"D1",
    "name":"DIGESTIVE BISCUIT",
     "price": 3.00,
    "merchandise":28
},
{"srlno":"D2",
    "name":"OREO",
     "price": 2.00,
    "merchandise":29
},
    
{"srlno":"D3",
    "name":"BELVITA",
     "price": 3.50,
    "merchandise":27
}
]
COTTON_CANDY=[
{"srlno":"E1",
    "name":"COTTON CANDY BLUE",
     "price": 5.00,
    "merchandise":24
},
{"srlno":"E2",
    "name":"COTTON CANDY PINK",
     "price": 5.00,
    "merchandise":24
},
    
{"srlno":"E3",
    "name":"COTTON CANDY MIX",
     "price": 5.50,
    "merchandise":18
}
]

POPCORN=[{"srlno":"F1",
    "name":"SALT POPCORN",
     "price": 3.00,
    "merchandise":19
},
{"srlno":"F2",
    "name":"CARAMEL POPCORN",
     "price": 3.00,
    "merchandise":19
     },
     {"srlno":"F3",
    "name":"CHEESE POPCORN",
     "price": 3.00,
    "merchandise":29
}
]
CHOCOLATE=[
{"srlno":"G1",
    "name":"DAIRY MILK",
     "price": 3.50,
    "merchandise":18
},
{"srlno":"G2",
    "name":"KITKAT",
     "price": 3.00,
    "merchandise":15
},
    
{"srlno":"G3",
    "name":"BREAK RIZZO",
     "price": 3.50,
    "merchandise":25
}
]
CUP_NOODLES=[
{"srlno":"H1",
    "name":"SAMYANG CARBONARA",
     "price": 13.50,
    "merchandise":20
},
{"srlno":"H2",
    "name":"SAMYANG SPICY",
     "price": 13.00,
    "merchandise":20
},
    
{"srlno":"H3",
    "name":"SAMYANG CHEESEY",
     "price": 13.50,
    "merchandise":20
}
]
CHEWING_BUBBLE_GUM=[
{"srlno":"I1",
    "name":"EXTRA STRAWBERRY",
     "price": 3.00,
    "merchandise":15
},
{"srlno":"I2",
    "name":"EXTRA MINT",
     "price": 3.00,
    "merchandise":18
},
    
{"srlno":"I3",
    "name":"EXTRA WATERMELON",
     "price": 3.50,
    "merchandise":28

}
]


# Function to display PrettyTable for a given category
def display_vendingitems_table(category, data):
    print(f"{category} Table:")
    table = PrettyTable()
    table.field_names = ['name']
    for row in data:
        table.add_row([row])
    print(table)
def display_table(category, data):
    print(f"{category} Table:")
    table = PrettyTable()
    table.field_names = ["srlno", "name", "price", "merchandise"]
    for row in data:
        table.add_row([row["srlno"], row["name"], row["price"], row["merchandise"]])
    print(table)


# Display tables for chips and drinks
display_vendingitems_table("vending machine items", VENDING_MACHINE_ITEMS)
display_table("Drinks", DRINKS)
display_table("Snacks", SNACKS)
display_table("Jelly", JELLY)
display_table("Biscuits", BISCUITS)
display_table("Cotton Candy", COTTON_CANDY)
display_table("Pop Corn", POPCORN)
display_table("Chocolate", CHOCOLATE)
display_table("Cup noddles", CUP_NOODLES)
display_table("Chewing bubble gum", CHEWING_BUBBLE_GUM)

# Display the initial shopping cart
total_amount = display_shopping_cart()

# Allow the user to add items to the shopping cart
while True:
    user_input = input("Enter the srlno of the item to add to the cart (q to finish): ")
    
    if user_input.lower() == 'q':
        break
    
    # Find the selected item
    selected_item = None
    for category_items in [DRINKS, SNACKS, JELLY, BISCUITS, COTTON_CANDY, POPCORN, CHOCOLATE, CUP_NOODLES, CHEWING_BUBBLE_GUM]:
        for item in category_items:
            if item["srlno"].lower() == user_input.lower():
                selected_item = item
                break

    if selected_item:
        add_to_cart(selected_item)
    else:
        print("Invalid selection. Please enter a valid srlno or 'q' to finish.")

# Display the final shopping cart
total_amount = display_shopping_cart()

# Process payment
process_payment(total_amount)

# Thank you message
print("Thanks for shopping!")
