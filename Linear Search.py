# %% [markdown]
# LINEAR SEARCH
# 
# There are certain conditions that code should meet (below are the conditions)
# 1. If the query number is repetative, than code should pick the firstly occured number.
# 2. If the input list is empty than the code should return -1.
# 3. If the query number/element present in the first/last location of input list also, code should detect the proper result
# 4. If the query number is nt present, than code should return -1

# %%
# function defines linear search
def locate_card(cards, query):
    #create a variable with position = 0
    position = 0 
    while True:
        if cards[position] == query:
            return position
        position += 1

        if position == len(cards):
            return -1
    -1

# %% [markdown]
#  Testing all edge condtions

# %%
# ideal input list
cards = [11,44,55,11,22,8,9,4]
query = 11
cards.sort(reverse=True)
result = locate_card(cards,query)
print(cards)
print(result)

# %%
# repetative input list
cards = [1,3,5,5,8,33,66,45,45,6]
query = 5
cards.sort(reverse=True)
result = locate_card(cards,query)
print(cards)
print(result)

# %%
# empty input list
cards = []
query = 11
cards.sort(reverse=True)
result = locate_card(cards,query)
print(cards)
print(result)

# %% [markdown]
# The above case (empty iput list) got failed so we have to alter the function

# %%
# the below program includes the edge condtion - empty input 
def locate_card1(cards, query):
    position = 0
    while len(cards)>0:
        if cards[position] == query:
            return position
        position += 1

        if position == len(cards):
            return -1
        
    return -1

# %%
# ideal input list
cards = [11,44,55,11,22,8,9,4]
query = 11
cards.sort(reverse=True)
result = locate_card1(cards,query)
print(cards)
print(result)

# %%
# repetative input list
cards = [1,3,5,5,8,33,66,45,45,6]
query = 5
cards.sort(reverse=True)
result = locate_card1(cards,query)
print(cards)
print(result)

# %%
# empty input list
cards = []
query = 11
cards.sort(reverse=True)
result = locate_card1(cards,query)
print(cards)
print(result)

# %%
# first number as a query number in input list
cards = [1,3,5,5,8,33,66,45,45,6]
query = 66
cards.sort(reverse=True)
result = locate_card1(cards,query)
print(cards)
print(result)

# %%
# query number not in input list
cards = [1,3,5,5,8,33,66,45,45,6]
query = 43
cards.sort(reverse=True)
result = locate_card1(cards,query)
print(cards)
print(result)

# %% [markdown]
# Functuon "locate_card1" executes well in all edge condtions