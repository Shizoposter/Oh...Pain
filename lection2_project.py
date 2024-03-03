# -*- coding: utf-8 -*-

#Project Second. Vigenere's and Cesaur's cipher.

# Button bg - #4b4d4b
# Text fg - #b1b5b1
# Button activeforeground - #b1b5b1
# Button activebackground - #313331


import string
from tkinter import *
from math import *

def _goBackFunc():
	if rezhim == 'cesaur':
		RD_Cesaur_1.place_forget()
		RD_Cesaur_2.place_forget()
		RD_Cesaur_3.place_forget()
		RD_Cesaur_4.place_forget()
		cesaurInputLabel.place_forget()
		cesaurOutputLabel.place_forget()
		cesaurIndentLabel.place_forget()
		cesaurTextEntryInput.place_forget()
		cesaurTextEntryOutput.place_forget()
		cesaurIndentEntry.place_forget()
		cesaurCipherButton.place_forget()
		_backButton.place_forget()
	elif rezhim == 'vigenere':
		RD_Vigenere_1.place_forget()
		RD_Vigenere_2.place_forget()
		RD_Vigenere_3.place_forget()
		RD_Vigenere_4.place_forget()
		VigenereInputLabel.place_forget()
		VigenereOutputLabel.place_forget()
		VigenereTextEntryInput.place_forget()
		VigenereTextEntryOutput.place_forget()
		VigenereCipherButton.place_forget()
		VigenereKeyEntry.place_forget()
		VigenereKeyLabel.place_forget()
		_backButton.place_forget()

	buttonStartVigenere.place(x = 50, y = 450)
	buttonStartCesaur.place(x = 315, y = 450)
	startMenuLabel.place(x = 85, y = 60)
	rootCanv.place(x = 150, y = 135)
	infoLabel.place(x = 30, y = 560)
#Cesaur's cipher:

def cesaurCipher():
	global rezhim
	rezhim = 'cesaur'
	buttonStartCesaur.place_forget()
	buttonStartVigenere.place_forget()
	startMenuLabel.place_forget()
	rootCanv.place_forget()
	infoLabel.place_forget()

	global like
	global like2
	like = IntVar()
	like.set(None)
	like2 = IntVar()
	like2.set(None)
	global RD_Cesaur_1
	RD_Cesaur_1 = Radiobutton(root,
		text='Encryprion',
		 variable=like,
		  value= 1,
		   font = ('Candara', 20),
		    bg = '#4b4d4b',
		     fg = '#000000')
	global RD_Cesaur_2 
	RD_Cesaur_2 = Radiobutton(root,
	 text = 'Decryption',
	  variable = like,
	   value = 2,
	    font = ('Candara', 20),
	     bg = '#4b4d4b',
	      fg = '#000000')
	global RD_Cesaur_3
	RD_Cesaur_3 = Radiobutton(root,
	 text = 'Russian',
	  variable = like2,
	   value = 1,
	    font = ('Candara', 20),
	     bg = '#4b4d4b',
	      fg = '#000000')
	global RD_Cesaur_4
	RD_Cesaur_4 = Radiobutton(root,
	 text = 'English',
	  variable = like2,
	   value = 2,
	    font = ('Candara', 20),
	     bg = '#4b4d4b',
	      fg = '#000000')
	global cesaurInputLabel
	cesaurInputLabel = Label(root,
	 text = 'Input:',
	  font = ('Candara', 20),
	   fg = '#000000',
	    bg = '#4b4d4b')
	global cesaurOutputLabel
	cesaurOutputLabel = Label(root,
	 text = 'Output:',
	  font = ('Candara', 20),
	   fg = '#000000',
	    bg = '#4b4d4b')
	global cesaurIndentLabel
	cesaurIndentLabel = Label(root,
	 text = 'Indent:',
	  font = ('Candara', 20),
	   fg = '#000000',
	    bg = '#4b4d4b')
	global cesaurTextEntryInput
	cesaurTextEntryInput = Text(root,
	 width = 34,
	  height = 5,
	   bd = 2,
	    bg = '#b1b5b1',
	     font = ('Candara', 15))
	global cesaurTextEntryOutput
	cesaurTextEntryOutput = Text(root,
	 width = 34,
	  height = 5,
	   bd = 2,
	    bg = '#b1b5b1',
	     font = ('Candara', 15))
	global cesaurIndentEntry
	cesaurIndentEntry = Entry(root,
	 width = 15,
	  bd = 2,
	   bg = '#b1b5b1',
	    font = ('Candara', 20))
	global cesaurCipherButton
	cesaurCipherButton = Button(root,
	 width = 15,
	  bd = 2,
	   bg = '#4b4d4b',
	    fg = '#b1b5b1',
	     text = 'Encrypt',
	      font = ('Candara', 20),
	       activeforeground = '#b1b5b1',
	        activebackground = '#313331',
	         command = encryptCesaur)

	RD_Cesaur_1.place(x = 75, y = 50) 
	RD_Cesaur_2.place(x = 75, y = 95)
	RD_Cesaur_3.place(x = 390, y = 50)
	RD_Cesaur_4.place(x = 390, y = 95)
	cesaurInputLabel.place(x = 50, y = 185)
	cesaurOutputLabel.place(x = 30, y = 350)
	cesaurTextEntryInput.place(x = 130, y = 195)
	cesaurTextEntryOutput.place(x = 130, y = 350)
	cesaurCipherButton.place(x  = 190, y = 500)
	cesaurIndentEntry.place(x = 200, y = 145)
	cesaurIndentLabel.place(x = 105, y = 145)
	_backButton.place(x = 265, y = 40)
	cesaurTextEntryOutput['state'] = 'disabled'

