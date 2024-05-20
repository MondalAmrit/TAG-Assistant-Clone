# TAG-Assistant-Clone-
An early Stage development of a new era of Assistants like JARVIS.

It's like ```AI Agents + Chat Focused + Small Models = TAG Model```

# Mission
To power the Applications using AI with the help of Automation Protocols with small language models

# Vission
Making the task automation easier than ever with the help of AI chat interface and less memory footprint

# About TAG
TAG - Task Automation via GPT

But Actually you can do much more than that :)

# How it works?
User interacts with the AI using the chat. <br />
Based on the user prompts the Ai will decide the response along with the protocol to run.

# Technical Details
 - It contains 3 models
    - [x] BERT for Classification
    - [x] GPT for text generation
    - [ ] BERT for Slot Filling
 - Classification model will classify which class to execute
 - If the class is `Basic Chat` then GPT model will work
 - Else `BERT Slot Filling` will extract the arguments from user prompt. Then passes it to action specified.

 # What do you mean by an Intent?
  - Intent Contains `examples` and `actions`
  - `actions` contains the functions (even another model) to be executed
  - `examples` contains the most likely prompts to call this aciton
  - In short, `Intent` contains the most relevent actions and examples at one place.

# Current Problems
 - [x] Why Models are having so poor performance ?
 - [x] Slot Filling model implementation
 - [ ] Dataset Quality
 - [ ] Poor Frontend

# Installation and Usage
For Installation setup refer [here](docs/installation.md) <br />
For Usage setup refer [here](docs/usage.md) <br />
**Note:** Installation is a one time setup and usage is to be done on every activation.

# How can I contribute?
Read the [contriubtion guidelines](docs/contribution_guide.md)

# How to create Intents/Datasets?
Refer to [creating intents](docs/CreatingIntents.md)

# Current Version Features
- [x] Chat Interface
- [ ] Internet Search
- [ ] YouTube Search
- [ ] Music Player
- [ ] GIT Command Line Handler
- [ ] Weather Forecasting

# Future Scope
- Introducing New Protocols
- Changing the Model Architecture
- Increasing the Sequence Length
- Enabling the Context
