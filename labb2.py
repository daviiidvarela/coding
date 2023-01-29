p = [2, 0, 1]
q = [-2, 1, 0, 0, 2]

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
            

        degree += 1

        
        if (len(p_list)==0): 
		        return 0 

    final_string = ' + '.join(terms) # The string ' + ' is used as "glue" between the elements in the string
    return final_string




print(poly_to_string(p))

print(poly_to_string(q))
print(poly_to_string([]))
