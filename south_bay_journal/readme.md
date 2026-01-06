# South Bay Journal blog

This is for this newsletter blog which is written in just simple HTML, CSS, and some JS. A way to not have to rely on substack.

## Layout for new blog post html pages:

~~~
<!doctype html>
    <html lang="en">
        <head>
            <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
            <link rel="stylesheet" href="../blog.css">
            <title>TITLE</title>
            <meta charset="UTF-8">
            <meta name="TITLE" content="DESCRIPTION">
        </head>
        <body>
            <h1> TITLE </h1>
            <h3> DESCRIPTION </h3>
            <h5> Originally posted on substack on DATE </h5>
            <div class="blog_post">
                BLOG_BODY
                <a href="/south_bay_journal/home.html"> HOME </a>
            </div>
            <div style="align-items:center;">
                [optional embedded spotify iframe]
            </div>
        </body>
    </html>
~~~