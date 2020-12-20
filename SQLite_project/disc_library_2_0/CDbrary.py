from app import app, db, routes, models
from app.models import Artist, Disc, ArtistDisc, Rented

#Creating a shell for models.py
@app.shell_context_processor
def make_shell_context():
   return {
       "db": db,
       "Artist": Artist,
       "Disc": Disc,
       "ArtistDisc": ArtistDisc,
       "Rented": Rented
   }

if __name__ == "__main__":
    app.run(debug=True)