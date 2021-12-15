from manim import *
from rich.console import group

config.frame_y_radius = 40
config.frame_x_radius = 20

tokenDict = {
    "0": [[-0.5, 0.5, 0], [1.5, 0.5, 0], [1.5, -0.5, 0], [0.5, -0.5, 0], [0.5, -1.5, 0], [-0.5, -1.5, 0]],
    "1": [[-1.5, 0.5, 0], [0.5, 0.5, 0], [0.5, -1.5, 0], [-0.5, -1.5, 0], [-0.5, -0.5, 0], [-1.5, -0.5, 0]],
    "2": [[-0.5, 1.5, 0], [0.5, 1.5, 0], [0.5, 0.5, 0], [1.5, 0.5, 0], [1.5, -0.5, 0], [-0.5, -0.5, 0]],
    "3": [[-0.5, 1.5, 0], [0.5, 1.5, 0], [0.5, -0.5, 0], [-1.5, -0.5, 0], [-1.5, 0.5, 0], [-0.5, 0.5, 0]],
    "4": [[-1.5, 0.5, 0], [1.5, 0.5, 0], [1.5, -0.5, 0], [0.5, -0.5, 0], [0.5, -1.5, 0], [-0.5, -1.5, 0], [-0.5, -0.5, 0], [-1.5, -0.5, 0]],
    "5": [[-1.5, 0.5, 0], [-0.5, 0.5, 0], [-0.5, 1.5, 0], [0.5, 1.5, 0], [0.5, -1.5, 0], [-0.5, -1.5, 0], [-0.5, -0.5, 0], [-1.5, -0.5, 0]],
    "6": [[-1.5, 0.5, 0], [-0.5, 0.5, 0], [-0.5, 1.5, 0], [0.5, 1.5, 0], [0.5, 0.5, 0], [1.5, 0.5, 0], [1.5, -0.5, 0], [-1.5, -0.5, 0], [-1.5, 0.5, 0]],
    "7": [[-0.5, 1.5, 0], [0.5, 1.5, 0], [0.5, 0.5, 0], [1.5, 0.5, 0], [1.5, -0.5, 0], [0.5, -0.5, 0], [0.5, -1.5, 0], [-0.5, -1.5, 0]],
    "8": [[-0.5, 1.5, 0], [0.5, 1.5, 0], [0.5, -1.5, 0], [-0.5, -1.5, 0]],
    "9": [[-1.5, 0.5, 0], [1.5, 0.5, 0], [1.5, -0.5, 0], [-1.5, -0.5, 0]]
}

