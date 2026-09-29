class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        pair = sorted(zip(position, speed), key=lambda x: x[0], reverse=True)
        
        fleets = 0
        lead_time = 0
        
        for p, s in pair:
            time = (target - p) / s
            # Only increments when a car is strictly slower than the fleet ahead
            if time > lead_time:
                fleets += 1
                lead_time = time
                
        return fleets