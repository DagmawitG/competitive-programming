# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        
        domainName = startUrl.split("http://")[1].split('/')[0]
        visited = set()
        answer = [startUrl]
        def bfs(url):
            queue = deque([(url)]) 
            visited.add(url)
            while queue:
                
                url = queue.popleft()
                getHtmlUrls = htmlParser.getUrls(url)
                for currentUrl in getHtmlUrls:
                    if currentUrl not in visited and currentUrl.split("http://")[1].split('/')[0] == domainName:
                        answer.append(currentUrl)
                        visited.add(currentUrl)
                        queue.append(currentUrl)
                        
                    else:
                        continue
        bfs(startUrl)
        return answer
    
        
        