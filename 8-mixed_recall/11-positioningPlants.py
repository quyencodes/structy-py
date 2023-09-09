def positioning_plants(costs):
  return _positioning_plants(costs, 0, None, {})

def _positioning_plants(costs, pos, last_plant, memo):
  key = (pos, last_plant)
  if key in memo:
    return memo[key]

  if pos == len(costs):
    return 0

  min_cost = float('inf')
  for plant_type, plant_cost in enumerate(costs[pos]):
    if plant_type != last_plant:
      candidate = plant_cost + positioning_plants(costs, pos+1, plant_type)
      min_cost = min(min_cost, candidate)
  memo[key] = min_cost
  return min_cost