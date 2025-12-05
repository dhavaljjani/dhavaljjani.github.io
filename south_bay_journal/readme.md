# South Bay Journal blog

This is my newsletter blog which is written in just simple HTML, CSS, and some JS.

## Layout for new blog post html pages:

~~~
<!doctype html>
<html lang="en">
    <head>
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
        <link rel="stylesheet" href="/south_bay_journal/blog.css">
        <title>*DATE*</title> 
    </head>
    <body>
        <h1> *TITLE OF POST* <h1>
        <h2> *SECONDARY LINE* <h2>
        <div class="blog_post">
            *BLOG BODY with images HERE*
            Text written in class=text_div as <p>
        </div>
    </body>
</html>
~~~

- Remember to put images used in /southbayjournal/archive/*DATE*/img/