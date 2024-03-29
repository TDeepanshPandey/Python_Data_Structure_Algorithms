# Python_Data_Structure_Algorithms
 
Big O Cheat sheet (Time Complexity) - *https://www.bigocheatsheet.com/*

### Array Problems - 
1. **Anagram Check** - Given two strings, check to see if they are anagrams. An anagram is when the two strings can be written using the exact same letters (so you can just rearrange the letters to get a different phrase or word). 
2. **Array Pair Sum** - Given an integer array, output all the *unique* pairs that sum up to a specific value **k**.
3. **Find the Missing Element** - Consider an array of non-negative integers. A second array is formed by shuffling the elements of the first array and deleting a random element. Given these two arrays, find which element is missing in the second array.
4. **Largest Continuous Sum** - Given an array of integers (positive and negative) find the largest continuous sum. 
5. **Sentence Reversal** - Given a string of words, reverse all the words.
6. **String Compression** - Given a string in the form 'AAAABBBBCCCCCDDEEEE' compress it to become 'A4B4C5D2E4'. For this problem, you can falsely "compress" strings of single or double letters. For instance, it is okay for 'AAB' to return 'A2B1' even though this technically takes more space.
7. **Unique Characters in String** - Given a string,determine if it is compreised of all unique characters. For example, the string 'abcde' has all unique characters and should return True. The string 'aabcde' contains duplicate characters and should return false.

### Stacks
1. **Implement a stack** - Try your best to implement your own stack! It should have the methods:
    * Check if its empty
    * Push a new item
    * Pop an item
    * Peek at the top item
    * Return the size
2. **Implement a queue** - A queue class should be able to do this:
    * Check if Queue is Empty
    * Enqueue
    * Dequeue
    * Return the size of the Queue
3. **Implement a Deque** - A Deque class with the following methods:
    * Check if its empty
    * Add to both front and rear
    * Remove from Front and Rear
    * Check the Size
4. **Balanced Parenthesis Check** - Given a string of opening and closing parentheses, check whether it’s balanced. We have 3 types of parentheses: round brackets: (), square brackets: [], and curly brackets: {}. Assume that the string doesn’t contain any other character than these, no spaces words or numbers. As a reminder, balanced parentheses require every opening parenthesis to be closed in the reverse order opened. For example ‘([])’ is balanced but ‘([)]’ is not. 

### Linked List
1. **Singly Linked List Cycle Check** - Given a singly linked list, write a function which takes in the first node in a singly linked list and returns a boolean indicating if the linked list contains a "cycle". A cycle is when a node's next point actually points back to a previous node in the list. This is also sometimes known as a circularly linked list.
2. **Linked List Reversal** - A function to reverse a Linked List in place. The function will take in the head of the list as input and return the new head of the list.
3. **Linked List Nth to Last Node** - A function that takes a head node and an integer value **n** and then returns the nth to last node in the linked list.
4. **Doubly Linked List** - Implement a node class and show how it can be used to create a doubly linked list.
5. **Singly Linked List** - Create a node class and show how it can be used to create a Singly Linked List.

### Recursion
1. **Recurring Sum** - A recursive function which takes an integer and computes the cumulative sum of 0 to that integer.
2. **Sum of All Individual Digits** - A function which returns the sum of all the individual digits in that integer.
3. **Word Splitting** - A function which takes in a string **phrase** and a set **list_of_words**. The function will then determine if it is possible to split the string in a way in which words can be made from the list of words. You can assume the phrase will only contain words found in the dictionary if it is completely splittable.
4. **Reverse a String** -  Reverse a string using recursion. Make sure to think of the base case here.
5. **Fibonnaci Sequence** - Implement a Fibonnaci Sequence in three different ways:
    * Recursively
    * Dynamically (Using Memoization to store results)
    * Iteratively