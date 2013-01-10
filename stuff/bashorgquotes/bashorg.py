import re
import HTMLParser
import requests
import sys

def bashierise(quote_no):
    if quote_no.isdigit():
        req = requests.get("http://bash.org/?%d" % int(quote_no))
        if req.ok:
            src = req.content.replace("\n", "").replace("\r", "")
            quote_p = re.compile(r".*<p class=\"qt\">(.+)</p>.*")
            match = quote_p.match(src)
            if match:
                quote = match.group(1)
                parser = HTMLParser.HTMLParser()
                quote = parser.unescape(quote)
                quote = quote.replace("<br />", "\n")
                return quote
    return "Quote %d does not exist." % int(quote_no)

def main():
    quote_no = sys.argv[1] if len(sys.argv) > 1 else "268981"
    q = bashierise(quote_no)
    if q:
        print q
    
if __name__ == "__main__":
    main()
