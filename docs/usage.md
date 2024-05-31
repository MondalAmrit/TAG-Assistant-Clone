**Note:** Kindly follow the [installation](installation.md) guide if not installed.

# To run python environment (Backend)
1. Naviagte to the root folder I.e. `TAG-Assistant-Clone`
2. Activate the virtual environment by `VirtualEnv\Scripts\activate` <br />
Later on you can even deactivate it by `VirtualEnv\Scripts\deactivate` if you are done.
3. Start the backend server by `uvicorn main:app --reload`

# To run the React-Vite environment (Frontend)
1. Naviaget to the frontend folder I.e. `TAG-Assistant-Clone/frontend`
2. Start the frontend server by `npm start`

**Note:**<br />
These will start the following servers in ports as:- <br/>
1. Frontend :- `http://127.0.0.1:3000`
2. Backend :- `http://127.0.0.1:8000`
<br/> So kindly make sure that these ports are available