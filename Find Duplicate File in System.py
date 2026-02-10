class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content_to_path = defaultdict(list)

        for path in paths:
            parts = path.split(" ")
            root = parts[0]
            for filee in parts[1:]:
                i = filee.find('(')
                j = filee.find(')')

                file_name = filee[:i]
                content = filee[i+1:j]

                whole_path = root + '/' + file_name
                content_to_path[content].append(whole_path)

        return [ group for group in content_to_path.values() if len(group)> 1]        
        
