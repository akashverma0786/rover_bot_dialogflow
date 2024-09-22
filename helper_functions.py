import re
def extract_session_id(session_str : str):
    match = re.search(r"/sessions/(.*?)/contexts/", session_str)
    if match:
        extracted_string = match.group(1)
        return extracted_string
    return ""


if __name__ == "__main__":
    res = extract_session_id("projects/rover-chatbot-lreo/agent/sessions/5ad2a701-9b95-78bf-5240-6c5c6efd67f2/contexts/details-")
    print(res)