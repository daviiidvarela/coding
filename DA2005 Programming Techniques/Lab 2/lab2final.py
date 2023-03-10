p = [2, 0, 1]
q = [-2, 1, 0, 0, 1]
p0 = [2,0,1,0]
q0 = [0,0,0]

def poly_to_string(p_list):
    '''
    Return a string with a nice readable version of the polynomial given in p_list.
    '''
    terms = []
    degree = 0

    # Collect a list of terms
    for coeff in p_list:
        if degree == 0:
            terms.append(str(coeff))
        if degree == 1 and coeff != 0:
            if coeff == 1:
                terms.append('x')    
            else:
                terms.append(str(coeff) + 'x')
        if degree > 1 and coeff != 0:
            if coeff == 1:
                term = 'x^' + str(degree)
                terms.append(term)
            elif coeff == -1:
                term = '-x^' + str(degree)
                terms.append(term)
            else:
                term = str(coeff) + 'x^' + str(degree)
                terms.append(term)
        degree += 1
        

    final_string = ' + '.join(terms) # The string ' + ' is used as "glue" between the elements in the string
    if (len(p_list) == 0): 
        return 0 
    else:
        return final_string

def drop_zeroes(p_list):
    while len(p_list) != 0: 
        if p_list[-1] == 0 :
            p_list.pop()
        else: 
            break
    return p_list
drop_zeroes(p0)
drop_zeroes(q0)

def eq_poly(p_list, q_list):
    if p_list == q_list:
        return True
    else:
        return False

def eval_poly(p_list, x):
	accelerator = 0
	for c in reversed(p_list):
		accelerator = accelerator * x + c
	return accelerator

def neg_poly(p_list):
    for x in range(len(p_list)):
        p_list[x] = -p_list[x]
        return p_list


#print(poly_to_string(p0))
#print(drop_zeroes([]))

#print(eq_poly(q0, []))
#print(eval_poly(q,-2))
print(neg_poly(p))