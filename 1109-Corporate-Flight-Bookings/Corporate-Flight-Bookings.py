from typing import List

class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        seats = [0] * n
        
        for reserva in bookings:
            primeiro, ultimo, assentos_reservados = reserva
            
            seats[primeiro - 1] += assentos_reservados
            if ultimo < n:
                seats[ultimo] -= assentos_reservados
        
        for i in range(1, n):
            seats[i] += seats[i - 1]
            
        return seats