# Weather Dataset Problem
- Weather Forecast must be time calculated (not predefined like Future,Past,...).<br/>
It should be calculated as if (Date.now() < prompt_time) then past...

# Notes Dataset Problem
- Open the notes can be considered as new feature
- Update File add Description to item can be considered in future updates

# News Dataset Problem
- It would be better to consider the news preferances
- Also providing the summary can be a good option
- Getting trusted sources for news can also be a value addition

# Mobile App
## Tokenizer (Coded by self)
## Model (Took the Onnx model and optimized it to .ort)
## Seq len (The current model is having problem with variable seq_len.)
To tackle this seq len problem, for now a post padding is being used and 
```
if (arr.length < seq_len) arr.concat([0]*(seq_len - arr.length))
```