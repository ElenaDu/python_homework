#Task 1: Diary
import traceback

try:
    with open('diary.txt', 'a') as file:
        c = 1
        while True:
            if c == 1:
                note = input("What happened today? ")
                c+=1
            else:
                note = input("What else? ")

            file.write(f'{note} \n')
            if note.lower() == "done for now":
                break
            
except Exception as e:
   trace_back = traceback.extract_tb(e.__traceback__)
   stack_trace = list()
   for trace in trace_back:
      stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
   print(f"Exception type: {type(e).__name__}")
   message = str(e)
   if message:
      print(f"Exception message: {message}")
   print(f"Stack trace: {stack_trace}")