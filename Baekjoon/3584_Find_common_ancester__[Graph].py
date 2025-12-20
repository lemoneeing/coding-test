import sys

input = sys.stdin.readline

class TreeNode:
    def __init__(self, v):
        self.value = v
        self.parent:TreeNode = None

    def __repr__(self):
        return str(self.value)


class Tree:
    root = None

    def __init__(self, node_cnt):
        self.root = None
        self.NODE_COUNT = node_cnt
        self.nodes = [0] * (self.NODE_COUNT+1)
        self.edges = [[] for _ in range(node_cnt+1)]

    def add_node(self, v):
        self.nodes[v] = TreeNode(v)

    def connect_nodes(self, pv, cv):
        '''
        두 노드를 연결하는 엣지 저장
        :param pv: 부모 노드 
        :param cv: 자식 노드
        '''
        if self.nodes[pv] == 0:
            self.add_node(pv)

        if self.nodes[cv] == 0:
            self.add_node(cv)

        self.edges[pv].append(cv)
        self.nodes[cv].parent = self.nodes[pv]
        if self.root == self.nodes[cv]:
            self.root = None

        if self.root is None and self.nodes[pv].parent is None:
            self.root = self.nodes[pv]


    def find_path_to_root(self, child):
        '''
        child 에서 루트 노드까지의 경로 탐색
        '''

        curr = self.nodes[child]
        path = [child]
        while curr.value != self.root.value:
            curr = curr.parent
            path.append(curr.value)

        path.append(self.root.value)

        return path


def solution():
    TC = int(input().strip())
    for _ in range(TC):
        N = int(input().strip())
        tree = Tree(N)

        for __ in range(N-1):
            v1, v2 = map(int, input().strip().split())

            tree.connect_nodes(v1, v2)

        n1, n2 = map(int, input().strip().split())

        # 한 노드에서 루트노드까지 가는 경로를 탐색
        from_n1_to_root = tree.find_path_to_root(n1)
        
        # 나머지 노드에서 하나씩 부모노드로 탐색하면서 위에서 찾은 상대 ~ 루트 경로를 만나는지 확인
        curr = tree.nodes[n2]
        while curr.value != tree.root.value:
            if curr.value in from_n1_to_root:
                print(curr.value)
                break

            curr = curr.parent

        # 루트노드가 유일한 공통 조상일경우 따로 출력
        if curr.value == tree.root.value:
            print(curr.value)

solution()