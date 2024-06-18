import re


def generate_code(data: dict[str, str]) -> str:
    segment = data['itineraries'][0]['segments'][0]
    traveler_pricing = data['travelerPricings'][0]
    fare_details = traveler_pricing['fareDetailsBySegment'][0]
    flight_class = fare_details['cabin']
    air_company = segment['carrierCode']
    iata_from = segment['departure']['iataCode']
    air_company_code = segment['number']
    iata_to = segment['arrival']['iataCode']
    
    code = ''.join([flight_class[0:3], air_company, iata_from, air_company_code, iata_to])
    
    return code

def parse_duration(data: str) -> str:
    duration = data['itineraries'][0]['duration']
    pattern = re.compile(r'PT(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?')
    match = pattern.match(duration)

    hours = int(match.group(1) or 0)
    minutes = int(match.group(2) or 0)
    seconds = int(match.group(3) or 0)
    duration = f"{hours:02}:{minutes:02}:{seconds:02}"
    
    return duration

def generate_ticket_data(data: dict[str, str]) -> dict[str, str]:
    duration = parse_duration(data)
    code_str = generate_code(data)
    
    ticket = {
            'code': code_str,
            'duration': duration,
            'price': data['price']['total'],
        }
    return ticket