class drawBoard(Scene):
    def get_token(self, token_id):
        token_points = tokenDict[token_id]
        token_polygon = Polygon(*token_points)
        token_polygon.set_fill(BLUE, 1)
        square = Square(side_length=3)
        return Group(token_polygon, square)

    def get_tokens(self):
        token_ids = [[2,4,6,7], [1,5,3,4], [9,0,2,3], [6,4,5,1], [0,8,6,9]]
        tokens = []
        start_token, end_token = "", ""
        for y in range(len(token_ids)):
            row = token_ids[y]
            for x in range(len(row)):
                token_id = str(row[x])
                token = self.get_token(token_id)
                if y == 0 and x == 0:
                    tokens.append(token)
                    continue
                if x == 0:
                    up_token = tokens[(y*4)-4]
                    token.next_to(up_token, DOWN)
                else:
                    last_token = tokens[-1]
                    token.next_to(last_token, RIGHT)
                tokens.append(token)
                if x == 1 and y == 4:
                    start_token = token
                elif x == 2 and y==0:
                    end_token = token
        token_group = Group(*tokens)
        return token_group, start_token, end_token, tokens

    def get_arrows(self):
        center_left = Arrow(color=DARK_BLUE).shift([-7.5, 0, 0])
        arrows = [center_left]
        arrows.append(center_left.copy().shift(self.UP_SHIFT).shift(self.UP_SHIFT))
        arrows.append(center_left.copy().shift(self.DOWN_SHIFT).shift(self.DOWN_SHIFT))
        arrows.append(center_left.copy().shift([15, 0, 0]).shift(self.UP_SHIFT).flip())
        arrows.append(center_left.copy().shift([15, 0, 0]).shift(self.DOWN_SHIFT).flip())
        return Group(*arrows), arrows

    def create_token_nodes(self, token_refs):
        nodes = []
        for i in range(len(token_refs)):
            nodes.append(Circle().move_to(token_refs[i]).set_stroke(width=15, color=BLUE).set_fill(BLACK, 1))
        return nodes

    def get_edges(self, nodes):
        edge_locs = [[0,1], [1,2], [1,5], [7, 11], [10,11], [12,13], [13,14], [17,13], [14, 18], [18,19]]
        edges = []
        for edge_loc in edge_locs:
            a = edge_loc[0]
            b = edge_loc[1]
            point_a = nodes[a].get_center()
            point_b = nodes[b].get_center()
            edges.append(Line(point_a, point_b).set_stroke(width=15, color=BLUE))
        return edges

    def get_node_uml(self):
        title = Text("class node")
        row = Text("row: int")
        column = Text("column: int")
        token = Text("token: Token")
        is_goal = Text("is_goal: Boolean")
        out_edges = Text("out_edges: List[Edge]")
        path_in_edge = Text("path_in_edge: Edge")
        content_group = VGroup(row, column, token, is_goal, out_edges, path_in_edge).arrange(DOWN, center=False, aligned_edge=LEFT).next_to(title, DOWN, buff=1)
        content_with_title = VGroup(title, content_group)
        rect = SurroundingRectangle(content_with_title, color=WHITE, buff=1)
        full_group = VGroup(rect, title, row, column, token, is_goal, out_edges, path_in_edge)
        text_dict = {
            "title" : title,
            "row" : row, 
            "column" : column,
            "token" : token,
            "is_goal" : is_goal,
            "out_edges" : out_edges,
            "path_in_edge" : path_in_edge,
            "rect" : rect
        }
        return full_group, text_dict

    def animate_node_uml(self, text_group, text_dict):
        text_group.shift(self.UP_SHIFT)
        self.play(Create(text_dict["rect"]))
        self.play(Create(text_dict["title"]))
        self.play(Create(text_dict["row"]))
        self.play(Create(text_dict["column"]))
        self.wait(3)
        self.play(Create(text_dict["token"]))
        self.wait(2)
        self.play(Create(text_dict["is_goal"]))
        self.wait(2)
        self.play(Create(text_dict["out_edges"]))
        self.wait(5)
        self.play(Create(text_dict["path_in_edge"]))
        self.wait(2)
        self.play(text_group.animate.scale(0.5))
        self.play(text_group.animate.shift(self.RIGHT_SHIFT).shift(self.RIGHT_SHIFT).shift(self.RIGHT_SHIFT).shift(self.RIGHT_SHIFT))

    def get_node_cost_labels(self, nodes):
        cost_array = [2,1,0,1,3,2,1,2,4,3,2,3,5,4,3,4,6,5,4,5]
        labels = []
        for i in range(len(nodes)):
            labels.append(Text(str(cost_array[i])).move_to(nodes[i]))
        return labels
    
    def get_modified_graph(self, nodes):
        edge_locs = [[0,1], [1,2], [1,5], [4,8], [7,11], [8,9], [8,12], [12,13], [13,14], [13,17], [14,18]]
        edges = []
        for edge_loc in edge_locs:
            a = edge_loc[0]
            b = edge_loc[1]
            point_a = nodes[a].get_center()
            point_b = nodes[b].get_center()
            edges.append(Line(point_a, point_b).set_stroke(width=15, color=BLUE))
        new_nodes = [node.copy() for node in nodes]
        return VGroup(*edges, *new_nodes), new_nodes

    UP_SHIFT = [0, 3.25, 0]
    DOWN_SHIFT = [0, -3.25, 0]
    RIGHT_SHIFT = [3.25, 0, 0]
    LEFT_SHIFT = [-3.25, 0, 0]

    def get_a_star_pseudo(self):
        text_strings = ["def a_star(start_node: Node):", 
                "   open_nodes = PriorityQueue()",
                "   open_nodes.push(start_node)",
                "   closed_nodes = []",
                "   start_node.stepsToReach = 0",
                "   while not open_nodes.is_empty():",
                "       current_node: Node = open_nodes.pop()",
                "       if current_node.get_is_valid_goal():",
                "           return current_node",
                "       closed_nodes.append(current_node)",
                "       expand_node(current_node, open_nodes, closed_nodes)",
                ]
        inset_levels = [0,1,1,1,1,1,2,2,3,2,2]
        text_mobjects = [Text(string) for string in text_strings]
        for i in range(1, len(text_mobjects)):
            text_mobjects[i].next_to(text_mobjects[i-1], DOWN)
        text_group = VGroup(*text_mobjects).arrange(DOWN, center=False, aligned_edge=LEFT)
        for i in range(len(inset_levels)):
            text_mobjects[i].shift(RIGHT * inset_levels[i])
        return text_group, text_mobjects

    def animate_a_star_pseudo(self, text_mobjects):
        self.play(Create(text_mobjects[0]))
        self.play(Create(text_mobjects[1]))
        self.play(Create(text_mobjects[2]))
        self.wait(15)
        self.play(Create(text_mobjects[3]))
        self.play(Create(text_mobjects[4]))
        self.play(Create(text_mobjects[5])) # while loop start
        self.wait(15)
        self.play(Create(text_mobjects[6]))
        self.wait(7)
        self.play(Create(text_mobjects[7]))
        self.wait(5)
        self.play(Create(text_mobjects[8]))
        self.wait(4)
        self.play(Create(text_mobjects[9]))
        self.play(Create(text_mobjects[10]))
        self.wait(13)

    def construct(self):
        token_group, start_token, end_token, token_refs = self.get_tokens()
        token_group.move_to([0,0,0])        
        player = Circle(color=DARK_BROWN).move_to(start_token).set_fill(RED, 1).scale(0.4)
        goal_marker = Star(color=YELLOW).move_to(end_token).set_fill(YELLOW, 1).scale(0.4)
        free_token = self.get_token("7").next_to(token_group, RIGHT, buff=5)
        arrows_group, arrows_ref = self.get_arrows()
        tokens_row_4 = Group(*token_refs[12:16])

        nodes = self.create_token_nodes(token_refs)
        edges = self.get_edges(nodes)
        part_2_vgroup = VGroup(*edges, *nodes, goal_marker, player)

        text_group, text_dict = self.get_node_uml()
        cost_labels = self.get_node_cost_labels(nodes)
        new_graph, new_nodes = self.get_modified_graph(nodes)
        new_graph = new_graph.next_to(part_2_vgroup, RIGHT, buff=5)
        connection_line = Line(start=LEFT*3, end=RIGHT*3).move_to(nodes[11]).shift([4,0,0]).set_stroke(color=BLUE, width=15)
        new_goal_marker = goal_marker.copy().move_to(new_nodes[2])
        part_3_vgroup = VGroup(connection_line, new_graph, new_goal_marker, part_2_vgroup )

        node_group_box = SurroundingRectangle(new_graph, color=WHITE, buff=1)

        a_star_text_group, text_mobjects = self.get_a_star_pseudo()
        a_star_text_group.move_to([0,0,0])

        self.next_section()
        self.add(token_group)
        self.add_foreground_mobject(player)
        self.add_foreground_mobject(goal_marker)
        self.add(free_token)
        self.add(arrows_group)
        self.wait(8)
        self.play(player.animate.shift(self.UP_SHIFT))
        self.wait(1)
        self.play(player.animate.shift(self.LEFT_SHIFT))
        self.wait(2)
        self.play(free_token.animate.scale(1.5))
        self.play(free_token.animate.scale(1/1.5))
        self.play(arrows_group.animate.scale(1.3))
        self.play(arrows_group.animate.scale(1/1.3))
        self.wait(2)
        self.play(free_token.animate.next_to(token_refs[3*4+3], RIGHT), FadeOut(arrows_ref[-1]))
        self.wait(2)
        self.play(tokens_row_4.animate.shift(self.LEFT_SHIFT), player.animate.shift(self.LEFT_SHIFT), free_token.animate.shift(self.LEFT_SHIFT))
        self.wait(2)
        self.play(token_refs[12].animate.next_to(token_group, RIGHT, buff=5), FadeIn(arrows_ref[-1]))
        self.wait(3)
        self.play(player.animate.shift(self.RIGHT_SHIFT).shift(self.RIGHT_SHIFT).shift(self.RIGHT_SHIFT).shift(self.RIGHT_SHIFT))
        self.wait(3)
        self.play(token_refs[12].animate.next_to(token_refs[13], LEFT), free_token.animate.next_to(token_group))
        self.play(player.animate.shift(self.LEFT_SHIFT).shift(self.LEFT_SHIFT).shift(self.DOWN_SHIFT), tokens_row_4.animate.shift(self.RIGHT_SHIFT))
        self.play(goal_marker.animate.scale(1.5))
        self.play(goal_marker.animate.scale(1/1.5))
        self.wait(31)
        self.play(FadeOut(token_group), FadeOut(arrows_group), FadeOut(free_token), FadeIn(*edges), FadeIn(*nodes) )
        self.wait(8)
        self.play(part_2_vgroup.animate.scale(0.5))
        self.play(part_2_vgroup.animate.shift(self.LEFT_SHIFT).shift(self.LEFT_SHIFT).shift(self.LEFT_SHIFT).shift(self.LEFT_SHIFT))
        self.animate_node_uml(text_group, text_dict)
        self.play(part_2_vgroup.animate.shift(self.RIGHT_SHIFT).shift(self.RIGHT_SHIFT).shift(self.RIGHT_SHIFT).shift(self.RIGHT_SHIFT))
        self.play(part_2_vgroup.animate.scale(2))
        self.wait(8)
        self.play(FadeOut(player), FadeOut(goal_marker), FadeIn(*cost_labels))
        self.wait(30)
        self.play(FadeOut(*cost_labels), FadeOut(text_group), FadeIn(goal_marker))
        self.bring_to_back(connection_line)
        self.play(FadeIn(new_graph), FadeIn(connection_line))
        player.move_to(nodes[11])
        self.play(part_3_vgroup.animate.move_to([0,0,0]))
        self.wait(1)
        self.play(player.animate.move_to(new_nodes[8]))
        self.wait(2)
        self.play(FadeOut(part_2_vgroup), FadeOut(connection_line), FadeOut(new_goal_marker))
        self.play(new_graph.animate.move_to([0,0,0]))
        node_group_box.move_to(new_graph)
        self.play(FadeIn(node_group_box))
        self.wait(48)
        self.next_section()
        self.play(FadeOut(node_group_box), FadeOut(new_graph))
        self.animate_a_star_pseudo(text_mobjects)
        self.wait(5)



