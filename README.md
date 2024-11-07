[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/qni6VKhf)
<h1>CS151 Lab 9</h1>

 <h3>🔴 DO NOT Start to code before the instructor Approve your algorithm, and test cases🔴</h3>

- **Grade: EMRN**
- **Due: Before Next Lab**

<h3>Table of contents</h3>

<!-- TOC -->
  * [`Problem`](#problem)
  * [`Purpose`](#purpose)
  * [`Details`](#details)
    * [File details](#file-details)
    * [Input](#input-)
    * [Output](#output)
    * [Programming Details](#programming-details)
  * [`Design`](#design)
    * [Function design](#function-design-)
  * [`Steps`](#steps)
  * [`What to Submit in GitHub`](#what-to-submit-in-github)
<!-- TOC -->

## `Problem`
You are organizing a dinner party with assigned seats. 
- Create a program to read in all the attendees and then output the seat assignments.

## `Purpose`
This lab gives you practice with: 
* Following problem-solving techniques
* Using for loops
* Doing file I/O
* Storing data in lists
* Processing a list

## `Details`

We want to have a class dinner party at the end of the semester. 
- Catering services will provide as many tables as we need, with each table seating five people. 
- Your goal is to determine and output:
  1. How many tables are needed? 
  2. Who is sitting at each table?


### File details
You have three different files with all the students names as well as the instructor's name for each CS151 instructor.  
- There is one name per line in a file. 
- All files share the same format, so your code should work for any file without modification if written correctly!

### Input 
You must ask the user the name of the file to read the names from.
- You can then read that file to input the data from the file (i.e. Read the data from the file into a list).

### Output
 
Determine and output how many tables we will need. 
- Fortunately the `number of attendees is a multiple of 5` in each file.

We will need name signs to go at each seat. 
- Each sign should have table number, seat number and guest's name. 
- The output on seating assignments should be similar in style to:

```
~~~~~~~~~~~~~~~~~~~~~~~
Table 1, Seat 1, Jones
~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~
Table 1, Seat 2, Smith
~~~~~~~~~~~~~~~~~~~~~~~
```

### Programming Details
Your program must read in all the information stored in the file, and store it in a list before doing any processing.
- You must use for loops.
- Make sure your input/output follows good usability rules.
- Use iterative development as you design algorithm and write code. Test as you go.

## `Design`
You must design your functions and their algorithms before you start coding. 
- Think about the tasks that need to be solved. Be sure to look back at yesterday’s notes, as the setup is much the same.
### Function design 
  Use the guidelines for creating a function
  -  **In algorithm**
  ```
  # Purpose:  [what problem does the function solve?]
  # Name: [The proposed name of the function]
  # Parameters: [list with purpose in the same order they appear in the function header]
  # Return: [return value, it's type, and what it represents]
  # Algorithm:
  ```
  - **In Code**
  ```
  # Purpose:  [what problem does the function solve?]
  # Parameters: [list with purpose in the same order they appear in the function header]
  # Return: [return value, it's type, and what it represents]
  ```

## `Steps`
1. Make sure you understand the problem
2. Determine the functions you need to solve this problem. 
   - `Remember that a function solves a high level task for the program.` 
   - Then write your algorithm for the function that determines the seating arrangement 
   <br> (you do not need to write the rest of the algorithms, but you do need to figure out what functions you need). 
   - **Take turns driving. Have your design approved by the professor before you start your code.**
3. Write your code.
   - Follow iterative development like you did in design – get one part working completely before moving on to the next part. 
   - Test it as you write it! **take turns driving**
4. Test your code to make sure it is working correctly. 
   - You may need to add some extra print statements to see what values are being used, or the value of the list (remove them for your final version).  
   - **Be sure to test with all input files.**
5. Write comments in your code to make it clear what it is doing.
6. Write comments for each function in your code. 
   - Use the Function Design guidelines
7. Include an updated version of the intro comments. 
   - Note the new final line below about `Input files`. 
   - Be sure to note that you need input files that contain one name per line! 
```
# Programmers:  [your names here]
# Course:  CS151, [Instructors Name]
# Due Date: [date assignment is due]
# Lab Assignment:  [number of assignment]
# Problem Statement:  [what problem does your code solve; i.e., calculating inches from centimeters]
# Data In: [what information do you request from the user?]
# Data Out:  [What information do you display for the user?]
# Credits: [Is your code based of an example in the book, in class, or something else?  Reminder: you should never take code from the Internet or another person.]
# Input Files: [description of the format of the input files you need for this program to work]
```


## `What to Submit in GitHub`

1. Completed `main.py` file  
2. `algorithm.md`
3. Encrypt your files using the `keys` and `process_reflection.py`
   1. `RD1.md` -> Reflection for Drive 1
   2. `RD2.md` -> Reflection for Drive 2
   3. If you use a different key, it is considered unsubmitted

**As a reminder, reflections count toward your participation grade.**

Type the Reflection INSIDE the respective Word file and addressing the following questions:

 - Objective:
   - What were you supposed to learn/accomplish?

 - Procedure:
   - What steps were followed and what techniques did you use to solve the problem?
   - What were the Key concepts explored?

 - Results:
   - Did your results match what you expected to get?
   - Did you try using various test cases, or extreme test cases?
  
 - Reflection:
   - What challenges did you encounter? 
   - How did you follow the first 3 rules of programming?
   - Did you overcome them, and how? 
   - Any key takeaways? 
   - Do you think you learned what you were supposed to learn for this lab? 
   - What was it like working with your partner?

**Make sure the file in your PyCharm and Github is the same (i.e. Commit and Push)**