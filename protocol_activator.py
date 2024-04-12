from Datasets.WeatherForecast import executor as weatherProtocol
from Datasets.GITcommandHandler import executor as GITCommandProtocol
from Datasets.InternetSearch import executor as InternetSearchProtocol
from Datasets.YouTubeSearch import executor as YouTubeSearchProtocol
from Datasets.MusicPlayer import executor as MusicPlayerProtocol
from Datasets.WeatherForecast import executor as WeatherProtocol


import pprint, inspect
protocol_map = {
    104 : GITCommandProtocol,
    105 : InternetSearchProtocol,
    106 : YouTubeSearchProtocol,
    107 : MusicPlayerProtocol,
    108 : WeatherProtocol,
}

protocol_map_str = {
    'GITCommandProtocol' : 104,
    'InternetSearchProtocol' : 105,
    'YouTubeSearchProtocol' : 106,
    'MusicPlayerProtocol' : 107,
    'WeatherProtocol' : 108,
}

def protocol_activator(Protocol_code, function_code, args = {}):
    """
    attributes
    ----------
    protocol_code: int --> The Protocol to activate
    function_code: int --> The function to activate
    args: dict --> The arguments that are given
    """
    # Get the function to call
    try:
        # Get the function to call
        func = protocol_map[Protocol_code].functionMap[function_code]
    except KeyError:
        print(f"Error: Protocol code {Protocol_code} or function code {function_code} not found.")
        return None
    
    # Get the params required for the function.
    params = inspect.getfullargspec(func)
    params_args, params_defaults = params.args, params.defaults
    args_to_pass = []
    defaults_idx = 0

    for idx, arg in enumerate(params_args):
        if arg not in args:
            # If it is a default args. Then get it staright.
            if params_defaults and idx >= len(params_args) - len(params_defaults):
                args_to_pass.append(params_defaults[defaults_idx])
                defaults_idx += 1
            else: 
                # Either ask from user. Or get from the personal data DB
                args_to_pass.append(input(f"{arg}: "))
        else:
            args_to_pass.append(args[arg])
    
    # Perform the function call
    res = func(*args_to_pass)
    pprint.pprint(res)
    return res

# protocol_activator(108,1)