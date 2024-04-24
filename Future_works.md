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
