p = [2, 0, 1, 0]
q = [-2, 1, 0, 0, 2]
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
        elif degree == 1 and coeff > 0 or coeff < 0:
            if coeff == 1:
                terms.append('x')    
            else:
                terms.append(str(coeff) + 'x')
        if degree > 1 and coeff > 1:
            term = str(coeff) + 'x^' + str(degree)
            terms.append(term)
        if degree > 1 and coeff == 1:
            term = 'x^' + str(degree)
            terms.append(term)
        if coeff == 0:
            term = str()
            return str()
        degree += 1
        if (len(p_list)==0): 
		        return 0 
        
    final_string=' + '.join(terms) # The string ' + ' is used as "glue" between the elements in the string
    return final_string

def drop_zeroes(p_list):
            while p_list[-1] == 0:
                return p_list.pop()

def eq_poly(p_list, q_list):
    if p_list == q_list:
        return True
    else:
        return False

#def eval_poly(p_list, x):
#    return coeff * x ** degree



print(poly_to_string(p))
#print(poly_to_string(q))
#print(eq_poly(p,p0))
#print(drop_zeroes(q0))
#eval_poly(p0, 1)