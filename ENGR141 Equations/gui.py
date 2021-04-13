import PySimpleGUI as sg
import mymath

sg.theme("DarkGrey")

layout = [[sg.Text("Functions for Statics Engineering",font=("Helvetica", 20))],
			[sg.Text("")],
			[sg.Text("Vector A: ",font=("Helvetica", 12)),sg.Input(key = 'Ai',size=(20,1)),sg.Text("i\t"),sg.Input(key = 'Aj',size=(20,1)),sg.Text("j\t"),sg.Input(key = 'Ak',size=(20,1)),sg.Text("k")],
			[sg.Text("")],
			[sg.Text("Vector B: ",font=("Helvetica", 12)),sg.Input(key = 'Bi',size=(20,1)),sg.Text("i\t"),sg.Input(key = 'Bj',size=(20,1)),sg.Text("j\t"),sg.Input(key = 'Bk',size=(20,1)),sg.Text("k")],
			[sg.Text("_"*100)],
			[sg.Button("Find Magnitude of A",key = "mag")],
			[sg.Button("Find Unit of A",key = "unit")],
			[sg.Button("Find Dot Product",key = "dot")],
			[sg.Button("Find \'A\' Projected onto \'B\'",key = "dotproj")],
			[sg.Button("Find Angle between \'A\' and \'B\'",key = "angle")],
			[sg.Button("Find Cross Product",key = "cross")],
			[sg.Txt('', size=(100,1), key='output',font=("Helvetica", 20))],
			[sg.Text("▅"*100)],
			[sg.Button("Confirm",key = "Confirm")],
			[sg.Button("Quit",key = "Quit")]]

window = sg.Window("Statics Equations",layout)

while True:
	event,value = window.Read()
	
	if event == sg.WINDOW_CLOSED or event == "Quit":
		break

	A = [value['Ai'],value['Aj'],value['Ak']]
	B = [value['Bi'],value['Bj'],value['Bk']]
	try:
		for x,y in enumerate(A):
			if y == '' or y ==None:
				A[x] = 0
			A[x] = int(A[x])
		for x,y in enumerate(B):
			if y == '' or y ==None:
				B[x] = 0
			B[x] = int(B[x])
	except:
		s = "Please enter only numbers"
	s = "Your vectors are... A: " + mymath.pV(A) + " and B: " + mymath.pV(B)

	if event == 'mag':
		r = mymath.findMag(A)
		format(r,".4f")
		s = "The Magnitude of A is: " + str(r)
	if event == 'unit':
		s = "The Unit of A is: " + str(mymath.pV(mymath.findUnit(A)))
	if event == 'dot':
		s = "The Dot Product between A and B is: " + str(mymath.dotProduct(A,B))
	if event == 'dotproj':
		s = "A Projected onto B is: " + mymath.pV(mymath.vectorDotProduct(A,B))
	if event == 'angle':
		s = "The angle between A and B is: " + str(mymath.angleBetween(A,B))
	if event == 'cross':
		s = "The cross product between A and B is: " + mymath.pV(mymath.crossProduct(A,B))

	window['output'].update(s,text_color = "yellow")

