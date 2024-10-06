#!/usr/bin/python3
append_after = __import__('100-append_after').append_after

def test_append_after():
    test_filename = "test_file.txt"
    search_string = "Python"
    new_string = "C is fun!\n"

    with open(test_filename, 'w') as file:
        file.write("I love Python.\n")
        file.write("Python is amazing.\n")
        file.write("Let's code!\n")

    append_after(test_filename, search_string, new_string)

    with open(test_filename, 'r') as file:
        result = file.read()
        print("Updated file content:")
        print(result)

test_append_after()
