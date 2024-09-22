from fastapi.responses import JSONResponse
from database.db_connection import db_get_billionaire_by_rank

def get_billionaire_by_rank(parameters : dict, session_id : str, top_billionaires_cache : dict):
    year, rank = parameters["number"], parameters["ordinal"]
    if not year:
        year = 2024
    elif int(year) < 1997 or int(year) > 2024:
        return JSONResponse(content={
            "fulfillmentText": "Please provide year ranging from 1997 - 2024, Thank you"
        })

    if not rank:
        rank = 1
    elif int(rank) < 1 or int(rank) > 10:
        return JSONResponse(content={
            "fulfillmentText": "Please provide rank ranging from 1 - 10, Thank you"
        })

    status = db_get_billionaire_by_rank(year, rank)
    result_dict = {rank: status[0]}
    
    top_billionaires_cache[session_id] = {
        "data": result_dict,
        "year": year
    }



    fulfillment_text = f"The number {int(rank)} richest person in {int(year)} is {status[0]} with wealth of {status[1]} dollars."
    return JSONResponse(content={
            "fulfillmentText": fulfillment_text
        })