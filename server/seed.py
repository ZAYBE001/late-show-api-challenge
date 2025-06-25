from server.app import app
from server.extensions import db
from server.models import Guest, Episode, Appearance



def seed_data():
    with app.app_context():
        # Clear existing data
        db.session.query(Appearance).delete()
        db.session.query(Episode).delete()
        db.session.query(Guest).delete()
        db.session.commit()

        # Create guests
        guest1 = Guest(name="John Doe", occupation="Actor")
        guest2 = Guest(name="Jane Smith", occupation="Comedian")
        guest3 = Guest(name="Alice Johnson", occupation="Musician")

        # Create episodes
        episode1 = Episode(date="2023-10-10", number=1)
        episode2 = Episode(date="2023-10-17", number=2)
        episode3 = Episode(date="2023-10-24", number=3)

        # Create appearances
        appearance1 = Appearance(rating=5, guest=guest1, episode=episode1)
        appearance2 = Appearance(rating=4, guest=guest2, episode=episode1)
        appearance3 = Appearance(rating=3, guest=guest3, episode=episode2)
        appearance4 = Appearance(rating=5, guest=guest1, episode=episode3)

        # Add to session and commit
        db.session.add_all([guest1, guest2, guest3, episode1, episode2, episode3, appearance1, appearance2, appearance3, appearance4])
        db.session.commit()

if __name__ == '__main__':
    seed_data()