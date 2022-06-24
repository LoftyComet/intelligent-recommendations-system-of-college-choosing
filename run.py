from config import app
from views.data_view import data
from views.page_view import page

app.register_blueprint(data, url_prefix="/data")
app.register_blueprint(page, url_prefix="/")


if __name__ == '__main__':
    app.run()