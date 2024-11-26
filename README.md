"# EECS510_Project" 

Execution:
	Ensure 'tester.py' and 'automaton.py' files are within the same directory.
	If using a test file, ensure it is also within the directory.
	Run with your favorite Python3 interperter. Note: this code was developed in Python 3.9.
	The code has been verified to run on the EECS cycle servers.
	To run on the cycle servers, use command "python3 tester.py".

Test file:
	When using a test file, the user provides the filename to the program.
	In the file, each line is a seperate test case. Each test case consists of an input string
	and an expected result. These are whitespace delineated. The expected results should be
	"ACCEPTED" or "REJECTED". If the expected result matches the result returned by the machine,
	the testing will return 'Success', regardless of if the string was accepted or not. If the
	expected result does not match the returned result from the machine, the testing will return
	'Failure'. Thus, if the expected result in not "ACCEPTED" or "REJECTED", the testing will
	always return 'Failure'. If an expected result is not provided in the test case, the testing
	will return 'Inconclusive'. Any additional information provided after the expected result
	(within the same line) will be ignored.
	Example test cases:
		1+7 ACCEPTED
		1a+5 REJECTED
