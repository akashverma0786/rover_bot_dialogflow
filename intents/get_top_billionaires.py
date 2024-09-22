from fastapi.responses import JSONResponse
from database.db_connection import db_get_top_billionaires

def get_top_billionaires(parameters: dict, session_id : str, top_billionaires_cache : dict):
    number = parameters["number"]
    if len(number) == 2:
        num, year = number[0], str(int(number[1]))
    else:
        num = number[0]
        year = "2024"
    status = db_get_top_billionaires(num, year)
    result_dict = {rank: name for rank, name, wealth in status}
    
    top_billionaires_cache[session_id] = {
        "data": result_dict,
        "year": year
    }

    if status:
        # fullfillment_text = f" this is it : {status}"
        richest_people = "\n,".join([f"{no}. {name} with {wealth} Dollars \n" for no, name, wealth in status])
        if int(number[0]) > 10:
            fulfillment_text = f"I cannot provide information more than top TEN, So here are The Top 10 richest people : {richest_people}."
        else:
            fulfillment_text = f"The {int(number[0])} richest people in {int(year)} are: {richest_people}."
    else:
        fulfillment_text = f"Nothing found. TYPE HELP to get examples of the commands I can do"
    return JSONResponse(content={
            "fulfillmentText": fulfillment_text
        })