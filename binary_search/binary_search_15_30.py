words = list(input().split())  # frodo  front frost frozen frame kakao
queries = list(input().split())  # fro?? ????o fr??? fro??? pro?

def solution(words, queries):
    cnts = []
    for query in queries:
        if query[-1] == '?':
            p = query.find('?')
            cnt = 0
            for word in words:
                if word.startswith(query[:p]) and len(word) == len(query):
                    cnt += 1
            cnts.append(cnt)
        elif query[0] == '?':
            p = query[::-1].find('?')
            cnt = 0
            for word in words:
                if word.endswith(query[-p:]) and len(word) == len(query):
                    cnt += 1
            cnts.append(cnt)
    return cnts  

solution(words, queries)