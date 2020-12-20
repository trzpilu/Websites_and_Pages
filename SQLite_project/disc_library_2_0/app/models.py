from datetime import datetime
import db

# SETTING UP CLASSES
# Setting up Artists.
class Artist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    artist = db.Column(db.String(100), index=True)
    about = db.Column(db.String(200))
    disc_artist = db.relationship("Disc", backref="artist", lazy="dynamic")
    disc_a_d = db.relationship("ArtistDisc", backref="artist", lazy="dynamic")

    def __str__(self):
        return f"<Artist: {self.name}>"
# Setting up CDs.
class Disc(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, index=True)
    genre = db.Column(db.Text)
    year = db.Column(db.Integer)
    description = db.Column(db.Text)
    artist_id = db.Column(db.Integer, db.ForeignKey('artist.id'))
    artists = db.relationship("ArtistDisc", backref="disc", lazy="dynamic")
    rented = db.relationship("Rented", backref="disc", lazy="dynamic")

    def __str__(self):
        return f"<Book: {self.id} {self.title[:50]}...>"
# Setting up Artist-Disc relationship    
class ArtistDisc(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    artist_id = db.Column(db.Integer, db.ForeignKey('artist.id'))
    disc_id = db.Column(db.Integer, db.ForeignKey('disc.id'))

    def __str__(self):
        return f"<ArtistCDs: {self.id} {self.artist_id} {self.cd_id}...>"

# Setting up rentals.
class Rented(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    disc_id = db.Column(db.Integer, db.ForeignKey('disc.id'))

    def __str__(self):
        return f"<Rented: {self.id}...>"

