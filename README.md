<h1 align="center"> NOVA </h1>

**Nextgen Offline Voice Assistant**

# About NOVA
An early Stage development of a new era of Assistants like JARVIS (or DUM-E).
It's like ```AI Agents + Chat Focused + Small Models = NOVA Model```

# Mission
To down stream the power of GEN AI to the low end devices with less space by creating a the infrastructure along with the supporting models and datasets

# Vision
To create a Infrastructure for the AI automation with Gen AI that can run on very poor devices like andorid 6 or so without much sarcifice.

# Other Superpowers that can be possible with this?
- MarketPlace for the intents
- AI based OS which will gain a full device control and remove the abstractions of device OS

# Why do we need NOVA
NOVA comes into play specially in the offline mode where the top assistants can't deliver their chatbot services. Also with it's small space requirement it will be a best fit for the IOT to acts an interface that can run independently.

But Actually you can do much more than that :)

# How it works?
User interacts with the AI using the chat. <br />
Based on the user prompts the Ai will decide the response along with the protocol to run.

# Technical Details
 - It contains 3 models
    - [x] BERT for Classification
    - [x] GPT for text generation
    - [x] BERT for Slot Filling
 - Classification model will classify which class to execute
 - If the class is `Basic Chat` then GPT model will work
 - Else `BERT Slot Filling` will extract the arguments from user prompt. Then passes it to action specified.

 # What do you mean by an Intent?
  - Intent Contains `examples` and `actions`
  - `actions` contains the functions (even another model) to be executed
  - `examples` contains the most likely prompts to call this aciton
  - In short, `Intent` contains the most relevent actions and examples at one place.

# Installation and Usage
For Installation setup refer [here](docs/installation.md) <br />
For Usage setup refer [here](docs/usage.md) <br />
**Note:** Installation is a one time setup and usage is to be done on every activation.

# How can I contribute?
Read the [contriubtion guidelines](docs/contribution_guide.md)

# How to create Intents/Datasets?
Refer to [creating intents](docs/CreatingIntents.md)

# How this repo works?
This repo works by:
1. Python (FASTAPI) for creating, storing and managing the datasets. This can become a future Service Type (Like the DialogFlow) thus enabling a new marketplace.
2. JavaScript for all other functions like Frontend, Models, Working,...
3. For Mobile we use `expo` with react native
4. For desktop we use `electron js`

# Current Version Features
- [x] Chat Interface
- [x] Internet Search
- [x] YouTube Search
- [x] Music Player
- [x] GIT Command Line Handler
- [x] Weather Forecasting

# Future Scope
- Introducing New Protocols
- Mobile Deployment
- Increasing the Sequence Length
- Enabling the Context
