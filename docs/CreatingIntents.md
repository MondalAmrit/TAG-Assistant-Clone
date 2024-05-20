<h1 align='center'> Creation of Intents </h1>

## What is an intent?
Intent is like a wrapper for all the intentions and their corresponding actions related to that intent.

## Why do we need it?
Intents are needed to maintain a structured way of storing the required intentions and their actions

## What does it contains?
Intents can be further divided into four files.

- `__init__.py` to make the intent a module
- `examples.py` contains the examples of an Intent
- `actions.py` contains the actions of an Intent
- `dataset.csv` to store the examples exculsively

## How to create examples?
Examples from `examples.py` are a synthetic generation where the python lists are used to do this.<br/><br/>
The `examples.py` mainly contains of five things:
- `Importing the Slots Labels`
- A variable containing the `<INTENT_NAME>`
- A Python list containing the `<CUSTOM_EXAMPLE_NAMES>` aka `ActionsMap`. Remember that these names are used to map the examples back with the actions. So kindly use the same naming conventions in the `action.py` also.
- `generate_dataset()` to get the final dataset.
- `generate_synthetic_dataset()` to get the synthetic dataset.
<br/>
Other than these you can also create your custom functions but ultimately they should align with the final example format.

## Example Format
This is a structured way of getting the example as a useful and meaningful data sample.<br/>
It will contain three sections (in python lists)
```
List[0] : The Synthetic prompt with Slots (Not filled)
List[1] : <INTENT_NAME> <CUSTOM_EXAMPLE_NAMES>
List[2] : A dictionary of the Slots with {SlotName:SlotValue}
``` 
<br/>
Slots are needed for making this dataset useful for the task of slot filling.
<br/><br/>
An example can be:

```Python
["What is the weather at {Location} on {Date}","Weather CurrentForecast",{"Location":"Delhi","Date":"28-05-2023"}]
```
**Note:** A doubt here. Will it be better to use Lists + Serial order or Dictionary to carry this slot data

## How to create Actions?
Actions from `actions.py` can be easily created by placing your intended function there and use that
`ActionsMap` as a dictionary to call the corresponding Action.<br/>
You can define the action to be executed upon the prompt call. Also a Response can be reutrned like in case of a Weather forecasting you can return the weather status.<br/>


## How will this example create a data sample?
The Example Format specified above is just like a preperator. This is then passed to the Acutal dataset formatter where it will get converted into the actual dataset. Like,
```Python
["[CLS] What is the weather at Delhi on 28-05-2023 [SEP]","Weather CurrentForecast","O O O O O O B-LOC O B-DATE I-DATE I-DATE O"]
```
**NOTE:** [CLS] and [SEP] is also considered while preparing the slot filling data


## Current Available Slots

```Python
{
    "Location" : ["B-LOC","I-LOC"],
    "Quantity" : ["B-QTY","I-QTY"],
    "Query" : ["B-QUERY","I-QUERY"],
    "Date" : ["B-DATE","I-DATE"],
    "Time" : ["B-TIME","I-TIME"],
}
```