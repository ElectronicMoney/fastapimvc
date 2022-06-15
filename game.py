"""
    Product Description
    You can Invest Money Below Given and Earn Double money by pREDicting colours. 
    If you are looking for easy and quick way to earn money online in India where 
    you can earn huge money in less time. Then color pREDiction game is perfect for 
    you. there are 3 colours in the game RED, GREEN, Violet. You can PREDict Every 
    3 Minutes by using investing money and earn double money.

    The market opens all day. The total number of trade is 480

    1. JOIN GREEN: if the result shows 1,3,7,9, you will get (98*2) 196 
    If the result shows 5, you will get (98*1.5) 147

    2. JOIN RED: if the result shows 2,4,6,8, you will get (98*2) 196.
    If the result shows 0, you will get (98*1.5) 147

    3. JOIN VIOLET: if the result shows 0 or 5, you will get (98*4.5) 441

    4. SELECT NUMBER: if the result is the same as the number you selected, 
    you will get(98*9)882

    5. JOIN SMALL: if the result shows 0,1,2,3,4 you will get (98*1.5)

    6. JOIN BIG: if the result shows 5,6,7,8,9 you will get (98*1.5)

"""


def process_trades(trades):
    winning_numbers = [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00]
    winner_details = {
        "winning_number": None,
        "winning_size": "",
        "winning_color": "",
        "winners": [],
        "losers": []
    }

    for trade in trades:
        if trade["is_color"]:
            # Checkif the color is RED
            # modify the amount at 0, 2,4,6,8
            if trade["color"] == "RED":
                winning_numbers[0] += (trade["trade_amount"] * 1.5)
                winning_numbers[2] += (trade["trade_amount"] * 2.0)
                winning_numbers[4] += (trade["trade_amount"] * 2.0)
                winning_numbers[6] += (trade["trade_amount"] * 2.0)
                winning_numbers[8] += (trade["trade_amount"] * 2.0)
            elif trade["color"] == "GREEN":
                winning_numbers[1] += (trade["trade_amount"] * 2.0)
                winning_numbers[3] += (trade["trade_amount"] * 2.0)
                winning_numbers[5] += (trade["trade_amount"] * 1.5)
                winning_numbers[7] += (trade["trade_amount"] * 2.0)
                winning_numbers[9] += (trade["trade_amount"] * 2.0)
            else:
                winning_numbers[0] += (trade["trade_amount"] * 4.5)
                winning_numbers[5] += (trade["trade_amount"] * 4.5)
    
        elif trade["is_number"]:
            if trade["number"] == 0:
                winning_numbers[0] += (trade["trade_amount"] * 9.0)
            if trade["number"] == 1:
                winning_numbers[1] += (trade["trade_amount"] * 9.0)
            if trade["number"] == 2:
                winning_numbers[2] += (trade["trade_amount"] * 9.0)
            if trade["number"] == 3:
                winning_numbers[3] += (trade["trade_amount"] * 9.0)
            if trade["number"] == 4:
                winning_numbers[4] += (trade["trade_amount"] * 9.0)
            if trade["number"] == 5:
                winning_numbers[5] += (trade["trade_amount"] * 9.0)
            if trade["number"] == 6:
                winning_numbers[6] += (trade["trade_amount"] * 9.0)
            if trade["number"] == 7:
                winning_numbers[7] += (trade["trade_amount"] * 9.0)
            if trade["number"] == 8:
                winning_numbers[8] += (trade["trade_amount"] * 9.0)
            if trade["number"] == 9:
                winning_numbers[9] += (trade["trade_amount"] * 9.0)
        else:
            if trade["size"] == "SMALL":
                winning_numbers[0] += (trade["trade_amount"] * 1.5)
                winning_numbers[1] += (trade["trade_amount"] * 1.5)
                winning_numbers[2] += (trade["trade_amount"] * 1.5)
                winning_numbers[3] += (trade["trade_amount"] * 1.5)
                winning_numbers[4] += (trade["trade_amount"] * 1.5)
            else:
                winning_numbers[5] += (trade["trade_amount"] * 1.5)
                winning_numbers[6] += (trade["trade_amount"] * 1.5)
                winning_numbers[7] += (trade["trade_amount"] * 1.5)
                winning_numbers[8] += (trade["trade_amount"] * 1.5)
                winning_numbers[9] += (trade["trade_amount"] * 1.5)



    min_number = winning_numbers[0]

    # Loop though the winning_numbers
    for i in range(len(winning_numbers)):
        if winning_numbers[i] < min_number:
            min_number = winning_numbers[i]
            
    winner_details["winning_number"] = winning_numbers.index(min_number)

    # Add the size based on the winning number
    if winner_details["winning_number"] < 5:
        winner_details["winning_size"] = "SMALL"
    else:
        winner_details["winning_size"] = "BIG"


    # Extrct the winners user_id from the trades
    for trade in trades:
        if trade["is_color"]:
            if trade["color"] == "RED":
                # Check if winner_details["winning_number"] is in [2, 4, 6, 8]
                if winner_details["winning_number"] in [0, 2, 4, 6, 8]:
                    winner_details["winners"].append(trade["user_id"])
                    winner_details["winning_color"] = trade["color"]

                else:
                    winner_details["losers"].append(trade["user_id"])

            elif trade["color"] == "GREEN":
                if winner_details["winning_number"] in [1, 3, 5, 7, 9]:
                    winner_details["winners"].append(trade["user_id"])
                    winner_details["winning_color"] = trade["color"]
                else:
                    winner_details["losers"].append(trade["user_id"])
            elif trade["size"] == "SMALL":
                if winner_details["winning_number"] in [0, 1, 2, 3, 4]:
                    winner_details["winners"].append(trade["user_id"])
                else:
                    winner_details["losers"].append(trade["user_id"])
            elif trade["size"] == "BIG":
                if winner_details["winning_number"] in [5, 6, 7, 8, 9]:
                    winner_details["winners"].append(trade["user_id"])
                else:
                    winner_details["losers"].append(trade["user_id"])

            else:
                if winner_details["winning_number"] in [0, 5]:
                    winner_details["winners"].append(trade["user_id"])
                    if winner_details["winning_number"] == 0:
                        winner_details["winning_color"] = "VOILET, RED"
                    else:
                        winner_details["winning_color"] = "VOILET, GREEN"
                     
                else:
                    winner_details["losers"].append(trade["user_id"])
        else:
            if trade["number"]  == winner_details["winning_number"]:
                winner_details["winners"].append(trade["user_id"])
            else:
                winner_details["losers"].append(trade["user_id"])


    return winner_details


