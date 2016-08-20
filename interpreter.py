""""
Project: The Interpreter
Coders: Makrand Bhale, Gunvant Sarpate, Akshay Nair
Version: Beta 0.1
Date: 20 August 2016
Reference: Google ;)
Guide: Mr.Deshpande G.S.
""""
import sys
def main():
	#input taken from user as list
	numbers = [1]
	problem=[
		str(x) for x in input().split()
		]
	n=len(problem)
	#print(n)
	
	#Module by Makrand Bhale.
	#sorting integers from list
	j = 0
	for i in problem:
		if (i.isdigit()):
			numbers.insert(j, i)
			#print(numbers[j])
			j = j + 1
			
	#Storing values from last index of list
	num1=(numbers[0])
	num2=(numbers[1])
	
	#finding keywords from list
	
	
	# changes made by Makrand
	
	if "add" in problem:
		add(num1,num2)
	elif "sub" in problem:
		sub(num1,num2)
	elif "mult" in problem:
		mult(num1,num2)
	elif "div" in problem:
		div(num1,num2)
	else:
		print ("Error, Sorry we are working on it")
		
def add(num1,num2):
	print(int(num1)+int(num2))
def sub(num1,num2):
	print(int(num1)-int(num2))
def mult(num1,num2):
	print(int(num1)*int(num2))
def div(num1,num2):
	print(int(num1)/int(num2))
main()
