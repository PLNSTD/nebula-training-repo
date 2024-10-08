### **Modules and Importing in Python Assignment: Git and GitHub Edition**

## **Objective**

This assignment deepens your understanding of Python modules, including the Standard Library, external libraries, and custom modules, while also introducing essential version control practices using Git and GitHub. You'll apply what you've learned about modules by completing programming tasks and then practice committing your code to a GitHub repository.

## **Git and GitHub Instructions**

After completing each task, you'll use Git and GitHub to submit your work. Here's a step-by-step guide:

### **Step 1: Create a New Repository**

1. Log into your GitHub account and create a new repository named "PythonModulesAssignment".
2. Initialize it with a README file. This will help others understand what your project is about.

### **Step 2: Clone the Repository**

1. On your computer, open a terminal or command prompt.
2. Clone the repository using the command: `git clone <repository-URL>`. You can find the URL on your repository's page on GitHub.

### **Step 3: Add Your Assignment**

1. Move your assignment files into the cloned repository's folder on your computer.
2. Use the terminal or command prompt to navigate into the repository folder.
3. Add your files to the repository with the command: `git add .`

### **Step 4: Commit Changes**

1. Commit your added files with the command: `git commit -m "Completed Python modules assignment"`. The message in quotes should describe what you're committing.

### **Step 5: Push to GitHub**

1. Push your commits to GitHub with the command: `git push origin master`. If you're using a different branch, replace `master` with your branch name.

### **Step 6: Submit Your Work**

1. On GitHub, navigate to your repository page. Your files should now be visible there.
2. Submit the link to your repository as your assignment submission.

## **Assignment Tasks**

### **Exercise 1: Working with Standard Library Modules**

- **Task 1.1:** Use the `math` module to calculate the square root of 144.
- **Task 1.2:** Utilize the `datetime` module to display today's date.
- **Task 1.3:** Generate a random integer between 1 and 10 with the `random` module.

### **Exercise 2: Using External Libraries**

- **Task 2.1:** Install `numpy` and create a 1D array of numbers from 1 to 5.

### **Exercise 3: Custom Module Creation**

- **Task 3.1:** Develop a `utilities.py` module with a `multiply` function. Use this in a separate script.

### **Exercise 4: Package Management with `pip` **

- **Task 4.1:** Create a virtual environment and install the `requests` package.
  > Quick Explanation of how to use VENV and PIP:
  >
  > - Open a terminal or command prompt.
  > - Navigate to the directory where you want to create the virtual environment.
  > - Run `python -m venv <name-of-environment>` to create the virtual environment.
  > - Run `source <name-of-environment>/bin/activate` on Mac/Linux or `<name-of-environment>\Scripts\activate` on Windows to activate the virtual environment.
  > - Run `pip install requests` to install the `requests` package.
  > - Run `pip list` to see the installed packages.
  > - Screenshot your list of packages.
  > - Run `deactivate` to exit the virtual environment.
  >   Additional documentation can be found [here](https://docs.python.org/3/library/venv.html)

## CREATE .gitignore WITH LINES "your-virtual-env \_\_pycache\_\_"

## **Submission Requirements**

- A GitHub repository containing:
  - Python scripts for Exercises 1, 2, and 3.
  - A `requirements.txt` file for Exercise 4.
  - (Optional) A screenshot in the repository showing the output of `pip list` in your virtual environment, demonstrating the installed `requests` package.
  - Ensure all code is well-commented and formatted.

## **Evaluation Criteria**

- Correct implementation and documentation of Python module tasks.
- Proper use of Git for version control and GitHub for code submission.
- Clean, readable code and repository organization.

This assignment not only tests your Python skills but also introduces you to version control, an essential skill for any programmer. Good luck, and remember to commit frequently!
