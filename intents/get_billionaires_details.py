from fastapi.responses import JSONResponse
from database.db_connection import db_get_details_billionaire

def get_billionaires_details(parameters : dict, session_id : str, top_billionaires_cache : dict):
    if session_id in top_billionaires_cache:
        result_dict = top_billionaires_cache[session_id]["data"]
        year_from_dict = top_billionaires_cache[session_id]["year"]

        name = ''

        # Check if 'person' exists and is a dictionary, then check for 'name'
        if 'person' in parameters and isinstance(parameters['person'], dict):
            name = parameters['person'].get('name', '').strip()
        number = parameters['number']
        
        if name:
            found = False
            for key, value in result_dict.items():
                if name.lower() == value.lower() or  name in value:
                    status = db_get_details_billionaire(key, year_from_dict)

                    b_rank, b_name, b_net_worth, b_age, b_nationality, b_primary_source = status

                    fulfillment_text = f"""The rank {b_rank} billionaire in {int(year_from_dict)} is {b_name} whose Net Worth is
                                        {b_net_worth} Dollars. {b_name}'s age and nationality are {b_age} &
                                        {b_nationality} respectively. The primary source of income of {b_name}
                                        is {b_primary_source}. Do you want to know about other billionaire from the list you got?"""
                    found = True
                    break
            if not found:
                fulfillment_text = f"No Billionaire with name {name} found. Please request the top billionaires first. Or Type HELP for commands"
        elif (number and number <= len(result_dict) and number > 0):
            status = db_get_details_billionaire(number, year_from_dict)
            
            fulfillment_text = f"status got from database : {status}"
        else:
            fulfillment_text = f"No Data found. Please request the top {int(number)} billionaires first."

    
        return JSONResponse(
            content={
                "fulfillmentText": fulfillment_text
                })
