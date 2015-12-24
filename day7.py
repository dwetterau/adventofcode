__author__ = 'david'

class Node(object):
    def __init__(self, key, input_value=None):
        self.edges = []
        self.key = key
        self.input_value = input_value

class Edge(object):
    TYPES = {"NOT", "OR", "AND", "LSHIFT", "RSHIFT", "NOOP", "1AND"}

    def __init__(self, t, extra=None, other_input=None):
        assert t in Edge.TYPES, "%s" % t
        self.type = t
        self.target = None
        self.extra = extra
        self.other_input = other_input

    def set_target(self, node):
        self.target = node

    def get_output(self, in1=None, in2=None):
        if self.type == "NOT":
            return ~in1
        if self.type == "LSHIFT":
            return in1 << self.extra
        elif self.type == "RSHIFT":
            return in1 >> self.extra
        elif self.type == "1AND":
            return in1 & 1
        elif self.type == "OR":
            if in1 is None or in2 is None:
                raise ValueError()
            return in1 | in2
        elif self.type == "AND":
            if in1 is None or in2 is None:
                raise ValueError()
            return in1 & in2
        elif self.type == "NOOP":
            if in1 is None:
                raise ValueError()
            return in1
        assert False, self.type

    @staticmethod
    def build(command):
        # Special case the no-op
        if len(command) == 2:
            return Edge("NOOP"), command[-1], None

        extra = None
        other_input = None
        if command[0] in {"LSHIFT", "RSHIFT"}:
            extra = int(command[1])
        if command[0] in {"AND", "OR", "1AND"}:
            other_input = command[1]
        e = Edge(command[0], extra, other_input)
        return e, command[-1], other_input

world = {}
def apply_line(line):
    global world
    command = line.split(" ")
    try:
        v = int(command[0])
        if command[1] != "->":
            raise ValueError()

        # This is a node, add it to the graph
        if command[2] in world:
            world[command[2]].input_value = v
        else:
            world[command[2]] = Node(command[2], v)
        print(command)
    except ValueError:
        # This is an edge, add it to the graph. Be careful about non-existent Nodes
        # Wow this sucks, I have to special case NOT...
        if command[0] == "1":
            command[1] = "1AND"

        if command[0] == "NOT":
            command[0], command[1] = command[1], command[0]

        edge, target_id, other_input = Edge.build(command[1:])
        if target_id not in world:
            world[target_id] = Node(target_id)
        edge.set_target(world[target_id])

        parent = command[0]
        if parent == "1":
            parent = other_input

        for i in [parent]:
            if i not in world:
                world[i] = Node(i)
            world[i].edges.append(edge)

file = open("input")
total = 0
for line in file:
    apply_line(line.strip())

# visualize code
import json
import random
out = dict(
    nodes=[dict(title=x.key, id=x.key, x=str(random.random())[2:5], y=str(random.random())[2:5]) for x in world.values()],
    edges=[dict(source=x.key, target=y.target.key) for x in world.values() for y in x.edges]
)
print(json.dumps(out))


# Do the final traversal
# Find the nodes that have assigned values
done = set()
for _ in range(len(world)):
    queue = []
    for key, node in world.items():
        if node.input_value is not None and key not in done:
            queue.append(node)
    print([x.key for x in queue])
    while queue:
        added_again = False
        n = queue.pop(0)
        if n.input_value is None:
            # we thought we could traverse past this node but we couldn't...
            assert False
        not_done = False
        for edge in n.edges:
            other_value = None
            if edge.other_input is not None:
                o = world[edge.other_input]
                if o.input_value is None:
                    # We can't do this computation yet...
                    not_done = True
                    continue
                other_value = o.input_value
            new_value = edge.get_output(n.input_value, other_value)

            assert edge.target.input_value is None or edge.target.input_value == new_value
            if edge.target.input_value is None:
                print("traversed", n.key, edge.other_input, edge.type, edge.target.key)
                edge.target.input_value = new_value
                queue.append(edge.target)

        if not not_done:
            done.add(n.key)

for key, node in world.items():
    print("%s: %s" % (key, node.input_value))

print(world["a"].input_value)