def encryptCesaur():
	s = []
	beta = []
	alpha = []
	t = 0
	cesaurTextEntryOutput['state'] = 'normal'
	cesaurTextEntryOutput.delete(1.0, END)
	cesaurTextEntryOutput['state'] = 'disabled'
	if like.get() == 1:
		if like2.get() == 1:
			_getInputText = cesaurTextEntryInput.get(1.0, END)
			_getIndent = cesaurIndentEntry.get()
			for i in _getInputText:
				beta.append(i)
			if 0 < int(_getIndent) < 26:
				if _getIndent.isdigit() == True:
					for i in _getInputText:
						if i in russianAlphabet:
							s.append(russianAlphabet[(russianAlphabet.index(i) + int(_getIndent)) % 66])
						elif i in string.punctuation or i == ' ' or i in list('0123456789'):
							s.append(i)
						else:
							break
							cesaurTextEntryOutput.delete(1.0, END)
							cesaurTextEntryOutput['state'] = 'normal'
							cesaurTextEntryOutput.insert(END, 'Введенный вами текст содержит недопустимые символы!')
							cesaurTextEntryOutput['state'] = 'disabled'
							return
					cesaurTextEntryOutput.delete(1.0, END)
					beta.remove('\n')
					t = 0
					for i in list(_getInputText):
						if list(_getInputText)[t] in string.punctuation or list(_getInputText)[t] == ' ' or list(_getInputText)[t] in list('0123456789'):
							s[t] = s[t]
							t += 1
						elif list(_getInputText)[t] in russianAlphabet and russianAlphabet.index(list(_getInputText)[t]) > 32:
							s[t] = s[t].upper()
							t += 1
						elif list(_getInputText)[t] in russianAlphabet and russianAlphabet.index(list(_getInputText)[t]) <= 32:
							s[t] = s[t].lower()
							t += 1
					cesaurTextEntryOutput.delete(1.0, END)
					cesaurTextEntryOutput['state'] = 'normal'
					cesaurTextEntryOutput.insert(END, ''.join(s))
					cesaurTextEntryOutput['state'] = 'disabled'
				else:
					cesaurTextEntryOutput.delete(1.0, END)
					cesaurTextEntryOutput['state'] = 'normal'
					cesaurTextEntryOutput.insert(END, 'Введенное вами значение отступа должно быть целочисленным!')
					cesaurTextEntryOutput['state'] = 'disabled'
			else:
					cesaurTextEntryOutput.delete(1.0, END)
					cesaurTextEntryOutput['state'] = 'normal'
					cesaurTextEntryOutput.insert(END, 'Введенное вами значение отступа должно быть в диапазоне от 1 до 25!')
					cesaurTextEntryOutput['state'] = 'disabled'
		if like2.get() == 2:
				_getInputText = cesaurTextEntryInput.get(1.0, END)
				_getIndent = cesaurIndentEntry.get()
				for i in _getInputText:
					beta.append(i)
				if 0 < int(_getIndent) < 26:
					if _getIndent.isdigit() == True:
						for i in _getInputText:
							if i in string.ascii_letters:
								s.append(string.ascii_letters[(string.ascii_letters.index(i) + int(_getIndent)) % 52])
							elif i in string.punctuation or i == ' ' or i in list('0123456789'):
								s.append(i)
							else:
								break
								cesaurTextEntryOutput.delete(1.0, END)
								cesaurTextEntryOutput['state'] = 'normal'
								cesaurTextEntryOutput.insert(END, 'Введенный вами текст содержит недопустимые символы!')
								cesaurTextEntryOutput['state'] = 'disabled'
								return
						cesaurTextEntryOutput.delete(1.0, END)
						beta.remove('\n')
						t = 0
						for i in list(_getInputText):
							if list(_getInputText)[t] in string.punctuation or list(_getInputText)[t] == ' ' or list(_getInputText)[t] in list('0123456789'):
								s[t] = s[t]
								t += 1
							elif list(_getInputText)[t] in string.ascii_letters and string.ascii_letters.index(list(_getInputText)[t]) > 25:
								s[t] = s[t].upper()
								t += 1
							elif list(_getInputText)[t] in string.ascii_letters and string.ascii_letters.index(list(_getInputText)[t]) <= 25:
								s[t] = s[t].lower()
								t += 1
						cesaurTextEntryOutput.delete(1.0, END)
						cesaurTextEntryOutput['state'] = 'normal'
						cesaurTextEntryOutput.insert(END, ''.join(s))
						cesaurTextEntryOutput['state'] = 'disabled'
					else:
						cesaurTextEntryOutput.delete(1.0, END)
						cesaurTextEntryOutput['state'] = 'normal'
						cesaurTextEntryOutput.insert(END, 'Введенное вами значение отступа должно быть целочисленным!')
						cesaurTextEntryOutput['state'] = 'disabled'
				else:
						cesaurTextEntryOutput.delete(1.0, END)
						cesaurTextEntryOutput['state'] = 'normal'
						cesaurTextEntryOutput.insert(END, 'Введенное вами значение отступа должно быть в диапазоне от 1 до 25!')
						cesaurTextEntryOutput['state'] = 'disabled'
	elif like.get() == 2:
		if like2.get() == 1:
			_getInputText = cesaurTextEntryInput.get(1.0, END)
			_getIndent = cesaurIndentEntry.get()
			for i in _getInputText:
				beta.append(i)
			if 0 < int(_getIndent) < 26:
				if _getIndent.isdigit() == True:
					for i in _getInputText:
						if i in russianAlphabet:
							s.append(russianAlphabet[((russianAlphabet.index(i) - int(_getIndent) + 66) % 66)])
						elif i in string.punctuation or i == ' ' or i in list('0123456789'):
							s.append(i)
						else:
							break
							cesaurTextEntryOutput.delete(1.0, END)
							cesaurTextEntryOutput['state'] = 'normal'
							cesaurTextEntryOutput.insert(END, 'Введенный вами текст содержит недопустимые символы!')
							cesaurTextEntryOutput['state'] = 'disabled'
							return
					cesaurTextEntryOutput.delete(1.0, END)
					beta.remove('\n')
					t = 0
					for i in list(_getInputText):
						if list(_getInputText)[t] in string.punctuation or list(_getInputText)[t] == ' ' or list(_getInputText)[t] in list('0123456789'):
							s[t] = s[t]
							t += 1
						elif list(_getInputText)[t] in russianAlphabet and russianAlphabet.index(list(_getInputText)[t]) > 32:
							s[t] = s[t].upper()
							t += 1
						elif list(_getInputText)[t] in russianAlphabet and russianAlphabet.index(list(_getInputText)[t]) <= 32:
							s[t] = s[t].lower()
							t += 1
					cesaurTextEntryOutput.delete(1.0, END)
					cesaurTextEntryOutput['state'] = 'normal'
					cesaurTextEntryOutput.insert(END, ''.join(s))
					cesaurTextEntryOutput['state'] = 'disabled'
		elif like2.get() == 2:
			_getInputText = cesaurTextEntryInput.get(1.0, END)
			_getIndent = cesaurIndentEntry.get()
			for i in _getInputText:
				beta.append(i)
			if 0 < int(_getIndent) < 26:
				if _getIndent.isdigit() == True:
					for i in _getInputText:
						if i in string.ascii_letters:
							s.append(string.ascii_letters[((string.ascii_letters.index(i) - int(_getIndent) + 52) % 52)])
						elif i in string.punctuation or i == ' ' or i in list('0123456789'):
							s.append(i)
						else:
							break
							cesaurTextEntryOutput['state'] = 'normal'
							cesaurTextEntryOutput.delete(1.0, END)
							cesaurTextEntryOutput.insert(END, 'Введенный вами текст содержит недопустимые символы!')
							cesaurTextEntryOutput['state'] = 'disabled'
							return
					cesaurTextEntryOutput.delete(1.0, END)
					beta.remove('\n')
					t = 0
					for i in list(_getInputText):
						if list(_getInputText)[t] in string.punctuation or list(_getInputText)[t] == ' ' or list(_getInputText)[t] in list('0123456789'):
							s[t] = s[t]
							t += 1
						elif list(_getInputText)[t] in string.ascii_letters and string.ascii_letters.index(list(_getInputText)[t]) > 25:
							s[t] = s[t].upper()
							t += 1
						elif list(_getInputText)[t] in string.ascii_letters and string.ascii_letters.index(list(_getInputText)[t]) <= 25:
							s[t] = s[t].lower()
							t += 1
					cesaurTextEntryOutput.delete(1.0, END)
					cesaurTextEntryOutput['state'] = 'normal'
					cesaurTextEntryOutput.insert(END, ''.join(s))
					cesaurTextEntryOutput['state'] = 'disabled'

