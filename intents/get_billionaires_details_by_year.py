from fastapi.responses import JSONResponse
from database.db_connection import db_get_details_from_year

def get_billionaires_details_by_year(parameters : dict):
    name = parameters.get('person', {}).get('name', None)
    year = int(parameters.get('number'))
    if name and year:
        status = db_get_details_from_year(name, year)
        
        if status:
            extracted_rank, extracted_name, extracted_wealth = status
            fulfillment_text = f"In year {year}, {extracted_name} was at rank {extracted_rank} with wealth of {extracted_wealth} dollars"
        else:
            fulfillment_text = f"{name} is not in Top 10 Billionaires of {year}. Search other or type HELP"

    else:
        fulfillment_text = f"Please provide appropriate details. You can also type HELP"

    return JSONResponse(
                content={
                    "fulfillmentText": fulfillment_text
                    })