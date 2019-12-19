"""
Solution stub for the River Problem.

Fill in the implementation of the `River_problem` class to match the
representation that you specified in problem XYZ.
"""
from searchProblem import Search_problem, Arc



class River_Node():
    """ This class defines the state representation as per the problem. 
    
    Attributes:
        L = Left Side of River
        R = Right Side of River
    """

    def __eq__(self, other):
        if self.L == other.L and self.R == other.R:
            return True

        return False

    def __str__(self):
        """ Generates the human readable representation of Node(Left,Right) of the class."""
        return "Node(L = {0}, R = {1})".format(str(self.L), str(self.R))

    def __init__(self, L, R):
        """ Parameters should be a string of FCG.
        
        L = Left Side of River
        R = Right Side of River
        """
        self.L = set(L)
        self.R = set(R)

class River_problem(Search_problem):
    def start_node(self):
        """returns start node"""
        x = River_Node("FHGR","")
        return x
    
    def is_goal(self,node):
        """is True if node is a goal"""
        
        return (set("FHGR") == node.R)

    def neighbors(self,node):
        """returns a list of the arcs for the neighbors of node"""
        
        valid_arcs = []
        temp_set = set("R")

        # Build valid_arcs list and return.

        if "R" in node.L:
            
            # Add the option of just moving the cart if it creates a valid state.
            temp_node = River_Node(node.L - temp_set, node.R.union(temp_set))
            if self.is_valid_node(temp_node):
                valid_arcs.append(Arc(node, temp_node, 1, "MOVE RAFT TO RIGHT"))

            # For each 
            for item in (node.L - set("R")):
                new_temp_set  = temp_set.union(set(item))
                new_temp_node = River_Node(node.L - new_temp_set, node.R.union(new_temp_set))

                if self.is_valid_node(new_temp_node):
                    valid_arcs.append(Arc(node, new_temp_node, 1, "PICKUP {0} AND MOVE TO RIGHT".format(item)))

        if "R" in node.R:

            temp_node = River_Node(node.L.union(temp_set), node.R - temp_set)
            if self.is_valid_node(temp_node):
                valid_arcs.append(Arc(node, temp_node, 1, "MOVE RAFT TO LEFT"))

            for item in (node.R - set("R")):
                new_temp_set  = temp_set.union(set(item))
                new_temp_node = River_Node(node.L.union(new_temp_set), node.R - new_temp_set)
                
                if self.is_valid_node(new_temp_node):
                    valid_arcs.append(Arc(node, new_temp_node, 1, "PICKUP {0} AND MOVE TO LEFT".format(item)))

        return valid_arcs

    def heuristic(self,n):
        """Gives the heuristic value of node n."""
        return len(n.L)

    def is_valid_node(self,n):
        """Checks if a node is a valid node according to problem"""

        # raft       = set("R")
        # invalid_HG = set("HG")
        # invalid_FH = set("FH")
        # These python sets don't really work as what I expected them to....

        # Check Left
        if "H" in n.L and "G" in n.L and "R" not in n.L: #  ie. The Hen and Grain cannot be left without the farmer (raft)
            return False 
        if "F"  in n.L and "H" in n.L and "R" not in n.L: # ie. The Fox and Hen cannot be left without the farmer (raft)
            return False 
        
        # Check Right
        if "H" in n.R and "G" in n.R and "R" not in n.R: #  ie. The Hen and Grain cannot be left without the farmer (raft)
            return False 
        if "F"  in n.R and "H" in n.R and "R" not in n.R: # ie. The Fox and Hen cannot be left without the farmer (raft)
            return False 

        return True # If both sides of the river are valid then the Node as whole is valid.

if __name__ == "__main__":

    x = River_problem()

    for item in x.neighbors(River_Node("FG", "RH")):
        print(item)

    print()

