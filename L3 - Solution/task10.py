class Polygon:
    # Validation method or method that will be used in that class 
    def is_polygon_can_exist(self, edges):
        sum_ofedges = sum(edges)

        # Validates if the polygon is real?
        for edge in edges:
            if edge >= sum_ofedges - edge or edge <= 0:
                return False

        return True

    def __init__(self, edges):
        self.edges = edges
        if not self.is_polygon_can_exist(edges):
            print(f"Polygon with edges {edges} can't exist.")

    def Set(self, newedges):
        if len(newedges) != len(self.edges):
            print(f"Error. New polygon have different number of edges.")
            return
        self.edges = newedges
        if not self.is_polygon_can_exist(newedges):
            print(f"Polygon with edges {newedges} can't exist.")

    def Print(self):
        if self.is_polygon_can_exist(self.edges):
            print(f"It's {len(self.edges)}-gon with length of edges: ", end="")        
            for i in range(len(self.edges)-1):
                print(self.edges[i], end=", ")
            print(self.edges[-1], end=".\n")
        else:
            print(f"Polygon with edges {self.edges} can't exist.")

class RightTriangle(Polygon):
    def is_right_triangle(cls, edges):
        if len(edges) != 3:
            return False
        for i in range(3):
            edge1, edge2, edge3 = edges[i], edges[i-1], edges[i-2]
            if edge1 * edge1 == edge2 * edge2 + edge3 * edge3:
                return True
        return False

    def __init__(self, a, b, c):
        super().__init__([a,b,c])
        if not self.is_right_triangle(self.edges):
            print(f"It's not right triangle.")
    
    def Set(self, a, b, c):
        super().Set([a,b,c])
        if not self.is_right_triangle(self.edges):
            print(f"It's not right triangle.")
    
    def Print(self):
        if self.is_right_triangle(self.edges):
            print(f"It's not right triangle.")
        else:            
            print(f"It's right triangle with length of edges: ", end="")
            for i in range(len(self.edges)-1):
                print(self.edges[i], end=", ")
            print(self.edges[-1], end=".\n")


a = Polygon([1,2,3,4])
a.Print()
a.Set([9,8])
a.Print()