class Test(Scene):
    def get_token(self, token_id):
        token_points = tokenDict[token_id]
        token_polygon = Polygon(*token_points)
        token_polygon.set_fill(BLUE, 1)
        square = Square(side_length=3)
        return Group(token_polygon, square)

    def get_tokens(self):
        token_ids = [[2,4,6,7], [1,5,3,4], [9,0,2,3], [6,4,5,1], [0,8,6,9]]
        tokens = []
        start_token, end_token = "", ""
        for y in range(len(token_ids)):
            row = token_ids[y]
            for x in range(len(row)):
                token_id = str(row[x])
                token = self.get_token(token_id)
                if y == 0 and x == 0:
                    tokens.append(token)
                    continue
                if x == 0:
                    up_token = tokens[(y*4)-4]
                    token.next_to(up_token, DOWN)
                else:
                    last_token = tokens[-1]
                    token.next_to(last_token, RIGHT)
                tokens.append(token)
                if x == 1 and y == 4:
                    start_token = token
                elif x == 3 and y==0:
                    end_token = token
        token_group = Group(*tokens)
        return token_group, start_token, end_token, tokens

    UP_SHIFT = [0, 3.25, 0]
    DOWN_SHIFT = [0, -3.25, 0]
    RIGHT_SHIFT = [3.25, 0, 0]
    LEFT_SHIFT = [-3.25, 0, 0]

    def construct(self):
        token_group, start_token, end_token, tokens = self.get_tokens()
        token_group.move_to([0,0,0])

        player = Circle(color=DARK_BROWN).move_to(start_token).set_fill(RED, 1).scale(0.4)
        goal_marker = Star(color=YELLOW).move_to(end_token).set_fill(YELLOW, 1).scale(0.4)
        free_token = self.get_token("7").next_to(token_group, RIGHT, buff=5)
        row1 = Group(*tokens[4:8])
        row2 = Group(*tokens[8:12])

        self.add(token_group)
        self.add_foreground_mobject(player)
        self.add_foreground_mobject(goal_marker)
        self.add(free_token)
        self.wait(5)
        self.play(player.animate.shift(self.UP_SHIFT))
        self.wait(2)
        self.play(free_token.animate.next_to(tokens[8], LEFT))
        self.play(row2.animate.shift(self.RIGHT_SHIFT), free_token.animate.shift(self.RIGHT_SHIFT))
        self.play(tokens[11].animate.next_to(token_group, RIGHT, buff=5))
        self.wait(2)
        self.play(player.animate.shift(self.LEFT_SHIFT))
        self.wait(2)
        self.play(player.animate.shift(self.UP_SHIFT))
        self.play(player.animate.shift(self.UP_SHIFT))
        self.wait(2)
        self.play(tokens[11].animate.next_to(tokens[7], RIGHT))
        self.play(row1.animate.shift(self.LEFT_SHIFT), tokens[11].animate.shift(self.LEFT_SHIFT), player.animate.shift(self.LEFT_SHIFT))
        self.play(player.animate.shift(self.RIGHT_SHIFT).shift(self.RIGHT_SHIFT).shift(self.RIGHT_SHIFT).shift(self.RIGHT_SHIFT))
        self.play(tokens[4].animate.next_to(token_group, RIGHT, buff=5))
        self.wait(2)
        self.play(player.animate.shift(self.UP_SHIFT))
        self.play(player.animate.shift(self.UP_SHIFT))

