"""Program to solve system of equation by substittution."""""
import re
import copy

_functions = [
    "x+2y= 12",
    "3y -4z = 25",
    "x+6y+z = 20"
]

_parsed_functions =[]



_function_re = re.compile(r"[+-]?\d*[a-zA-Z]*")
_expression_re = re.compile(r"([+-]?)(\d*)([a-zA-Z]*)")

def parse_expression(exp):
    match=_expression_re.match(exp)
    sign = "+" if  match.group(1)!='-' else '-'  
    variable = match.group(3) 
    number = '1' if match.group(2) == ''  and variable != '' else match.group(2)
    return [sign,number,variable,]
    


def parse_function(f):
    f=f.replace(" ","")
    split_function = f.split("=")
    left =[parse_expression(u) for u in  _function_re.findall(split_function[0]) if u !='']
    right = [parse_expression(u) for u in  _function_re.findall(split_function[1]) if u !='']
    return [left,right]
    

def set_function_to_zero(f):
    """puts function  in x+y+z+# = 0 form if not already in it"""
    new_function = [copy.deepcopy(f[0]),[['+','0','']]]
    for exp in f[1]:
        exp[0] = '-' if  exp[0] == '+' else '+'
        new_function[0].append(exp)
    return new_function

def normalize_function(f):
    """puts function  in x+y+z =# form if not already in it"""
    new_function = [copy.deepcopy(f[0]),[]]
    for exp in f[1]:
        if exp[2] != '':
            exp[0] = '-' if  exp[0] == '+' else '+'
            new_function[0].append(exp)
        else:
            new_function[1].append(exp)
    return new_function

def create_list_variables(f):
    """Creates a list of all variables to be found in a set of functions."""
    variables = []
    print (f"function: {f}")
    for function in f:
        for exp in function[0]:
            if exp[2] !='' and exp[2] not in variables:
                variables.append(exp[2])
        print (f"temp3: {function[1]}")
        for exp in function[1]:
            print(f"exp3: {exp}")
            if exp[2] != '' and exp[2] not in variables:
                variables.append(exp[2])
    return variables
    
def isolate_variable(v, f):
    """puts function  in v = rest form """
    new_function = [[],[]]
    for exp  in f[0]:
        if exp[2] == v:
            new_function[0].append(exp[:])
        else:
            exp[0] = '-' if  exp[0] == '+' else '+'
            new_function[1].append(exp[:])
            new_function[1][-1][0] = '-' if exp[0] == '+' else '+'
    if new_function[0] == []:
        return []
    if new_function[0][0][0] == '-':
        new_function[0][0][0] = '+'
        for index, exp in enumerate(new_function[1]):
            new_function[1][index][0] = '-' if  new_function[1][index][0] == '+' else '+'  
    if new_function[0][0][1] != '1':
        value = int(new_function[0][0][1])
        new_function[0][0][1] = '1'
        for index, exp in enumerate(new_function[1]):
            #new_function[1][index][1] = str(float(new_function[1][index][1])/float(value)   )
            new_function[1][index][1] = f"({new_function[1][index][1]}/{str(value)})"
    return new_function        
    
def create_isolated_functions(parsed_functions):
    """Given parsed function create all possible functions for substitution."""
    variable_list  = create_list_variables(parsed_functions)
    temp_functions = []
    for f in parsed_functions:
        for v in variable_list:
            temp_functions.append(isolate_variable(v,f))
            print (f"temp1: {temp_functions[-1]}")
            if temp_functions[-1] == []:
                print ("deleting")
                del temp_functions[-1]
    return temp_functions            


def add_exp (e1,e2):
    """Adds to expressions"""
    n1 = int(e1[1] if e1[0] == '+' else -1*int (e1[1]) )
    n2 = int(e2[1] if e2[0] == '+' else -1*int (e2[1]) )
    n1 += n2
    if n1 == 0:
        return []
    if n1 < 0:
        return ['-',str(-1*n1),e1[2]]
    return ['+',str(n1),e1[2]]

def combine_like_variables(f):
    """combines like variables"""
    new_function = [[],copy.deepcopy(f[1])]
    while f[0]:
        exp = f[0].pop(0)
        found = -1
        for index, value in  enumerate (new_function[0]):
            if exp[2] == value[2]: 
                found = index
                break
        if found > -1:
            new_function[0][index] = add_exp(new_function[0][index], exp)
            if new_function[0][index] == []:
                del new_function[0][index]
        else:
            new_function[0].append(exp)
    return new_function

def get_function_string (f):
    function_string = "" 
    for exp in f[0]:
        function_string += ''.join(exp) 
    function_string += " = "
    if f[1]:
        for exp in f[1]:
            function_string += ''.join(exp) 
    else:
        function_string += "0"
    return function_string

for f in _functions:
    _parsed_functions.append(parse_function(f))
    
_temp_functions = copy.deepcopy(_parsed_functions)    
_zero_functions = []
for f in _temp_functions:
    _zero_functions.append(set_function_to_zero(f))    
    
print ("Zero functions:")
for f in _zero_functions:
    print (get_function_string(f))

_temp_functions = copy.deepcopy(_zero_functions)
_equal_functions = []
print ("Functions set equal to each other:")
while _temp_functions:
    f1 = _temp_functions.pop()
    for f2 in _temp_functions:
        _equal_functions.append([f1[0],f2[0]])
    
for f in _equal_functions:
    print(get_function_string(f))
 
_combined_functions = []
for f in _equal_functions:
    temp_function = set_function_to_zero(f)
    _combined_functions.append(combine_like_variables(temp_function))


print ("combined functions")
for f in _combined_functions:
    print(get_function_string(f))    
        
        
_work_functions = copy.deepcopy(_combined_functions)
for f in _parsed_functions:
    _work_functions.insert(0,set_function_to_zero(f))
print ("Functions to work on:")
for f in _work_functions:
    print(get_function_string(f))


_isolated_functions = create_isolated_functions(_work_functions)
print("isolated variable functions")
for f in _isolated_functions:
    print(get_function_string(f))
