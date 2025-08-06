# Creating a module to test importing and using modules.

# Success message courtesy of Xibalba
# print("This should be played at high volume. Preferably in a residential area.")

# Display the name of the module
# print("Module name:", __name__)
# When the module is run directly, __name__ is set to "__main__".
# When imported, __name__ is set to the module's name.
# This is why we run test cases with `if __name__ == "__main__":` to avoid running them when the module is imported.

# if __name__ == "__main__":
#     print("This module is being run directly.")
# else:
#     print("This module has been imported.")

# We can create our own functions and classes in this module.

__counter = 0

def list_sum(list):
    global __counter
    __counter += 1
    return sum(list)

def list_product(list):
    global __counter
    __counter += 1
    result = 1
    for item in list:
        result *= item
    return result

if __name__ == "__main__":
    print('I am just a module, but I will run these test cases here.')
    test_list = [i for i in range(1, 6)]
    print("Sum:", list_sum(test_list))
    print("Product:", list_product(test_list))
