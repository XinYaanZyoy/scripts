- ./config.py should look like...
    ```
    screen_name = ""
    #1. username of twitter account user

    max_followers_count = 
    #2. this is used by the Curser, which needs number of items to fetched, just set it (multiple of 20) to some max number you think you can't exceed, update it periodically if needed

    CONSUMER_API_KEY = ""
    CONSUMER_API_KEY_SECRET = ""
    ACCESS_TOKEN = ""
    ACCESS_TOKEN_SECRET = ""
    #3. these are all the keys that are needed, as is described in documentation
    ```

- all the data is strored in ./data

- ./functions.py include all the api implementation functions and also some run functions

- there are two run functions availible, sync and status, which can be run by corresponding bash scripts.

- the run bash script just runs both the run scripts in order.