def encryptVigenere():
	#Encrypt(mn) = (Q + mn + kn) % Q
	#где mn - позиция символа открытого текста,
	#kn - позиция символа ключа шифрования,
	#Q - количество символов в алфавите,
	#cn - позиция символа зашифрованного текста.
	s = []
	alpha = []
	beta = []
	gamma = []
	if like3.get() == 1:
		if like4.get() == 1:
			_getInputText = VigenereTextEntryInput.get(1.0, END)
			_getKey = VigenereKeyEntry.get()
			for i in _getKey:
				if str(i) == ' ' or str(i) in string.punctuation:
					VigenereTextEntryOutput['state'] = 'normal'
					VigenereTextEntryOutput.delete(1.0, END)
					VigenereTextEntryOutput.insert(END, 'Ключ не может содержать символы пробела и/или знаки препинания!')
					VigenereTextEntryOutput['state'] = 'disabled'					
					return
				elif i in string.ascii_letters:
					VigenereTextEntryOutput['state'] = 'normal'
					VigenereTextEntryOutput.delete(1.0, END)
					VigenereTextEntryOutput.insert(END, 'Ключ не может содержать символы другого языка!')
					VigenereTextEntryOutput['state'] = 'disabled'
					return
				elif i in list('0123456789'):
					VigenereTextEntryOutput['state'] = 'normal'
					VigenereTextEntryOutput.delete(1.0, END)
					VigenereTextEntryOutput.insert(END, 'Ключ не может содержать цифры!')
					VigenereTextEntryOutput['state'] = 'disabled'
				else:
					beta.append(russianAlphabet.index(i))

			for i in _getInputText:
				if i in string.punctuation or i == ' ':
					alpha.append(i)
				elif i in russianAlphabet:
					alpha.append(russianAlphabet.index(i))
				elif i in list('0123456789'):
					VigenereTextEntryOutput['state'] = 'normal'
					VigenereTextEntryOutput.delete(1.0, END)
					VigenereTextEntryOutput.insert(END, 'Введенный вами текст содержит цифры! Введите необходимое число буквенным способом!')
					VigenereTextEntryOutput['state'] = 'disabled'
					return			
			t = 0
			for i in alpha:
				if str(i) == ' ' or str(i) in string.punctuation:
					s.append(i)
				else:
					if t < len(beta):
						s.append(i + beta[t])
						t += 1
					else:
						t = 0
						s.append(i + beta[t])
						t += 1
			for i in s:
				if str(i) == ' ' or str(i) in string.punctuation:
					continue
				else:
					if i > 65:
						v = s.index(i)
						i = abs(65 - i + 1)
						s[v] = russianAlphabet[i]
					elif i <= 65:
						s[s.index(i)] = russianAlphabet[i]
			t = 0
			for i in alpha:
				if str(i) == ' ' or str(i) in string.punctuation:
					t += 1
					continue
				else:
					if i > 32:
						s[t] = s[t].upper()
						t += 1
					elif i <= 32:
						s[t] = s[t].lower()
						t += 1
			VigenereTextEntryOutput['state'] = 'normal'
			VigenereTextEntryOutput.delete(1.0, END)
			VigenereTextEntryOutput.insert(END, ''.join(s))
			VigenereTextEntryOutput['state'] = 'disabled'





		if like4.get() == 2:
			_getInputText = VigenereTextEntryInput.get(1.0, END)
			_getKey = VigenereKeyEntry.get()
			for i in _getKey:
				if str(i) == ' ' or str(i) in string.punctuation:
					VigenereTextEntryOutput['state'] = 'normal'
					VigenereTextEntryOutput.delete(1.0, END)
					VigenereTextEntryOutput.insert(END, 'Ключ не может содержать символы пробела и/или знаки препинания!')
					VigenereTextEntryOutput['state'] = 'disabled'					
					return
				elif i in russianAlphabet:
					VigenereTextEntryOutput['state'] = 'normal'
					VigenereTextEntryOutput.delete(1.0, END)
					VigenereTextEntryOutput.insert(END, 'Ключ не может содержать символы другого языка!')
					VigenereTextEntryOutput['state'] = 'disabled'
					return
				elif i in list('0123456789'):
					VigenereTextEntryOutput['state'] = 'normal'
					VigenereTextEntryOutput.delete(1.0, END)
					VigenereTextEntryOutput.insert(END, 'Ключ не может содержать цифры!')
					VigenereTextEntryOutput['state'] = 'disabled'
					return
				else:
					beta.append(string.ascii_letters.index(i))

			for i in _getInputText:
				if i in string.punctuation or i == ' ':
					alpha.append(i)
				elif i  in string.ascii_letters:
					alpha.append(string.ascii_letters.index(i))
				elif i in list('0123456789'):
					VigenereTextEntryOutput['state'] = 'normal'
					VigenereTextEntryOutput.delete(1.0, END)
					VigenereTextEntryOutput.insert(END, 'Текст не может содержать цифры! Пожалуйста, введите данное число буквенным способом!')
					VigenereTextEntryOutput['state'] = 'disabled'
					return
				else:
					break
					VigenereTextEntryOutput['state'] = 'normal'
					VigenereTextEntryOutput.delete(1.0, END)
					VigenereTextEntryOutput.insert(END, 'Введенный вами текст содержит недопустимые для выбранного языка символы!')
					VigenereTextEntryOutput['state'] = 'disabled'
					return			
			t = 0
			for i in alpha:
				if str(i) == ' ' or str(i) in string.punctuation:
					s.append(i)
				else:
					if t < len(beta):
						s.append(i + beta[t])
						t += 1
					else:
						t = 0
						s.append(i + beta[t])
						t += 1
			for i in s:
				if str(i) == ' ' or str(i) in string.punctuation:
					continue
				else:
					if i > 51:
						v = s.index(i)
						i = abs(51 - i + 1)
						s[v] = string.ascii_letters[i]
					elif i <= 51:
						s[s.index(i)] = string.ascii_letters[i]
			t = 0
			for i in alpha:
				if str(i) == ' ' or str(i) in string.punctuation:
					t += 1
					continue
				else:
					if i > 25:
						s[t] = s[t].upper()
						t += 1
					elif i <= 25:
						s[t] = s[t].lower()
						t += 1
			VigenereTextEntryOutput['state'] = 'normal'
			VigenereTextEntryOutput.delete(1.0, END)
			VigenereTextEntryOutput.insert(END, ''.join(s))
			VigenereTextEntryOutput['state'] = 'disabled'





	elif like3.get() == 2:
		if like4.get() == 1:
			_getInputText = VigenereTextEntryInput.get(1.0, END)
			_getKey = VigenereKeyEntry.get()
			for i in _getKey:
				if str(i) == ' ' or str(i) in string.punctuation:
					VigenereTextEntryOutput['state'] = 'normal'
					VigenereTextEntryOutput.delete(1.0, END)
					VigenereTextEntryOutput.insert(END, 'Ключ не может содержать символы пробела и/или знаки препинания!')
					VigenereTextEntryOutput['state'] = 'disabled'					
					return
				elif i in string.ascii_letters:
					VigenereTextEntryOutput['state'] = 'normal'
					VigenereTextEntryOutput.delete(1.0, END)
					VigenereTextEntryOutput.insert(END, 'Ключ не может содержать символы другого языка!')
					VigenereTextEntryOutput['state'] = 'disabled'
					return
				else:
					beta.append(russianAlphabet.index(i))

			for i in _getInputText:
				if i in string.punctuation or i == ' ':
					alpha.append(i)
				elif i  in russianAlphabet:
					alpha.append(russianAlphabet.index(i))
				else:
					break
					VigenereTextEntryOutput['state'] = 'normal'
					VigenereTextEntryOutput.delete(1.0, END)
					VigenereTextEntryOutput.insert(END, 'Введенный вами текст содержит недопустимые для выбранного языка символы!')
					VigenereTextEntryOutput['state'] = 'disabled'
					return

			#Decrypt(cn) = (Q + cn - kn) % Q.
			#где mn - позиция символа открытого текста,
			#kn - позиция символа ключа шифрования,
			#Q - количество символов в алфавите,
			#cn - позиция символа зашифрованного текста.			
			
			t = 0
			for i in alpha:
				if str(i) == ' ' or str(i) in string.punctuation:
					s.append(i)
				else:
					if t < len(beta):
						s.append(i - beta[t])
						t += 1
					else:
						t = 0
						s.append(i - beta[t])
						t += 1
			for i in s:
				if str(i) == ' ' or str(i) in string.punctuation:
					continue
				else:
					if i > 65:
						v = s.index(i)
						i = abs(65 - i + 1)
						s[v] = russianAlphabet[i]
					elif i <= 65:
						s[s.index(i)] = russianAlphabet[i]
			t = 0
			for i in alpha:
				if str(i) == ' ' or str(i) in string.punctuation:
					t += 1
					continue
				else:
					if i > 32:
						s[t] = s[t].upper()
						t += 1
					elif i <= 32:
						s[t] = s[t].lower()
						t += 1
			VigenereTextEntryOutput['state'] = 'normal'
			VigenereTextEntryOutput.delete(1.0, END)
			VigenereTextEntryOutput.insert(END, ''.join(s))
			VigenereTextEntryOutput['state'] = 'disabled'

		elif like4.get() == 2:
			_getInputText = VigenereTextEntryInput.get(1.0, END)
			_getKey = VigenereKeyEntry.get()
			for i in _getKey:
				if str(i) == ' ' or str(i) in string.punctuation:
					VigenereTextEntryOutput['state'] = 'normal'
					VigenereTextEntryOutput.delete(1.0, END)
					VigenereTextEntryOutput.insert(END, 'Ключ не может содержать символы пробела и/или знаки препинания!')
					VigenereTextEntryOutput['state'] = 'disabled'					
					return
				elif i in russianAlphabet:
					VigenereTextEntryOutput['state'] = 'normal'
					VigenereTextEntryOutput.delete(1.0, END)
					VigenereTextEntryOutput.insert(END, 'Ключ не может содержать символы другого языка!')
					VigenereTextEntryOutput['state'] = 'disabled'
					return
				else:
					beta.append(string.ascii_letters.index(i))

			for i in _getInputText:
				if i in string.punctuation or i == ' ':
					alpha.append(i)
				elif i  in string.ascii_letters:
					alpha.append(string.ascii_letters.index(i))
				else:
					break
					VigenereTextEntryOutput['state'] = 'normal'
					VigenereTextEntryOutput.delete(1.0, END)
					VigenereTextEntryOutput.insert(END, 'Введенный вами текст содержит недопустимые для выбранного языка символы!')
					VigenereTextEntryOutput['state'] = 'disabled'
					return			
			t = 0
			for i in alpha:
				if str(i) == ' ' or str(i) in string.punctuation:
					s.append(i)
				else:
					if t < len(beta):
						s.append(i - beta[t])
						t += 1
					else:
						t = 0
						s.append(i - beta[t])
						t += 1
			for i in s:
				if str(i) == ' ' or str(i) in string.punctuation:
					continue
				else:
					if i > 51:
						v = s.index(i)
						i = abs(51 - i + 1)
						s[v] = string.ascii_letters[i]
					elif i <= 51:
						s[s.index(i)] = string.ascii_letters[i]
			t = 0
			for i in alpha:
				if str(i) == ' ' or str(i) in string.punctuation:
					t += 1
					continue
				else:
					if i > 25:
						s[t] = s[t].upper()
						t += 1
					elif i <= 25:
						s[t] = s[t].lower()
						t += 1
			VigenereTextEntryOutput['state'] = 'normal'
			VigenereTextEntryOutput.delete(1.0, END)
			VigenereTextEntryOutput.insert(END, ''.join(s))
			VigenereTextEntryOutput['state'] = 'disabled'
