from url_shortener import db

class URL(db.Model):
    short_url = db.Column(db.String(50), primary_key=True)
    redirect_url = db.Column(db.String(150), nullable=False)
    password = db.Column(db.String(60), nullable=True)

    def __repr__(self):
        return f"URL('{short_url} - {redirect_url}')"