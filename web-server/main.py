import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get('/')
def get_list():
    return[1,2,3]


@app.get('/contact',response_class=HTMLResponse)
def get_list():
    return """
<head>
  <meta charset="utf-8">
  <title>HTML</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="estilo.css">
</head>

<body>
  <p>Esta página web es una página HTML válida.</p>
</body>
    """



def run():
    store.get_categories()


if __name__ == '__main__':
    run()