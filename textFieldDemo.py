"""
Program: textFieldDemo.py
Chapter 8 (Page 263)
1/18/2024

**NOTE: The module breezypythongui.py
MUST be in the same directory as this
file for the app to run correctly.

Template code for any GUI-based application in Chapter 9
"""
from breezypythongui import EasyFrame
# Other imports go here.

# Class header (class name will change from project to project.)
class TextFieldDemo(EasyFrame):
	#Definition of our classes' constructor method
	def __init__(self):
		# Call to the EasyFrame class constructor.
		EasyFrame.__init__(self, title = "Text Field Demo", width = 280, height = 160, background = "skyblue")

	# Label and entry field for the input.
		self.addLabel(text = "Input", row = 0, column = 0, background  = "skyblue")
		self.inputField = self.addTextField(text = "", row = 0, column = 1)
		self.inputField["background"] = "khaki" 

		# Label and entry field for output
		self.addLabel(text = "Output", row = 1, column = 0, background = "skyblue")
		self.outputField = self.addTextField(text = "", row = 1, column = 1, state = "readonly")
		
		# The command button which triggers the convert() function
		self.addButton(text = "Convert", row = 2, column = 0, columnspan = 2, command = self.convert)

	# Definition of the convert method.
	def convert(self):
		""" Collects the input string, converts it to
		uppercase and output the results."""
		text = self.inputField.getText()
		result = text.upper()
		self.outputField.setText(result)

#Global definition of the main() method.
def main():
	# Instantiate an object from the class into mainLoop()
	TextFieldDemo().mainloop()

# Global call to main() for program entry.
if __name__ == '__main__':
	main()



