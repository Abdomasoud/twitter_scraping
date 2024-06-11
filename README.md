# README

This README file provides instructions on how to set up a virtual environment (venv) to test the code in `main.py` in your local environment.

## Prerequisites

Before setting up the venv, make sure you have the following installed on your system:

- Python
- pip

## Setting up the Virtual Environment

1. Open a terminal or command prompt.

2. Navigate to the directory where `main.py` is located.

3. Create a new virtual environment by running the following command:

   ```
   python -m venv myenv
   ```

   This will create a new directory named `myenv` which will contain the virtual environment.

4. Activate the virtual environment by running the appropriate command for your operating system:

   - For Windows:

     ```
     myenv\Scripts\activate
     ```

   - For macOS/Linux:

     ```
     source myenv/bin/activate
     ```

5. Install the required dependencies by running the following command:

   ```
   pip install requests beautifulsoup4 schedule
   ```

## Testing the Code

Once the virtual environment is set up and the dependencies are installed, you can now test the code in `main.py` in your local environment.

1. Run the following command to execute the code:

   ```
   python main.py
   ```

   This will run the `main.py` file and execute the code.

2. Verify that the code is working as expected and producing the desired output.

## Author

Abdulrhman Masoud Ibrahim
