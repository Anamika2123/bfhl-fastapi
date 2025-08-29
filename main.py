# from fastapi import FastAPI
# from pydantic import BaseModel
# from typing import List

# app = FastAPI()

# class RequestModel(BaseModel):
#     data: List[str]

# @app.post("/bfhl")
# def get_bfhl():
#     return {"operation_code": 1}

# def bfhl_handler(request: RequestModel):
#     data = request.data

#     odd_numbers = []
#     even_numbers = []
#     alphabets = []
#     special_characters = []
#     total_sum = 0
#     concat_string = ""

#     for item in data:
#         if item.isdigit():
#             num = int(item)
#             total_sum += num
#             if num % 2 == 0:
#                 even_numbers.append(item)
#             else:
#                 odd_numbers.append(item)
#         elif item.isalpha():
#             alphabets.append(item.upper())
#             concat_string += item
#         else:
#             special_characters.append(item)

#     return {
#         "is_success": True,
#         "user_id": "anamika_unnikrishnan_17091999",
#         "email": "your@vitstudent.ac.in",
#         "roll_number": "22BCE0000",
#         "odd_numbers": odd_numbers,
#         "even_numbers": even_numbers,
#         "alphabets": alphabets,
#         "special_characters": special_characters,
#         "sum": str(total_sum),
#         "concat_string": concat_string[::-1]  # reverse
#     }


from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class RequestModel(BaseModel):
    data: List[str]

@app.get("/bfhl")
def get_bfhl():
    return {"operation_code": 1}

@app.post("/bfhl")
def bfhl_handler(request: RequestModel):
    data = request.data

    odd_numbers = []
    even_numbers = []
    alphabets = []
    special_characters = []
    total_sum = 0
    concat_string = ""

    for item in data:
        if item.isdigit():
            num = int(item)
            total_sum += num
            if num % 2 == 0:
                even_numbers.append(item)
            else:
                odd_numbers.append(item)
        elif item.isalpha():
            alphabets.append(item.upper())
            concat_string += item
        else:
            special_characters.append(item)

    return {
        "is_success": True,
        "user_id": "anamika_unnikrishnan_17091999",
        "email": "your@vitstudent.ac.in",
        "roll_number": "22BCE0000",
        "odd_numbers": odd_numbers,
        "even_numbers": even_numbers,
        "alphabets": alphabets,
        "special_characters": special_characters,
        "sum": str(total_sum),
        "concat_string": concat_string[::-1]  # reverse string
    }