#Vigenere's cipher:

def vigenereFunction():
	global rezhim
	rezhim = 'vigenere'
	buttonStartCesaur.place_forget()
	buttonStartVigenere.place_forget()
	startMenuLabel.place_forget()
	rootCanv.place_forget()
	infoLabel.place_forget()

	global like3
	global like4
	like3 = IntVar()
	like3.set(None)
	like4 = IntVar()
	like4.set(None)

	global RD_Vigenere_1
	RD_Vigenere_1 = Radiobutton(root,
		text='Encryprion',
		 variable=like3,
		  value= 1,
		   font = ('Candara', 20),
		    bg = '#4b4d4b',
		     fg = '#000000')
	global RD_Vigenere_2
	RD_Vigenere_2 = Radiobutton(root,
	 text = 'Decryption',
	  variable = like3,
	   value = 2,
	    font = ('Candara', 20),
	     bg = '#4b4d4b',
	      fg = '#000000')
	global RD_Vigenere_3
	RD_Vigenere_3 = Radiobutton(root,
	 text = 'Russian',
	  variable = like4,
	   value = 1,
	    font = ('Candara', 20),
	     bg = '#4b4d4b',
	      fg = '#000000')
	global RD_Vigenere_4
	RD_Vigenere_4 = Radiobutton(root,
	 text = 'English',
	  variable = like4,
	   value = 2,
	    font = ('Candara', 20),
	     bg = '#4b4d4b',
	      fg = '#000000')
	global VigenereInputLabel
	VigenereInputLabel = Label(root,
	 text = 'Input:',
	  font = ('Candara', 20),
	   fg = '#000000',
	    bg = '#4b4d4b')
	global VigenereOutputLabel
	VigenereOutputLabel = Label(root,
	 text = 'Output:',
	  font = ('Candara', 20),
	   fg = '#000000',
	    bg = '#4b4d4b')
	global VigenereKeyLabel
	VigenereKeyLabel = Label(root,
	 text = 'Key:',
	  font = ('Candara', 20),
	   fg = '#000000',
	    bg = '#4b4d4b')
	global VigenereTextEntryInput
	VigenereTextEntryInput = Text(root,
	 width = 34,
	  height = 5,
	   bd = 2,
	    bg = '#b1b5b1',
	     font = ('Candara', 15))
	global VigenereTextEntryOutput
	VigenereTextEntryOutput = Text(root,
	 width = 34,
	  height = 5,
	   bd = 2,
	    bg = '#b1b5b1',
	     font = ('Candara', 15))
	global VigenereKeyEntry
	VigenereKeyEntry = Entry(root,
	 width = 15,
	  bd = 2,
	   bg = '#b1b5b1',
	    font = ('Candara', 20))
	global VigenereCipherButton
	VigenereCipherButton = Button(root,
	 width = 15,
	  bd = 2,
	   bg = '#4b4d4b',
	    fg = '#b1b5b1',
	     text = 'Encrypt',
	      font = ('Candara', 20),
	       activeforeground = '#b1b5b1',
	        activebackground = '#313331',
	         command = encryptVigenere)

	RD_Vigenere_1.place(x = 75, y = 50) 
	RD_Vigenere_2.place(x = 75, y = 95)
	RD_Vigenere_3.place(x = 390, y = 50)
	RD_Vigenere_4.place(x = 390, y = 95)
	VigenereInputLabel.place(x = 50, y = 185)
	VigenereOutputLabel.place(x = 30, y = 350)
	VigenereTextEntryInput.place(x = 130, y = 195)
	VigenereTextEntryOutput.place(x = 130, y = 350)
	VigenereCipherButton.place(x  = 190, y = 500)
	VigenereKeyEntry.place(x = 200, y = 145)
	VigenereKeyLabel.place(x = 125, y = 145)
	_backButton.place(x = 265, y = 40)
	VigenereTextEntryOutput['state'] = 'disabled'


				
