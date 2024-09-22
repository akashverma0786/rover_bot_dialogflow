# Please Follow the Steps Carefully

# 1. Clone Repository

To clone the repository, use the following command:

```bash
git clone https://github.com/akashverma0786/rover_bot_dialogflow.git
```
# 2. Install Requirements

To install the necessary dependencies, navigate to the project directory and run the following command:

```bash
pip install -r requirements.txt
```

# 3: Connect to MySQL

Navigate to `rover_bot_dialogflow/database/db_cred.py` and set your database credentials to set up the MySQL server.

# 4: Scrape Data from Wikipedia

Navigate to `rover_bot_dialogflow/datascraping.py` and run the file manually to scrape all the data from Wikipedia and store it in the database for further interaction with the dialog bot.

# 5: Run FastAPI Server

Now that your MySQL credentials are provided, you can run the FastAPI server. Use the following command in the project directory's terminal:

```bash
uvicorn main:app --reload
```

# 6: Import Dialogflow Bot

The `Rover-Chatbot.zip` file is provided inside the project. This Chatbot has every intent, entity I created(Dialogflow ES Version). To import the chatbot into Google Dialogflow ES, follow these steps:

1. Go to the [Dialogflow Console](https://dialogflow.cloud.google.com/).
2. Create a new agent or select an existing one.
3. In the left-hand menu, click the Settings (⚙️) icon next to the agent’s name.
4. Go to the Export and Import section and click **Import from ZIP**.
5. Upload the `Rover-Chatbot.zip` file from the repository.
6. Click **Restore** to complete the import.

# 7: Integrate Webhook Using ngrok

To integrate the FastAPI backend with your Dialogflow bot, we need to use HTTPS for the webhook. Since FastAPI runs on HTTP, we will use ngrok to create a secure tunnel. Following are steps are to intsall ngrok using brew you can also download zip file to install nngrok by follwing steps given on [ngrok](https://dashboard.ngrok.com/get-started/setup/)

### Installing ngrok
IN NEW TERMINAL
You can install ngrok using Homebrew with the following command:

```bash
brew install ngrok/ngrok/ngrok
```

Create a free account on ngrok and get the auth token.

Run the following command to add your authtoken to the default ngrok.yml configuration file.

```bash
ngrok config add-authtoken <auth_token you got after signing in>
```

Put your fastAPI app online at an ephemeral domain forwarding to your upstream service. For example, if it is listening on port http://localhost:8000, run:

```bash
ngrok http http://localhost:8000
```
OR

```bash
ngrok http 8000
```
You will get a Forwarding which will look like this `https://bf8e-122-162-151-113.ngrok-free.app`

# 8: Using the HTTPS URL in Dialogflow

To use the chatbot with the integrated webhook, follow these steps:

1. Go to the Dialogflow Console and select imported agent.
2. Navigate to the **Fulfillment** section in the left-hand menu.
3. Enable the **Webhook** option.
4. In the **URL** field, paste the HTTPS URL provided by ngrok.
5. Click **Save** to apply the changes.

# 9: Use the Chatbot

To integrate the chatbot with your frontend, follow these steps:

1. Go to the **Integrations** section in Dialogflow and find the **Web Demo**.
2. Copy only the link inside the `src=""` line. **This step is important: only copy the link inside `src=""`.**
3. In your Code, navigate to the `frontend` folder and open `index.html`.
4. Inside the `<body>` tag, find the `<iframe>` tag. Inside this tag, set the `src` attribute to the URL you copied. It should look like this:

   ```html
             <iframe 
                width="550" 
                height="630" 
                allow="microphone;" 
                src="YOUR_COPIED_URL">
            </iframe>
   ```
5. Save the index.html file.
6. Go to your PC where your project folder is located, navigate to the frontend folder, and run the index.html file.

# 10. Watch the rover bot running :-
[Video of functioning Rover](https://drive.google.com/file/d/1zbdUONPrHdaWS87wjawfyBcm1NrwwM5Z/view?usp=sharing)