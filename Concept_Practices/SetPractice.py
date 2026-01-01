# Practicing with the Set data type
# What is a set? A set is a de-duplicated list
# Sets also have different methods for comparison, since they contain no
# repeating values in an individual set.

set1 = set([1, 2, 3, 4, 5])
print(set1)
# The output terminal shows a list in braces, so we can create a set by making a list in braces
set2 = {1, 2, 3, 4, 5}
print(set2)

# We CANNOT create a blank set using the curly braces, as no data in that implies
# that the created object is a dictionary and must instead create an empty set by:
emptySet = set()

duplicatedSet = set([1, 1, 2, 2, 3, 4, 5, 5, 6, 4, 5, 6])
print(duplicatedSet)

# Sets are not immutable!
# We can add a single value using the .add() method
set1.add(6)
print(set1)
# We can add a list using the .update() method
set2.update([6, 7, 8])
print(set2)
# Values can also be removed using the .remove() and .discard() methods
# The difference is that .remove() will return a KeyError if the value passed
# does not exist within the set, whereas the .discard() method will simply move on.
set1.remove(5)
set1.discard(10)
print(set1)

# ========== Operations ==========
set3 = {1, 2, 3}
set4 = {2, 3, 4}
set5 = {3, 4, 5}

# Intersection method returns a set of values that are in the sets
intersectedSet = set3.intersection(set4, set5)
print(intersectedSet)

# The .difference() method returns a set of values that are not shared. The method will
# only compare values from the calling set, so changing the position of the sets may yield
# different results
differenceSet = set3.difference(set4)
print(differenceSet)

# Symmetric Difference will return ALL of the values that appear in one set but not the other
symmetricSet = set3.symmetric_difference(set4)
print(symmetricSet)

# De-duping list results using a set
# We can cast a list as a set to remove the duplicates (and cast it back if needed)

list1 = [1, 1, 2, 2, 3, 3, 4, 5, 6, 7]
list2 = list(set(list1))

print(list2)

# We can also cast lists as sets to do intersection or difference operation

employees = ["Corey", "Jim", "Steven", "April", "Judy", "Jenn", "John", "Jane"]
gymMembers = ["April", "John", "Corey"]
developers = ["Judy", "Corey", "Steven", "Jane", "April"]

swoleDevs = set(gymMembers).intersection(developers)
print(swoleDevs)

notGymOrDev = set(employees).difference(gymMembers, developers)
print(notGymOrDev)
