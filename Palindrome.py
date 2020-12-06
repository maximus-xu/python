
from python.utils import reverse_string

def palindrome_problem():
    input_str = str(input("Enter: "))
    reversed_input = reverse_string(input_str)
    print(reversed_input == input_str)