if __name__ == "__main__":    
    from app.settings.Settings import setting
    print(setting["APP_NAME"])
    trades = [
        {
            "trade_id": 1,
            "user_id": 1,
            "trade_amount": 100,
            "is_color": True,
            "size": None,
            "number": None,
            "is_number": False,
            "color": "RED",
            "status": "pending",
        },

        {
        "trade_id": 1,
        "user_id": 2,
        "trade_amount": 150,
        "is_color": True,
        "number": None,
        "size": None,
        "is_number": False,
        "color": "GREEN",
        "status": "pending",
    },

    {
        "trade_id": 1,
        "user_id": 3,
        "trade_amount": 200,
        "number": None,
        "size": None,
        "color": "RED",
        "is_number": False,
        "status": "pending",
        "is_color": True,
    },
    
     {
        "trade_id": 1,
        "user_id": 4,
        "trade_amount": 150,
        "is_color": True,
        "number": None,
        "is_number": False,
        "size": None,
        "color": "GREEN",
        "status": "pending",
    },

    {
        "trade_id": 1,
        "user_id": 5,
        "trade_amount": 100,
        "number": None,
        "is_number": False,
        "size": None,
        "color": "VOILET",
        "is_color": True,
        "status": "pending",
    },

    {
        "trade_id": 1,
        "user_id": 6,
        "trade_amount": 100,
        "number": 2,
        "is_number": True,
        "color": None,
        "size": None,
        "is_color": False,
        "status": "pending",
    },
    {
        "trade_id": 1,
        "user_id": 7,
        "trade_amount": 100,
        "number": 9,
        "is_number": False,
        "color": None,
        "size": None,
        "is_color": False,
        "status": "pending",
    },
    {
        "trade_id": 1,
        "user_id": 8,
        "trade_amount": 100,
        "number": 4,
        "color": None,
        "size": None,
        "is_color": False,
        "is_number": True,
        "status": "pending",
    },

    {
        "trade_id": 1,
        "user_id": 9,
        "trade_amount": 200,
        "number": 1,
        "is_number": True,
        "color": None,
        "size": None,
        "is_color": False,
        "status": "pending",
    },


    {
        "trade_id": 1,
        "user_id": 10,
        "trade_amount": 200,
        "number": None,
        "is_number": False,
        "color": None,
        "size": "BIG",
        "is_color": False,
        "status": "pending",
    }



]

    p_t = process_trades(trades=trades)
    print(p_t)