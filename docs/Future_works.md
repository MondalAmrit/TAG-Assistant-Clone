# Approaches
- [ ] Conversation
- [x] Individual Prompts

# How should the dataset look like?
- Size : More examples is better (Examples : 10K)
- Quality matters
- Previous Pythonic Approach to create dataset

# Aspect
- Greetings ( Hi, Hello, Thank You )
- - Hi --> 'Hello #name#' --> .replace( '#name#',user.name ) -->  Hello Anirudh
- Jokes
- Facts
- Events ( What is on Jaunary 26th?, Historical Events )
- Small Talk ( Do You like coffee? )
- Feedback improvement
- Error Handling ( Harmful Context, Out of Context )

# Command line like Things
 - Calculator ( .replace('x','*') --> eval())
 - @weather_current location = 'Delhi'

# Naming Conventions
User : {
name, dob, mobile number, email
}


# Examples structure.
**Note:** Slot filling is ignored for now.

It will be of five columns (Prefix, Target, Suffix, TAG_NAME, Slot Filling),
``` 
exmple = [prompt = <PREFIX> <TARGET> <SUFFIX> ], [TAG_NAME], [SLOT FILLING[]],
<PREFIX> = <PREFIX> <TARGET> <SUFFIX> | Constant
<TARGET> = Constant
<SUFFIX> = <PREFIX> <TARGET> <SUFFIX> | Constant
```

Prefix and suffix can either be nested of can also be empty string.
TAG_NAME helps to identify which example belongs to which specific action.
Target Must be written in format #TKN#. So that a replace function can be simply used in sythetic generation case.

Slot filling consists all the #tkn# replacements.
So Slot filling will be an array in the serial order
So in the execution time,
1. The tokenizer will tokenize the Slots as Begin, Include.
2. These will be replaced in the actual first string matching (as we are having #tkn# in serial order)
```
Example : 'Can you increase the volume to #tkn# please?', 'Volume', [70]

So, when interpreted, first the 70 will be breaked into tokens.
Based on the Begin and included tokens will be assigned.
Now, SLOT_FILLING = [ [toknes of a single #tkn#] ]
After tokenizing the prompt, we can simply replace 151 (#tkn#) with SLOT_FILLING[0] I.e. tokens to be occured in place of single #tkn#.
This will create a slot filling.

Now the actual input will be created by simply replaceing #tkn# with SLOT_FILLING in serial order.
```

# Current Works
- [ ] Converting Each example to classification example
- [ ] Use random shuffle at the end of dataset creation
- [ ] Implement BERT model training on this dataset