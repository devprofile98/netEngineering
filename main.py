from fastapi import FastAPI

app= FastAPI()

data = [
            {
            "image_url":"https://images.app.goo.gl/4EVHNVKwiqj6CRoi9",
            "name":"first_object",
            "id":1
            },
             {
            "image_url":"https://images.app.goo.gl/5a6dR6wQcMiQiDCt6",
            "name":"first_object",
            "id":2
            },
             {
            "image_url":"https://images.app.goo.gl/o2Xbf6KdpgR3h6Da8",
            "name":"first_object",
            "id":3
            }
            , {
            "image_url":"https://images.app.goo.gl/a14jNBJY9V4mxUEj6",
            "name":"first_object",
            "id":4
            }
            , {
            "image_url":"https://images.app.goo.gl/9GNkDRijWMtBvB8W6",
            "name":"first_object",
            "id":5
            }
        ]

@app.get("/items/")
async def get_items(): # get items list 
    return{
        "data":data
    }


@app.get("/item/{item_id}")
async def get_item(item_id:int): # get one item from data
    return {"data":data[item_id]}