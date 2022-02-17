# NLP_Week-20_HW


Map Reduce is techinque which is used to handle huge amounts of data. It is used to write the python programs, that can read the data from the standard input(stdin)

### Steps used to create and run map_reduce
> In Visual studio we need to create a folder map_reduce, inside which will create a mapper.py file where we use the file and split into words.
> 
> we use shebang line #!/usr/bin/env python which connects to the Bash command to execute the programm. This will make sure the bash will be used to interpret the script, even if it is executed under different shell.
> 
### mapper.py file:
>use the standard input to read the file, and iterating the input inside the loop to remove leading and trailing whitespaces and split the lines into words. Next, using regex will separate punctuations from the words and lower all the words.

>To execute and see the output we will run the command for cat_text file(cat ../cats_txt.txt|./mapper.py|sort) in git bash.



> We can see the above image. it separates words from the sentences and printed them separately.

### reducer.py file:
> We use the pipe(|) to join the mapper and reducer files and hthis gives us the combined output by sorting them.
> 



When we are dealing with huge amounts of data which may include punctuations, text, and some other mixed type of data, then it is important to strip the words from punctuations.
Also we do all the words to lower which makes us easy to count the words.
