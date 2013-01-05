#!/usr/bin/python
from operator import itemgetter

def parse_scoreboard():
    raw = file("scoreboard").read()
    raw_l = raw.split("\n")
    scores = []
    for i in raw_l:
        if not i == "":
            scores.append(i.split(":::"))
    return scores

def main():
    scores = parse_scoreboard()
    leaders = {}
    for i in scores:
        if i[1] not in leaders.keys():
            leaders[i[1]] = int(i[3])
        else:
            leaders[i[1]] += int(i[3])
    sort = sorted(leaders.items(), key=itemgetter(1), reverse=True)
    html = '<div style="width:100%"><table><thead><tr><th scope="col">No.</th><th scope="col">Name/Handle</th><th scope="col">Score</th></thead><tbody>'
    for i in range(len(sort)):
        html += '<tr><td>%d.</td><td>%s</td><td align="right">%s</td></td></tr>\n' % (i, sort[i][0], sort[i][1])
    html += "</tbody></table><br /><br /><h2>Narwhals Cant Into Web Design</h2></div>"
    response = "HTTP/1.1 200 OK\n\n%s%s\n  </div>\n</body>\n</html>" % (file("page.html").read(), html)
    print response



    
    
if __name__ == "__main__":
    main()
