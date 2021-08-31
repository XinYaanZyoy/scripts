- ./config.py should look like...
    ```
    screen_name = ""
    #1. username of twitter account user

    count_per_page = 200
    #2. this is twitter API var, the number of users per page (in one req 1 page, and total 15 req/15 min), default is 20 and max is 200

    max_followers_count = 400
    #3. this is used by the Curser, which needs number of items to fetched, just set it (multiple of 20) to some max number you think you can't exceed (number of followers), update it periodically if needed

    CONSUMER_API_KEY = ""
    CONSUMER_API_KEY_SECRET = ""
    ACCESS_TOKEN = ""
    ACCESS_TOKEN_SECRET = ""
    #4. these are all the keys that are needed, as is described in documentation
    ```

- all the data is strored in ./data

- ./functions.py include all the api implementation functions and also some run functions

- there are two run functions availible, ./sync.sh and ./status.sh, the former accumulates the data and the latter analyzes it. both should be run in that order.

- ./api_stst.sh is run to check the API limit status

- the ./clean.sh cleans old data from ./data (except last and latest files and correspnding source directories)