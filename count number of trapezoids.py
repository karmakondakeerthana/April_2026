class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        n = len(points)
        if n < 4:
            return 0
        def norm_slope(dy, dx):
            if dx == 0:
                return (1, 0)
            if dy == 0:
                return (0, 1)
            g = gcd(dy, dx)
            dy //= g
            dx //= g
            if dx < 0:
                dy = -dy
                dx = -dx
            return (dy, dx)
        slope_line_points = defaultdict(lambda: defaultdict(set))
        mid_map = defaultdict(lambda: defaultdict(int))
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i+1, n):
                x2, y2 = points[j]
                dy = y2 - y1
                dx = x2 - x1
                s = norm_slope(dy, dx)
                v = s[0] * x1 - s[1] * y1
                slope_line_points[s][v].add(i)
                slope_line_points[s][v].add(j)
                mid_key = (x1 + x2, y1 + y2)
                mid_map[mid_key][s] += 1
        def C2(x):
            return x * (x - 1) // 2 if x >= 2 else 0
        total_pairs_parallel_lines = 0
        for s, line_map in slope_line_points.items():
            A = []
            for v, pts in line_map.items():
                t = len(pts)
                a = C2(t)  
                if a > 0:
                    A.append(a)
            if not A:
                continue
            sumA = sum(A)
            sumA2 = sum(a * a for a in A)
            total_pairs_parallel_lines += (sumA * sumA - sumA2) // 2
        parallelograms = 0
        for mid_key, slope_counts in mid_map.items():
            k = sum(slope_counts.values())          
            if k < 2:
                continue
            total_pairs = C2(k)                    
            same_slope_pairs = sum(C2(cnt) for cnt in slope_counts.values()) 
            parallelograms += (total_pairs - same_slope_pairs)
        return total_pairs_parallel_lines - parallelograms