cesaurInput_Massive = []
russianAlphabet = ['а','б','в','г','д','е','ё','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я','А','Б','В','Г','Д','Е','Ё','Ж','З','И','Й','К','Л','М','Н','О','П','Р','С','Т','У','Ф','Х','Ц','Ч','Ш','Щ','Ъ','Ы','Ь','Э','Ю','Я']
russianAlphabetLower = ['а','б','в','г','д','е','ё','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я']
root = Tk()
root.geometry('600x600')
root.resizable(False, False)
root.title('Vigenere\'s and Cesaur\'s cipher.')
root['bg'] = '#4b4d4b'

rootCanv = Canvas(root, width = 256, height = 256, bg = '#4b4d4b', bd=0, highlightthickness=0)
rootCanv.place(x = 150, y = 135)
logoPath = PhotoImage(file = 'lec2_logo.gif')
logoPlace = rootCanv.create_image(145, 135, anchor = CENTER, image = logoPath)

buttonStartCesaur = Button(root, width = 15, text = 'Cesaur', font = ('Candara', 20), bd = 2, bg = '#4b4d4b', fg = '#b1b5b1', activeforeground = '#b1b5b1', activebackground = '#313331', command = cesaurCipher)
buttonStartVigenere = Button(root, width = 15, text = 'Vigenere', font = ('Candara', 20), bd = 2, bg = '#4b4d4b', fg = '#b1b5b1', activeforeground = '#b1b5b1', activebackground = '#313331', command = vigenereFunction)
startMenuLabel = Label(root, text = 'Vigenere\'s and Cesaur\'s cipher.', font = ('Candara', 25), fg = '#b1b5b1', bg = '#4b4d4b')
infoLabel = Label(root, text = 'Written by Ushakov Kirill - Yota <yotahole850@gmail.com>', fg = '#b1b5b1', bg = '#4b4d4b', font = ('Candara', 15))
_backButton = Button(root,
	width = 7,
	height = 1,
	text = 'В меню.',
	bg = '#4b4d4b',
	fg = '#b1b5b1',
	bd = 2,
	font = ('Candara', 15),
	activeforeground = '#b1b5b1',
	activebackground = '#313331',
	command = _goBackFunc)
buttonStartVigenere.place(x = 50, y = 450)
buttonStartCesaur.place(x = 315, y = 450)
startMenuLabel.place(x = 85, y = 60)
infoLabel.place(x = 30, y = 560)

root.mainloop()