# Write your code here.
#Task 1: Hello
def hello():
    return("Hello!")
print(hello())

#Task 2: Greet with a Formatted String
def greet(name):
    return (f"Hello, {name}!")

#Task 3: Calculator
def calc(a,b,operation="multiply"):
    try: 
        match operation:
            case "add":
                result = a + b
            case "subtract":
                result = a - b
            case "multiply":
                result = a * b
            case "divide":
                result = a / b
            case "int_divide":
                result = a // b
            case "modulo": 
                result = a % b
            case "power":
                result = a ** b
        return result
    except ZeroDivisionError:
        return("You can't divide by 0!")
    except TypeError:
        return("You can't multiply those values!")
    

print(calc(2,0, "divide"))

#Task 4: Data Type Conversion
def data_type_conversion(value, data_type_name):
    try:
        match data_type_name:
            case "int":
                result = int(value)
            case "float":
                result = float(value)
            case "str":
                result = str(value)
        return result
    
    except ValueError:
        return (f"You can't convert {value} into a {data_type_name}.")
   
print(data_type_conversion("test","int"))

#Task 5: Grading System, Using *args

def grade(*args):
    try:
        result = sum(args)/len(args)
        if result < 60:
            grade = "F"
        elif result < 69:
            grade = "D"
        elif result < 79:
            grade = "C"
        elif result < 89:
            grade = "B"
        else: 
            grade = "A"
        return grade

    except TypeError:
        return ("Invalid data was provided.")

print(grade(10, 60, 80, 58))

#Task 6: Use a For Loop with a Range

def repeat(string, count):
    new_str = ""
    for i in range(count):
        new_str += string
    return new_str

print(repeat("test",5))

#Task 7: Student Scores, Using **kwargs
def student_scores(position, **kwargs):
    match position:
        case "best":
            max_key = None
            max_value = 0
            for key, value in kwargs.items():
                if value > max_value:
                    max_value = value
                    max_key = key
            return max_key
        
        case "mean":
            average_score = sum(kwargs.values())/len(kwargs.values())
            return average_score

#Task 8: Titleize, with String and List Operations

def titleize(string):
    words = string.split(" ")
    little_words = {"a","on","an","the","of","and","is","in"}
    words[0] = words[0].capitalize()
    if len(words) > 1:
        for i in range (1,len(words)):
            if words[i] in little_words and (i!=len(words)-1):
                continue
            else:
                words[i]=words[i].capitalize()
    return ' '.join(words)

print(titleize("Test: the new Version of my code is good and."))

#Task 9: Hangman, with more String Operations

def hangman(secret, guess):
    new_word = ""
    
    for s in secret:
        if s in guess:
            new_word += s
        else:
            new_word += "_"
    return new_word
    

print(hangman("Test", "e"))

#Task 10: Pig Latin, Another String Manipulation Exercise

def pig_latin(english_string):
    eng_list = english_string.split(" ")
    vowel = {"a", "e", "i", "o", "u"}
    for i in range(len(eng_list)):
        if eng_list[i][0] in vowel:
            eng_list[i] = eng_list[i]+"ay"
        else:
            j=0
            consonant=""
            while eng_list[i][j] not in vowel:
                consonant+=eng_list[i][j]
                j+=1
            if consonant[-1] =="q" and eng_list[i][j]=="u":
                consonant+="u"
                j+=1
            eng_list[i] = eng_list[i][j:]+consonant+"ay"            

    return  " ".join(eng_list)

print(pig_latin("quiet apple and cherry"))