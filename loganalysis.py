
from flask import Flask, request, redirect, url_for

from loganalysisdb import get_titles, get_authors, get_errors

import bleach

app = Flask(__name__)
action = ''
# HTML template for the forum page
HTML_WRAP = '''\
<!DOCTYPE html>
<html>
  <head>
    
    <style>
    
      h1, form,a,h3 { text-align: center; }
      div{padding:2px; margin:2px; text-align:center }
      
     .title{color:blue}
     .views{color:red}
     body {
    height:100%%;}
     

    </style>
  </head>
  <body>
   <div id = main> 
   <!-- post content will go here -->
<div>

%s
%s
</div>
<div>

%s
%s
</div>
<div>

%s
%s
</div>
</div>   
'''

# HTML template for an individual comment
TITLE = ''' 
\
<h2>%s</h2>
'''
QUESTION = '''
 \
    
    <p> -Title: <span class=title>"%s"</span>  -- <span class=views>%s</span> views</p>
    
    
 
'''
AUTHOR = '''
 \
    
    <p> -AUTHOR: <span class=title>"%s"</span>  -- <span class=views>%s</span> views</p>
    
    
 
'''
ERROR = '''
 \
    
    <p> -Date: <span class=title>"%s"</span>  -- <span class=views>%s%%</span> errors</p>
    
    
 
'''

@app.route('/', methods=['GET'])
def main():
  x = bleach.clean(HTML_WRAP, tags=[u'html', u'body', u'head', u'style',
                                    u'div', u'button', u'form', u'h1', u'textarea'], strip=True)
  titles = get_titles()
  authours = get_authors()
  errors = get_errors()

  questionTitle1 = "".join(TITLE % ("1.What are the most popular three articles of all time?"))
  question1 = "".join(QUESTION % ( title, views) for title, views in titles)

  questionTitle2 = "".join(TITLE % ("2.Who are the most popular article authors of all time?"))
  question2 = "".join(AUTHOR % ( title, views) for title, views in authours)

  questionTitle3 = "".join(TITLE % ("3. On which days did more than 1% of requests lead to errors? "))
  question3 = "".join(ERROR % ( Error_DATE, precentage) for Error_DATE, precentage in errors)

  html = x % (questionTitle1,question1,questionTitle2,question2,questionTitle3,question3)
  return html



if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8000)
