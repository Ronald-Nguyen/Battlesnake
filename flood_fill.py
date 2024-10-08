"""
Ronald Nguyen 222200308
Anastasiia Rudyk 222202247
Florin Josua Seiberling 222202338
Amina Tolikova 222201628
Karola Melisa Yegen 222202033
Paloma Kopplow 222200077
"""

class flood_fill:

    # Flood fill algorithm for maximizing accessible area
    def flood_fill(board, x, y, width, height, obstacles):
      queue = [(x, y)]
      visited = set(queue)
      count = 0
    
      while queue:
          cx, cy = queue.pop(0)
          count += 1
    
          for nx, ny in [(cx+1, cy), (cx-1, cy), (cx, cy+1), (cx, cy-1)]:
              if 0 <= nx < width and 0 <= ny < height and (nx, ny) not in visited and (nx, ny) not in obstacles:
                  visited.add((nx, ny))
                  queue.append((nx, ny))
    
      return count