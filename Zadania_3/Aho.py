class TrieNode:
    def __init__(self):
        
        self.children = {}
        self.output = []
        self.fail = None


def build_automaton(keywords):
    root = TrieNode()
    for keyword in keywords:
        node = root
        for char in keyword:
            node = node.children.setdefault(char, TrieNode()) # if not in dict create new entry and return
        
        node.output.append(keyword)

    queue = []
    
    for node in root.children.values():
        queue.append(node)
        node.fail = root

    while queue:
        current_node = queue.pop(0)
        for key, next_node in current_node.children.items():
            queue.append(next_node)
            fail_node = current_node.fail
            while fail_node and key not in fail_node.children:
                fail_node = fail_node.fail
            next_node.fail = fail_node.children[key] if fail_node else root
            next_node.output += next_node.fail.output

    return root

def search_text(text, keywords):
    root = build_automaton(keywords)
    result = {keyword: [] for keyword in keywords}

    current_node = root
    for i, char in enumerate(text):
        while current_node and char not in current_node.children:
            current_node = current_node.fail

        if not current_node:
            current_node = root
            continue

        current_node = current_node.children[char]
        for keyword in current_node.output:
            result[keyword].append(i - len(keyword) + 1)

    return result


if __name__ == "__main__":
    text1 = "truetreerastreetriutrue"
    arr1 = ["tree", "true"]
    result1 = search_text(text1, arr1)
    print(result1)
