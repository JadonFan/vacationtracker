# Vacation Tracker

In the [Discord developer portal](https://discord.com/developers/applications),

1. Create a new application.
2. Copy the application ID.
3. Configure the privileged intents for the application.

Then, in this project,

1. Create a new file named .env in the same folder as this file.
2. Paste the following line into the .env file and replace <application_id> with the application ID.

    ```env
    BOT_KEY=<application_id>
    ```

3. Run the following commands on the command line:

    **Windows**

    ```powershell
    bot-env\Scripts\activate.bat
    python3 -m vacationtracker
    ```

    **Mac**

    ```bash
    source bot-env/bin/activate
    python3 -m vacationtracker
    ```
