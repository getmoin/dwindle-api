# FILE: main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configure CORS
origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/client")
async def get_client():
    return {
        "id": 1,
        "name": "Central Ottawa Service",
        "logo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTe5Yl8Y17JjFZnFEySotX7S97ZMgKzkbqEOg&s?w=128&h=128&fit=crop",
        "description": "Leading provider of automotive services with over 20 years of experience. Trust our certified mechanics for all your vehicle maintenance and repair needs.",
        "heroImage": "https://plus.unsplash.com/premium_photo-1674375344746-2f27c4720440?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D?w=1600",
        "address": {
        "street": "123 Auto Service Lane",
        "city": "Ottawa",
        "state": "ON",
        "zip": "K1P 1J1"
        },
        "availableDates": [
            "2024-11-26",
            "2024-11-27",
            "2024-11-28",
            "2024-12-01",
            "2024-12-02",
        ],
        "availableTimeSlots": [
            "09:00 AM",
            "10:00 AM",
            "11:00 AM",
            "02:00 PM",
            "03:00 PM",
            "04:00 PM",
        ],
        "reviews": [
            {
                "id": "1",
                "author": "John Smith",
                "rating": 5,
                "comment": "Excellent service! They fixed my car quickly and the price was very reasonable.",
                "date": "2024-02-15",
                "avatar": "https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?w=64&h=64&fit=crop"
            },
            {
                "id": 2,
                "author": "Sarah Johnson",
                "rating": 5,
                "comment": "Very professional team. They explained everything clearly and did a great job.",
                "date": "2024-02-10",
                "avatar": "https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=64&h=64&fit=crop"
            },
            {
                "id": 3,
                "author": "Mike Wilson",
                "rating": 4,
                "comment": "Reliable service and friendly staff. Would recommend to others.",
                "date": "2024-02-05",
                "avatar": "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=64&h=64&fit=crop"
            }
        ] 
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)