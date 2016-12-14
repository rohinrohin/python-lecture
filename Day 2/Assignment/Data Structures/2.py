event_info = [
        {
            "name": "Rohin",
            "detail": "Hello",
            "date": {
                "dd":"02",
                "mm":"10",
                "yy":"2016"
            },
            "people": ["person1", "person2"]
        },

        {
            "name": "Ravi",
            "detail": "Hello2",
            "date": {
                "dd": "04",
                "mm": "11",
                "yy": "2015"
            },
            "people": ["person1", "person2"]

        }
]

event_info.sort(key=lambda x: x["date"]["yy"]) #chronological order of date

print(event_info)

