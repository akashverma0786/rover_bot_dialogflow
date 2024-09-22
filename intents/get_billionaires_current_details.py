from fastapi.responses import JSONResponse
from database.db_connection import db_get_details_from_name

def get_billionaires_current_details(parameters : dict):
    name = parameters.get('person', {}).get('name', None)
    if name:
        status = db_get_details_from_name(name)
        if status:
            extracted_rank, extracted_name, extracted_wealth = status
            fulfillment_text = f"{extracted_name}'s rank is {extracted_rank} in Top 10 Billionaires of 2024 with a wealth of {extracted_wealth} Dollars"
        else:
            fulfillment_text = f"{name} is not in Top 10 Billionaires of 2024"

    else:
        fulfillment_text = f"No record of {name} found. You can also type help for commands."

    return JSONResponse(
                content={
                    "fulfillmentText": fulfillment_text
                    })
