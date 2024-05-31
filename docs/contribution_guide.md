# Frontend
- The Pages should in `/pages` folder along with css file
- The Algorithm or a function must have it's explaination at the top in comments

# Backend
- The API should be in a proper format.
- `PyDantic Base Model` must be used to create a request template for an object.
- The relative path of backend will be from `./TAG-Assistant-Clone/backend/`

# Datasets
- The dataset will be a intent
- Each intent will have some actions and their activation examples <br/><br/>

- It Should contain four files
- - `__init__.py` for specifying the folder as a package
- - `dataset.csv` for directly adding the training and validation example
- - `examples.py` for any synthetic generation or to return the dataset examples for this intent
- - `actions.py` for functions that will be executed under this intent
<br/><br/>

- For any token specifying in the example. use something like `#tkn#` so that it will be easy to use  with `.replace('#tkn#','<NEW_TOKEN>')`
- `examples.py` must return two datasets (I.e. for training and validation)