def root(environ,start_response):
    data = route(environ)
    data =data.encode('utf-8')
    start_response(
        f"200 OK",[
            ("Content-Type","text/html"),
            ("Content-Length",str(len(data)))
        ]
    )
    return iter([data])

def render_template(template_name ="index", context = {}):
    html_main = ""
    html_body =""

    with open("templates/"+template_name+".html","r") as f:
        html_body = f.read()
        html_body =html_body.format(**context)
    with open("templates/index.html","r") as f:
        html_main = f.read()
        html_main = html_main.format(html_body=html_body)

    return html_main

def route(environ):
    path = environ.get('PATH_INFO')[:-1]
    if path == "": return render_template('root')
    return "<h1>404 Page not found</h1>"

if __name__ == "__main__":
    from waitress import serve
    serve(root)
