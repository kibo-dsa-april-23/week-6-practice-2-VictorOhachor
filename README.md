# Linked List String

In this assignment, you will write iterative and recursive methods that operate on a linked list representation of a string. We started the `LLString` class in the lessons and practice exercises this week. Now, it's your turn to add functionality to it.

## Starter Code

You are given the file `llstring.py`, which includes the implementation of `LLString` class that we started in the lessons this week. Each `LLString` object contains both a `head` pointer to the beginning of the linked list, as well as a `tail` pointer to the end of the linked list. It also contains the following methods:

* Constructors (`__init__`) for creating a linked list, including from a string
* An `append()` method, which appends a new node to the end of the list
* A `print()` method, which prints the contents of the list
* A `to_string()` method, which returns a string version of the `LLString`

***You should not change any of the existing methods in the `LLString` class.*** Doing so may hinder our ability to test your code.

You may wish to refer back to the lessons or practice exercises to see example implementations of other `LLString` methods.

## Steps to Complete

Implement the following six methods. As you do so, keep the following guidelines in mind:

* For some methods, you may be required to implement the solution either iteratively or recursively. Solutions that don't implement the method using the described technique will receive only partial credit.
* You should *not* change any of the method signatures (names or parameters), and in particular, you should not add any optional or default parameters.
* If you need to add a recursive helper function, you should create a new method using the double underscore convention. For example, if the given method to implement is `print()` and you need a recursive helper method, you should name the recursive method `__print()`.
* For each method, you should consider all possible edge cases, including (but not limited to): if the list is empty and if the list has one node. Be sure to test your methods with as many cases as possible. More information about testing is below.

1. Implement the `print_every_other()` method using either iteration or recursion.

    'print_every_other()` should print the first character of the linked list, followed by every other character from that point.

    For example, if the list represents the string `'hello'`, then `print_every_other()` should print `'hlo'`.

    Notes:

    * You may use either iteration or recursion.
    * Your method should print a newline character at the end of the string.
    * Remember that Python's `print()` function has an optional parameter `end` that you can use to print each individual character (without including a newline after each character): `print(trav.val, end='')`.
    * If the list is empty, the method should print a newline character.

2. Implement the `char_at(i)` method using recursion.

    `char_at(i)` finds and returns the character at index `i` in the list.

    For example, if the list represents the string `'hello'`, then `char_at(3)` should return `'l'`.

    Notes:

    * Your solution should use recursion.
    * If the list is empty or doesn't have `i` characters, your method should return `None`.

3. Implement the `concat(other_llstring)` method using iteration.

    `concat(other_llstring)` concatenates the calling `LLString` (`self`) with `other_llstring` and returns the result.

    For example, if the calling list (`self`) represents the string `'banana'`, and the other `LLString` represents the string `'orange'`, then `concat(other_llstring)` should modify the calling list so that it holds `'bananaorange'`.

    Notes:

    * You don't need to create any new nodes.
    * You should use iteration.
    * If the calling list is empty, your method should modify the calling list so that it contains all of the nodes of the other list.
    * If the other list is empty, your method can return without making any changes to the calling list.

4. Implement the `reverse()` method using either iteration or recursion.

    `reverse()` should reverse the list and set `self.head` to what was previously `self.tail`. It should also set `self.tail` to what was previously `self.head`.

    For example, if the list represents `'hello'`, then `reverse()` should change the list so that it represents `'olleh'`.

    Notes:

    * You may use either iteration or recursion.
    * If list is empty, no action should be taken.

5. Implement the `index_of(c)` function using recursion.

    `index_of(c)` should return the index of the first occurrence of the character `c` in the `LLString`.

    For example, if the linked list represents the string `'banana'`, then `index_of('a')` should return 1.

    Notes:

    * Your solution should use recursion.
    * If the character `c` does not appear in the list, the method should return -1.
    * If the list is empty, your method should return -1.

## Testing

In `test_llstring.py`, there are unit tests for each of the six methods described above. However, these tests are not exhaustive, and you should add your own tests to ensure the correctness of your code.
