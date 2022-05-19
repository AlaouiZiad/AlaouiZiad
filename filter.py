# input
# type the input method of array and mode here (for develepers)
# type 1 for high freqency filter and 0 for low freqency filter
# prosses
if mode:
    x=0
    out=[]
    for element in array:
        x+=element
        out.append(x)
else:
    subtrac=lambda x,y:x-y
    tracker=0
    stack=[]
    out=[]
    for element in array:
        if tracker<2:
            stack.append(element)
            tracker+=1
        else:
            out.append(subtrac(stack[1],stack[0]))
            stack.append(element)
            stack.remove(stack[0])
# output
# type the output method of out here (for develepers)



          