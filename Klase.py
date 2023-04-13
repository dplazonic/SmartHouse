class Weather:
    def __init__(self, temperature, wind, location, description, is_day) -> None:
        self.temperature = temperature
        self.wind = wind
        self.location = location
        self.description = description
        self.is_day = is_day

    
    def __str__(self) -> str:
        return f"Temp: {self.temperature}\nWind: {self.wind}\nCity: {self.location}\n{self.description}"