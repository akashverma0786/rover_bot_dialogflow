import subprocess
import sys
from fastapi import FastAPI
from fastapi import Request
import helper_functions
from intents.get_top_billionaires import get_top_billionaires
from intents.get_billionaire_by_rank import get_billionaire_by_rank
from intents.get_billionaires_details import get_billionaires_details
from intents.get_billionaires_current_details import get_billionaires_current_details
from intents.get_billionaires_details_by_year import get_billionaires_details_by_year


app = FastAPI()
top_billionaires_cache = {}

@app.post("/")
async def handle_top_billionaires(request: Request):
    payload = await request.json()

    intent = payload['queryResult']['intent']['displayName']
    parameters = payload['queryResult']['parameters']
    outputContexts = payload['queryResult']['outputContexts']
    session_id = helper_functions.extract_session_id(outputContexts[0]['name'])

    if intent == "get.top.billionaires":
        return get_top_billionaires(parameters, session_id, top_billionaires_cache)
    if intent == "get.billionaires.by.rank":
        return get_billionaire_by_rank(parameters, session_id, top_billionaires_cache)
    if intent == "get.billionaires.details":
        return get_billionaires_details(parameters, session_id, top_billionaires_cache)
    if intent == "get.billionaires.current.details":
        return get_billionaires_current_details(parameters)
    if intent == "get.billionaires.details.by.year":
        return get_billionaires_details_by_year(parameters)