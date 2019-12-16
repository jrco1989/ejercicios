# funciones recursivas 

import random 

def binary_search(data, target, low, high):
	if low >high:
		return False
	mid=(low+high)//2
	if target== data[mid]:
		return True
	elif target<data[mid]: 
		return binary_search(data, target, low, mid -1)
	else:
		return binary_search(data, target, mid +1, high )

def factorial (number):
	if number==0 or number ==1:
		return 1
	elif number>1:
		return number*factorial(number-1)


if __name__=='__main__': #de esta manera se genera el punto de ingreso 
	data=[]
	data=[random.randint(0,100) for i in range(100)]
	data.sort()
	print (data)
	target=int( input( 'what number would you like to find?'))
	found=binary_search(data, target, 0, len(data)-1)
	print (found)


if __name__=="__main__":
	number=int (input('Enter the number to calculate your factorial'))
	result=factorial(number)
	print('the factorial of {} is {}'.format(number,result))

