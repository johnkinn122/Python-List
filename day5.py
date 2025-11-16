# Exercises: Day 5

# Exercises: Level 1
""""
1. Declare an empty list
2. Declare a list with more than 5 items
3. Find the length of your list
4. Get the first item, the middle item and the last item of the list
5. Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
6. Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
7. Print the list using print()(skip)
8. Print the number of companies in the list(skip)
9. Print the first, middle and last company(skip)
10. Print the list after modifying one of the companies
11. Add an IT company to it_companies(skip)
12. Insert an IT company in the middle of the companies list(skip)
13. Change one of the it_companies names to uppercase (IBM excluded!)(skip)
14. Join the it_companies with a string '#;'
15. Check if a certain company exists in the it_companies list.
16. Sort the list using sort() method
17. Reverse the list in descending order using reverse() method
18. Slice out the first 3 companies from the list
19. Slice out the last 3 companies from the list
20. Slice out the middle IT company or companies from the list
21. Remove the first IT company from the list(skip)
22. Remove the middle IT company or companies from the list(skip)
23. Remove the last IT company from the list(skip)
24. Remove all IT companies from the list
25. Destroy the IT companies list
26. Join the following lists:
--> front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
--> back_end = ['Node','Express', 'MongoDB']
27. After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.
"""
#Exercises: Level 2
"""
1. The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
- Sort the list and find the min and max age
- Add the min age and the max age again to the list
- Find the median age (one middle item or two middle items divided by two)
- Find the average age (sum of all items divided by their number )
- Find the range of the ages (max minus min)
- Compare the value of (min - average) and (max - average), use abs() method
1. Find the middle country(ies) in the countries list
2. Divide the countries list into two equal lists if it is even if not one more country for the first half.
3. ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
"""
# Exercises: Level 1

#1. Declare an empty list
list = []
#2. Declare a list with more than 5 items
list_2 = [1,2,3,4,5,6]
#3. Find the length of your list
len_list = len(list_2)
print(len_list)
#4. Get the first item, the middle item and the last item of the list
first_item = list_2[0]
middle_item_left = list_2[2]
middle_item_right = list_2[-3]
last_item = list_2[-1]
#5. Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ['FLm', 69, 1.69, "married", "Biringan"]
#6. Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
#10. Print the list after modifying one of the companies
it_companies[0] = "FLM Foundation inc"
print(it_companies)
#14. Join the it_companies with a string '#;'
join_item = " #; ".join(it_companies)
print(join_item)
#15. Check if a certain company exists in the it_companies list.
if "Google" in it_companies:
  print(True)
else:
  print(False)
#16. Sort the list using sort() method
it_companies.sort()
print(it_companies)
#17. Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies)
#18. Slice out the first 3 companies from the list
slice_first_three_elements = it_companies[0:3]
print(slice_first_three_elements)
#19. Slice out the last 3 companies from the list
slice_last_three_elements = it_companies[5:]
print(slice_last_three_elements)
#20. Slice out the middle IT company or companies from the list
slice = it_companies[3] 
print(slice)
#24. Remove all IT companies from the list
it_companies.clear()
print(it_companies)
#25. Destroy the IT companies list
# same solution in #24
#26. Join the following lists:
#--> front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
#--> back_end = ['Node','Express', 'MongoDB']
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
full_stack = front_end + back_end
print(full_stack)
#27. After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.
full_stack[5:5] = ['Python', 'SQL']  # insert after Redux
print(full_stack)

#Exercises: Level 2

#1. The following is a list of 10 students ages:
"""
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
- Sort the list and find the min and max age
- Add the min age and the max age again to the list
- Find the median age (one middle item or two middle items divided by two)
- Find the average age (sum of all items divided by their number )
- Find the range of the ages (max minus min)
- Compare the value of (min - average) and (max - average), use abs() method
"""
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
#- Sort the list and find the min and max ages
ages.sort()
print(ages)
#find the min and max ages
max_age = max(ages)
min_age = min(ages)
print(max_age)
print(min_age)
#- Find the median age (one middle item or two middle items divided by two)
import statistics
median_ages = int(statistics.median(ages))
print(f"the median of ages: {median_ages}")
#- Find the average age (sum of all items divided by their number )
mean_ages = int(statistics.mean(ages))
print(f"the average or mean of ages: {mean_ages}")
#- Find the range of the ages (max minus min)
range_ages = max_age - min_age
print(f"the range of ages: {range_ages}")
#- Compare the value of (min - average) and (max - average), use abs() method
abs_min_diff = abs(min_age - mean_ages)
abs_max_diff = abs(max_age - mean_ages)
print(f"Absolute difference between min and average: {abs_min_diff}")
print(f"Absolute difference between max and average: {abs_max_diff}")

if abs_min_diff > abs_max_diff:
    print("min is farther from average than max")
elif abs_min_diff < abs_max_diff:
    print("max is farther from average than min")
else:
    print("min and max are equally far from average")

#1. Find the middle country(ies) in the countries list
import countries 
countries_len = len(countries.countries)
print(countries_len)
mean_countries = statistics.median(countries.countries)
print(mean_countries)
#2. Divide the countries list into two equal lists if it is even if not one more country for the first half.

all_countries = countries.countries  # assuming countries is a list in your module

# Calculate midpoint: if odd, first half gets the extra country
mid = (len(all_countries) + 1) // 2

# Split the list
first_half = all_countries[:mid]
second_half = all_countries[mid:]

print("First half:", first_half)
print("Second half:", second_half)
#3. ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
sample_countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']

# Unpack the first three and the rest
china, russia, usa, *scandic_countries = sample_countries

print("First country:", china)
print("Second country:", russia)
print("Third country:", usa)
print("Scandic countries:", scandic_countries)
