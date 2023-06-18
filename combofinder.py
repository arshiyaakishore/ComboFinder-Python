#Find all the list of products whose sum-of-price is between 290 and 310.

#Step 1: Library inclusion                             
import random as r



# Step 2: Parameter Setting
ProductList = {'p1':10, 'p2':15, 'p3':20, 'p4':25, 'p5':30, 'p6':35, 'p7':50,
               'p8':40, 'p9':55, 'p10':60, 'p11':65, 'p12':75, 'p13':70,
               'p14':45}
LB          = 290
UB          = 310
ResultList  = set()   # Store Result List i.e. list of sets whose sum is between 90 and 210.
Iterations  = 1000    # Number of Inerations

# Step3: Start Program
for i in range(Iterations):

    # Select combo size (i.e. number of products in a combo)
    SetSize = r.randint(2, len(ProductList)-1)

    # Select number of elements from Set
    ComboList = r.sample(list(ProductList.keys()),SetSize)
    ComboList.sort()

    # Sum the products in ColboList
    ComboSum = sum([ ProductList[i] for i in ComboList])

    # Check the Sum Between LB and UB
    if ComboSum>= LB and ComboSum<= UB:
      ResultList.add(tuple(ComboList))


#The for loop runs Iterations times, and in each iteration, a combination of products is generated.
# SetSize is assigned a random value between 2 and the length of ProductList minus
# 1. This determines the number of products to be selected in a single combination.
# ComboList is generated using the sample() function from the random module. It randomly selects SetSize number of elements (product codes) from ProductList.keys().
# The selected elements are then sorted in ascending order.
# The total sum of prices for the products in ComboList is calculated and assigned to ComboSum using a list comprehension and the sum() function.
# The if statement checks if ComboSum falls between LB and UB. If it does, the combination ComboList is added to ResultList as a tuple.
      
# Print all the sets whose sum is between LB and UB
for r in ResultList:
	print (r)

# Print total sets
print ("\nTotal Sets: ", len(ResultList), "\n")
