from fastapi import FastAPI

app = FastAPI()

@app.get("/factorial/{starting_number}")
def factorial(starting_number: int):
    if starting_number == 0:
        return {"result": False}

#app.get para po sa mismong function sa url
#if starting number is equal sa user input
#if si starting number ay == 0 mag fofalse ang output

    result = 1
    number = starting_number

#ang value ng starting_number ay malilipat sa number dahil sa declaration

    while number > 1:
        result *= number
        number -= 1

#yung statement na while number > 1: means na if si number ay greater than 1 magluloop ang code

    return {"Numerong inilagay": starting_number, "Ang iyong sagot ay": result}