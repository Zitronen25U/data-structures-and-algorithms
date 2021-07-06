# Challenge Summary 

- Given a business trip itinerary, and an Alaska Airlines route map, is the trip possible with direct flights? If so, how much will the total trip cost be?

## WhiteBoard

- [CHECK IT](../graph_business_trip/challenge.jpg)

## Approach

- utilizing the fact that the graph returns a list of keys and values, iterate through that list and determine if a vertex is neighbors with another vertex. 

- Add the weight of that vertex to determine total "flight" costs

## Tests

- [CHECK IT](/tests/test_graph_trip.py)